/*global $*/

$(function() {

    // Button to grab the headlines from the homepage
    $('#btn-get-headlines').click(function() {
        // Check if table already populated
        if ($('#results-table-body tr').length > 1) {
            $('#results-table-body').children().remove()
            $('#btn-get-meta, #btn-get-csv').hide()
            $('td.meta').remove()
            $('#btn-get-headlines').removeClass('btn-warning').addClass('btn-info').text('Get headlines');
            return false
        }

        // Show the progress bar
        $('#progress-bar').show();

        // Populate table with data from The Guardian homepage
        $.get("/guardian_homepage", function(data) {
            var row_number = 1;
            data.forEach(function(item) {
                $('#results-table-body').append('<tr></tr>');
                var row = $('#results-table-body tr:nth-of-type(' + row_number + ')');
                row.append('<th class="headline_title">' + item['headline_title'] + '</th>');
                row.append('<td class="headline_kicker">' + item['headline_kicker'] + '</td>');
                row.append('<td class="headline_body">' + item['headline_body'] + '</td>');
                row.append('<td class="headline_link"><a href="' + item['headline_link'] + '">' + item['headline_link'] + '</a></td>');
                row_number += 1;
            })
            // When loading is complete, hide the progress bar
            $('#btn-get-meta').show().removeClass('btn-warning').addClass('btn-info').text('Retrieve meta data');
            $('#btn-get-headlines').removeClass('btn-info').addClass('btn-warning').text('Remove headlines');
        });
        $('#progress-bar').hide();
    })

    // Get page by page meta data
    $('#btn-get-meta').click(function() {
        // Check if table already populated
        if ($("td.article_date").length > 1) {
            $('td.meta').remove()
            $('#btn-get-meta').removeClass('btn-warning').addClass('btn-info').text('Retrieve meta data');
            $('#btn-get-csv').hide();
            return false
        }
        // Show the progress bar
        $('#progress-bar').show();

        //  Number of articles to get meta data for
        var article_count = $('#results-table-body tr .headline_link a').length

        // Progress bar initial state
        var progress_bar_position = 0

        // Set ticker initial state

        // loop through an array of length # of articles
        $.each(new Array(article_count), function(index) {
            $.get("/get_per_article_meta_data", { 'position': index })
                .done(function(item_outer) {
                    // Establish variables
                    var item = item_outer[0];
                    var row_number = index + 1
                    var row = $('#results-table-body tr:nth-of-type(' + row_number + ')');

                    row.append('<td class="meta article_authors">' + item['authors'] + '</td>');
                    row.append('<td class="meta article_keywords">' + item['keywords'] + '</td>');
                    row.append('<td class="meta article_date">' + item['date'] + '</td>');


                    // Advance the progress bar
                    progress_bar_position += 1;
                    $('.progress-bar').css('width', progress_bar_position / article_count * 100 + '%')

                    // Clean up when all article meta data is loaded into the table
                    if (progress_bar_position + 1 == article_count) {
                        $('#progress-bar').slideUp('slow');
                        $('.progress-bar').css('width', '0%');
                        $('#btn-get-meta').removeClass('btn-info').addClass('btn-warning').text('Remove meta data');
                        $('#btn-get-csv').show();
                    }
                })
        })
    })

    $("#btn-get-csv").click(function() {
        var table_data = {};

        $('tr:gt(1)').each(function(outer_index) {
            var row = [];
            // console.log(this);
            $(this).find('th, td').each(function() {
                console.log($(this).text())
                row.push($(this).text());
            });
            console.log(row)
            // console.log(row)
            table_data[outer_index] = row;
        })
        // $(selector).post(URL,data,function(data,status,xhr),dataType)
        
        console.log('sending post to /download')
        var data = JSON.stringify(table_data)
        $.post(
            '/csvmaker', 
            data)
            .success($('#secret-form-submit').submit())
    })


    $('.circle').click(function(){
        $('.circle').removeClass('circle-selected');
        $(this).addClass('circle-selected');
        var id = $(this).attr('id');
        
    });


});
