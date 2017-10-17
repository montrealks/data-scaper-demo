__author__ = "Kris"
from bs4 import BeautifulSoup
import requests





"""
from flaskbp.src.models import GetTheGaurdianData as g
"""


ghp = """


<!DOCTYPE html>
<html id="js-context" class="js-off is-not-modern id--signed-out" lang="en" data-page-path="/international">
<head>
<title>News, sport and opinion from the Guardian's global edition | The Guardian</title>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=Edge"/>
<meta name="format-detection" content="telephone=no"/>
<meta name="HandheldFriendly" content="True"/>
<meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
<link rel="dns-prefetch" href="https://assets.guim.co.uk/"/>
<link rel="dns-prefetch" href="https://i.guim.co.uk"/>
<link rel="dns-prefetch" href="https://api.nextgen.guardianapps.co.uk"/>
<link rel="dns-prefetch" href="https://hits-secure.theguardian.com"/>
<link rel="dns-prefetch" href="//j.ophan.co.uk"/>
<link rel="dns-prefetch" href="//ophan.theguardian.com"/>
<link rel="dns-prefetch" href="//beacon.gu-web.net"/>
<link rel="dns-prefetch" href="//www.google-analytics.com"/>
<link rel="dns-prefetch" href="//sb.scorecardresearch.com"/>
<link rel="apple-touch-icon" sizes="152x152" href="https://assets.guim.co.uk/images/favicons/451963ac2e23633472bf48e2856d3f04/152x152.png"/>
<link rel="apple-touch-icon" sizes="144x144" href="https://assets.guim.co.uk/images/favicons/1a3f98d8491f8cfdc224089b785da86b/144x144.png"/>
<link rel="apple-touch-icon" sizes="120x120" href="https://assets.guim.co.uk/images/favicons/cf23080600002e50f5869c72f5a904bd/120x120.png"/>
<link rel="apple-touch-icon" sizes="114x114" href="https://assets.guim.co.uk/images/favicons/f438f6041a4c1d0289e6debd112880c2/114x114.png"/>
<link rel="apple-touch-icon" sizes="72x72" href="https://assets.guim.co.uk/images/favicons/b5050517955e7cf1e493ccc53e64ca05/72x72.png"/>
<link rel="apple-touch-icon-precomposed" href="https://assets.guim.co.uk/images/favicons/4fd650035a2cebafea4e210990874c64/57x57.png"/>
<link rel="manifest" href="/2015-06-24-manifest.json" crossorigin="use-credentials">
<link rel="shortcut icon" type="image/png" href="https://assets.guim.co.uk/images/favicons/79d7ab5a729562cebca9c6a13c324f0e/32x32.ico"/>
<link rel="alternate" href="https://www.theguardian.com/uk" hreflang="en-GB"/>
<link rel="alternate" href="https://www.theguardian.com/us" hreflang="en-US"/>
<link rel="alternate" href="https://www.theguardian.com/au" hreflang="en-AU"/>
<link rel="canonical" href="https://www.theguardian.com/international"/>
<meta name="apple-mobile-web-app-title" content="Guardian"/>
<meta name="application-name" content="The Guardian"/>
<meta name="msapplication-TileColor" content="#005689"/>
<meta name="theme-color" content="#005689">
<meta name="msapplication-TileImage" content="https://assets.guim.co.uk/images/favicons/f06f6996e193d1ddcd614ea852322d25/windows_tile_144_b.png"/>
<meta name="apple-itunes-app" content="app-id=409128287, app-argument=https://www.theguardian.com/international, affiliate-data=ct=newsmartappbanner&pt=304191">
<link rel="publisher" href="https://plus.google.com/113000071431138202574"/>
<meta name="description" content="Latest international news, sport and comment from the Guardian"/>
<meta property="og:url" content="http://www.theguardian.com/international"/>
<meta property="og:description" content="Latest international news, sport and comment from the Guardian"/>
<meta property="og:image" content="https://assets.guim.co.uk/images/2170b16eb045a34f8c79761b203627b4/fallback-logo.png"/>
<meta property="al:ios:url" content="gnmguardian://international?contenttype=front&amp;source=applinks"/>
<meta property="og:type" content="website"/>
<meta property="al:ios:app_store_id" content="409128287"/>
<meta property="fb:app_id" content="180444840287"/>
<meta property="al:ios:app_name" content="The Guardian"/>
<meta property="og:site_name" content="the Guardian"/>
<meta name="twitter:app:id:iphone" content="409128287"/>
<meta name="twitter:app:name:googleplay" content="The Guardian"/>
<meta name="twitter:app:name:ipad" content="The Guardian"/>
<meta name="twitter:site" content="@guardian"/>
<meta name="twitter:app:url:ipad" content="gnmguardian://international?contenttype=front&amp;source=twitter"/>
<meta name="twitter:card" content="summary"/>
<meta name="twitter:app:name:iphone" content="The Guardian"/>
<meta name="twitter:app:id:ipad" content="409128287"/>
<meta name="twitter:app:id:googleplay" content="com.guardian"/>
<meta name="twitter:app:url:iphone" content="gnmguardian://international?contenttype=front&amp;source=twitter"/>
<meta name="twitter:dnt" content="on">
<meta property="fb:pages" content="10513336322"/>
<meta property="fb:pages" content="456740217686384"/>
<meta property="fb:pages" content="516977308337360"/>
<script data-schema="Organization" type="application/ld+json">
        {"name":"The Guardian","url":"http://www.theguardian.com/","logo":"https://assets.guim.co.uk/images/favicons/451963ac2e23633472bf48e2856d3f04/152x152.png","sameAs":["https://www.facebook.com/theguardian","https://twitter.com/guardian","https://plus.google.com/+theGuardian","https://www.youtube.com/user/TheGuardian"],"@type":"Organization","@context":"http://schema.org"}
    </script>
<script data-schema="WebPage" type="application/ld+json">
        {"@id":"https://www.theguardian.com/international","potentialAction":{"@type":"ViewAction","target":"android-app://com.guardian/https/www.theguardian.com/international"},"@type":"WebPage","@context":"http://schema.org"}
    </script>
<link rel="alternate" href="ios-app://409128287/gnmguardian/international?contenttype=front&amp;source=google"/>
<meta name="twitter:url" content="https://www.theguardian.com/international"/>
<meta property="og:title" content="News, sport and opinion from the Guardian's global edition | The Guardian"/>
<link rel="alternate" href="https://www.theguardian.com/international/rss" title="RSS" type="application/rss+xml">
<style class="js-loggable">
    .svg .i,
    .svg .caption:before,
    .svg figcaption:before,
    .svg blockquote.quoted:before {
        background-image: none;
    }
    .is-updating {
        background-image: url(https://assets.guim.co.uk/images/f2465f9293ea046b91128035ecf4cdd5/auto-update-activity.gif);
    }
    .is-updating--dark {
        background-image: url(https://assets.guim.co.uk/images/614abf55ccbb65d1bb691aa8bf64fd7f/auto-update-activity-dark.gif);
    }
    .tweet__user-name:before {
        background-image: url(https://assets.guim.co.uk/images/twitter/ca807fd6567f678fc0981a4ab6904fbe/bird.svg);
    }

    .no-svg .inline-guardian-logo-160 { background-image: url(https://assets.guim.co.uk/images/logo/c53d8a40a4962863a36388902a43f279/guardian-logo-160.png); }
    .no-svg .inline-guardian-logo-320 { background-image: url(https://assets.guim.co.uk/images/logo/951ac05886372ebb77554a9dd4ae420f/guardian-logo-320.png); }
    .no-svg .inline-observer-logo-160 { background-image: url(https://assets.guim.co.uk/images/logo/bee4ad72a1badb16d72a86484d192a1c/observer-logo-160.png); }
    .no-svg .inline-observer-logo-320 { background-image: url(https://assets.guim.co.uk/images/logo/c5669a2096d808752b0d5798be09ab0f/observer-logo-320.png); }
</style>
<!--[if (lt IE 9)&(!IEMobile)]>





    <link rel="stylesheet" type="text/css" href="https://assets.guim.co.uk/stylesheets/2dc5cd34723641950a3bf41bec4179a8/old-ie.head.facia.css" media="only x" />
    <noscript>
        <link rel="stylesheet" type="text/css" href="https://assets.guim.co.uk/stylesheets/2dc5cd34723641950a3bf41bec4179a8/old-ie.head.facia.css" />
    </noscript>







    <link rel="stylesheet" type="text/css" href="https://assets.guim.co.uk/stylesheets/ea609b47a1568669995152dd82af95f6/old-ie.content.css" media="only x" />
    <noscript>
        <link rel="stylesheet" type="text/css" href="https://assets.guim.co.uk/stylesheets/ea609b47a1568669995152dd82af95f6/old-ie.content.css" />
    </noscript>


<![endif]-->
<!--[if (IE 9)&(!IEMobile)]>





    <link rel="stylesheet" type="text/css" href="https://assets.guim.co.uk/stylesheets/1e5802fe3009feca9965d975df0c21a9/ie9.content.css" media="only x" />
    <noscript>
        <link rel="stylesheet" type="text/css" href="https://assets.guim.co.uk/stylesheets/1e5802fe3009feca9965d975df0c21a9/ie9.content.css" />
    </noscript>







    <link rel="stylesheet" type="text/css" href="https://assets.guim.co.uk/stylesheets/515cfe95f0a2df56b352d296787250de/ie9.head.facia.css" media="only x" />
    <noscript>
        <link rel="stylesheet" type="text/css" href="https://assets.guim.co.uk/stylesheets/515cfe95f0a2df56b352d296787250de/ie9.head.facia.css" />
    </noscript>


<![endif]-->
<!--[if (gt IE 9)|(IEMobile)]><!-->
<style class="js-loggable">
    


    html{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body{margin:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block;vertical-align:baseline}audio:not([controls]){display:none;height:0}[hidden],template{display:none}a{background:transparent}a:active,a:hover{outline:0}abbr[title]{border-bottom:0.0625rem dotted}b,strong{font-weight:bold}dfn{font-style:italic}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sup{top:-.5em}sub{bottom:-.25em}img{border:0}svg:not(:root){overflow:hidden}figure{margin:1em 0}hr{-moz-box-sizing:content-box;-webkit-box-sizing:content-box;box-sizing:content-box;height:0}pre{overflow:auto}code,kbd,pre,samp{font-family:monospace, monospace;font-size:1em}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0;-webkit-font-smoothing:antialiased}button{overflow:visible}button,select{text-transform:none}.button{outline:0}button,html input[type='button'],input[type='reset'],input[type='submit']{-webkit-appearance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type='checkbox'],input[type='radio']{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding:0}input[type='number']::-webkit-inner-spin-button,input[type='number']::-webkit-outer-spin-button{height:auto}input[type='search']{-webkit-appearance:textfield;-moz-box-sizing:content-box;-webkit-box-sizing:content-box;box-sizing:content-box}input[type='search']::-webkit-search-cancel-button,input[type='search']::-webkit-search-decoration{-webkit-appearance:none}legend{border:0;padding:0}textarea{overflow:auto}optgroup{font-weight:bold}table{border-collapse:collapse;border-spacing:0}td,th{padding:0}html{overflow-y:scroll}html.iframed{overflow-y:auto}html.iframed--overflow-hidden{overflow:hidden}body{background-color:#ffffff}.is-modern .has-membership-access-requirement{visibility:hidden !important}::-moz-selection{background:rgba(75,198,223,0.4)}::selection{background:rgba(75,198,223,0.4)}head{font-family:'mobile'}@media (min-width: 30em){head{font-family:'mobileLandscape'}}@media (min-width: 46.25em){head{font-family:'tablet'}}@media (min-width: 61.25em){head{font-family:'desktop'}}@media (min-width: 71.25em){head{font-family:'leftCol'}}@media (min-width: 81.25em){head{font-family:'wide'}}body:after{border:0 !important;clip:rect(0 0 0 0) !important;height:0.0625rem !important;margin:-0.0625rem !important;overflow:hidden !important;padding:0 !important;position:absolute !important;width:0.0625rem !important;content:'mobile'}@media (min-width: 30em){body:after{content:'mobileLandscape'}}@media (min-width: 46.25em){body:after{content:'tablet'}}@media (min-width: 61.25em){body:after{content:'desktop'}}@media (min-width: 71.25em){body:after{content:'leftCol'}}@media (min-width: 81.25em){body:after{content:'wide'}}.dateline{font-size:0.8125rem;line-height:1.125rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;color:#767676}@media (min-width: 46.25em){.dateline{font-size:0.875rem;line-height:1.25rem}}.dateline i{vertical-align:baseline}.relative-timestamp{display:block;color:#767676;margin:0}.relative-timestamp span{display:inline-block}.relative-timestamp__icon{vertical-align:-0.125rem}ol,ul{list-style-position:inside}a,button,input[type='button'],input[type='submit']{-ms-touch-action:manipulation;touch-action:manipulation}html{font-family:"Guardian Text Egyptian Web",Georgia,serif;-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased}body{line-height:1.5;color:#333}html,body{text-rendering:optimizeSpeed}.should-kern body{text-rendering:optimizeLegibility;-webkit-font-feature-settings:'kern';-moz-font-feature-settings:'kern';font-feature-settings:'kern';-webkit-font-kerning:normal;font-kerning:normal;-webkit-font-variant-ligatures:common-ligatures;-moz-font-variant-ligatures:common-ligatures;font-variant-ligatures:common-ligatures}h1,h2,h3,h4,h5,h6{margin:0}blockquote{margin:0}p{margin-top:0;margin-bottom:0.5rem}h3{font-size:1rem;line-height:1.5rem;font-family:"Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;margin-bottom:0.4375rem}.type-5{font-size:1.125rem;line-height:1.5rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal}.control__icon-wrapper{width:1.875rem;height:1.875rem;border:0.0625rem solid #333;padding:0;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box;background-color:transparent}.control__icon-wrapper,.control__icon-wrapper:active,.control__icon-wrapper:focus,.control__icon-wrapper:hover{text-decoration:none;color:#333}.u-unstyled,.inline-list,.linkslist{margin:0;list-style:none}a,.u-fauxlink{color:#005689;cursor:pointer;text-decoration:none}a:hover,a:focus,.u-fauxlink:hover,.u-fauxlink:focus{text-decoration:underline}a:active,.u-fauxlink:active{color:#4bc6df;text-decoration:none}.u-h{border:0 !important;clip:rect(0 0 0 0) !important;height:0.0625rem !important;margin:-0.0625rem !important;overflow:hidden !important;padding:0 !important;position:absolute !important;width:0.0625rem !important}@media (max-width: 19.99em){.hide-until-mobile{display:none !important}}@media (max-width: 29.99em){.hide-until-mobile-landscape{display:none !important}}@media (max-width: 46.24em){.hide-until-tablet{display:none !important}}@media (max-width: 71.24em){.hide-until-leftcol{display:none !important}}@media (max-width: 81.24em){.hide-until-wide{display:none !important}}@media (max-width: 61.24em){.hide-until-desktop{display:none !important}}@media (min-width: 30em){.hide-from-mobile-landscape{display:none !important}}@media (min-width: 46.25em){.hide-from-tablet{display:none !important}}@media (min-width: 71.25em){.hide-from-leftcol{display:none !important}}@media (min-width: 81.25em){.hide-from-wide{display:none !important}}.is-hidden,[hidden]{display:none !important}@media (min-width: 46.25em){.mobile-only{display:none !important}}.hide-on-mobile{display:none !important}@media (min-width: 46.25em){.hide-on-mobile{display:block !important}}.hide-on-mobile-inline{display:none !important}@media (min-width: 46.25em){.hide-on-mobile-inline{display:inline !important}}@media (min-width: 20em) and (max-width: 61.24em){.hide-on-tablet{display:none !important}}@media (min-width: 61.25em){.hide-on-desktop{display:none !important}}.u-cf:after,.u-cf:before{content:'';display:table}.u-cf:after{clear:both}.u-baseline-top{margin-top:0.75rem}.skip:focus,.skip:active{font-size:80%;display:block;color:#00456e;text-decoration:none;position:static !important;width:100% !important;height:1.125rem !important;text-align:center}.u-responsive-ratio{width:100%;padding-bottom:60%;position:relative;overflow:hidden}.u-responsive-ratio img,.u-responsive-ratio object,.u-responsive-ratio embed,.u-responsive-ratio iframe,.u-responsive-ratio svg,.u-responsive-ratio video{width:100%;height:100%;position:absolute;top:0;left:0}.u-responsive-aligner{margin:0 auto;width:100%}.u-responsive-ratio--hd{padding-bottom:56.25%}.u-responsive-ratio--letterbox{padding-bottom:40%}.u-text-hyphenate{word-wrap:break-word;-webkit-hyphens:auto;-moz-hyphens:auto;-ms-hyphens:auto;hyphens:auto}.u-test-ellipsis{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.u-button-reset{display:block;margin:0;padding:0;border:0;width:100%;background:transparent}.u-button-reset:focus{outline:0}.u-underline{text-decoration:none !important;border-bottom:0.0625rem solid #dcdcdc;-webkit-transition:border-color .15s ease-out;transition:border-color .15s ease-out}.u-underline:hover,.u-underline:focus{border-color:#6e99b3}.u-underline:active{border-color:#4bc6df}.u-nobr{white-space:nowrap}.flushp{padding:0 !important}.flushp--top{padding-top:0 !important}.meta-button{background:transparent;border:0;margin:0;padding:0}.u-font-weight-normal{font-weight:normal}.u-vertical-align-middle-icon svg{vertical-align:middle}.u-faux-block-link{position:relative}.u-faux-block-link a,.u-faux-block-link abbr[title],.u-faux-block-link__promote{position:relative;z-index:1}.u-faux-block-link__overlay{top:0;right:0;bottom:0;left:0;overflow:hidden;text-indent:200%;white-space:nowrap;background:transparent}a.u-faux-block-link__overlay{position:absolute;z-index:0;opacity:0}a.u-faux-block-link__overlay:focus{outline:none}.u-faux-block-link--hover .u-faux-block-link__cta{text-decoration:underline}dt{font-weight:bold}menu,ol,ul{padding:0;margin-left:1.5625rem}nav ul,nav ol{list-style:none;list-style-image:none}.inline-list__item{display:inline-block}.inline-icon{fill:#ffffff}.inline-icon svg{overflow:visible}.inline-icon--light-grey{fill:#bdbdbd}.inline-close--small svg{height:100%;width:45%}.inline-tone-fill{fill:#005689}.tonal--tone-comment .inline-tone-fill{fill:#e6711b}.tonal--tone-feature .inline-tone-fill{fill:#951c55}.tonal--tone-review .inline-tone-fill{fill:#7d7569}.tonal--tone-editorial .inline-tone-fill{fill:#005689}.tonal--tone-analysis .inline-tone-fill{fill:#4bc6df}.tonal--tone-live .inline-tone-fill,.tonal--tone-dead .inline-tone-fill{fill:#b51800}.tonal--tone-media .inline-tone-fill{fill:#fb0}.tonal--tone-special-report .inline-tone-fill{fill:#4bc6df}.inline-icon__fallback{display:none}.inline-icon__fallback{display:none !important}.no-svg .inline-icon{display:none !important}.no-svg .inline-icon__fallback{display:block !important}.gs-container{position:relative;margin:0 auto}@media (min-width: 46.25em){.gs-container{max-width:46.25rem}}@media (min-width: 61.25em){.gs-container{max-width:61.25rem}}@media (min-width: 71.25em){.gs-container{max-width:71.25rem}}@media (min-width: 81.25em){.gs-container{max-width:81.25rem}}.l-header{display:none;position:relative;z-index:1000}@media (min-width: 81.25em){.has-page-skin .l-header .gs-container{width:61.25rem}}@media (min-width: 46.25em){.l-header{display:none}}@media (min-width: 46.25em) and (min-width: 61.25em){.l-header{display:block}}@media (min-width: 61.25em){.l-header{display:block}}.l-header--is-slim{background:#005689}.l-header--is-slim .l-header__inner:after,.l-header--is-slim .l-header__inner:before{content:'';display:table}.l-header--is-slim .l-header__inner:after{clear:both}.l-header--is-slim.l-header--is-slim-ab{background:#005689}.l-header--is-slim .hide-on-slim-header{display:none !important}.l-header--is-slim .show-on-slim-header{display:block !important}.l-header--animate{-webkit-transition:margin-top 1s cubic-bezier(0, 0, 0, 0.985);transition:margin-top 1s cubic-bezier(0, 0, 0, 0.985)}.logo-wrapper{position:relative;float:right;margin:0.1875rem 0.625rem 0.75rem 0}.logo-wrapper svg{width:10rem;height:1.875rem}.logo-wrapper .logo-tagline{height:0}.logo-wrapper .logo-tagline__link{font-size:0.75rem;line-height:1rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;position:absolute;top:3rem;right:0.125rem;color:#aad8f1;font-weight:bold}@media (min-width: 46.25em){.logo-wrapper{margin-top:-0.375rem;margin-bottom:0.375rem}.logo-wrapper svg{width:22.5rem;height:4.25rem}}.l-header--is-slim .logo-wrapper{margin-top:0.5625rem;margin-bottom:0;float:left}@media (min-width: 46.25em){.l-header--is-slim .logo-wrapper svg{width:10rem;height:1.875rem}}.no-svg .l-header--is-slim .logo-wrapper .inline-logo{width:10rem;height:1.875rem}.logo-wrapper .inline-logo{display:block}.no-svg .logo-wrapper .inline-logo{width:10rem;height:1.875rem}@media (min-width: 46.25em){.no-svg .logo-wrapper .inline-logo{width:20rem;height:3.75rem}}.l-header-pre,.l-header--is-slim .l-header-pre{float:left}.l-header-pre{min-width:8.75rem;z-index:1020;position:relative}@media (min-width: 46.25em){.l-header-pre{float:none}}.l-header-main{position:relative;z-index:2}.l-header--is-slim .l-header-main{float:right}@media (max-width: 46.24em){.weather{padding-top:0.0625rem}.fc-container--first .fc-container__inner,.index-page-header{padding-top:0.5625rem}.content__labels{padding:0.5625rem 0}}@media (max-width: 29.99em){.content__head:not(.tonal__head--tone-dead):not(.tonal__head--tone-live):not(.tonal__head--tone-media):not(.content__head--crossword):not(.content__head--interactive){margin-right:-0.625rem;margin-left:-0.625rem}}@media (min-width: 30em) and (max-width: 41.24em){.content__head:not(.tonal__head--tone-dead):not(.tonal__head--tone-live):not(.tonal__head--tone-media):not(.content__head--crossword):not(.content__head--interactive){margin-right:-1.25rem;margin-left:-1.25rem}}@media (min-width: 41.25em) and (max-width: 46.24em){.media-primary,.content__head{margin-left:-1.25rem;margin-right:-1.25rem}}.header-cta-item{color:#aad8f1;float:left;position:relative}.header-cta-item:hover,.header-cta-item:focus{color:#ffffff;text-decoration:none;outline:none}.header-cta-item__label{display:inline-block;font-family:'Guardian Egyptian Web', 'Guardian Text Egyptian Web', Georgia, serif;font-size:0.8125rem;font-weight:700;line-height:1;padding:0.75rem 0.625rem;position:relative}@media (min-width: 22.5em){.header-cta-item__label{font-size:0.875rem}}@media (min-width: 46.25em){.header-cta-item__label{font-size:1.0625rem;padding-top:0.875rem}}@media (max-width: 61.24em){.header-cta-item__new-line{display:block}}.header-cta-item--primary{color:#00456e}.is-paying-member .header-cta-item--primary,.is-recent-contributor .header-cta-item--primary{display:none}.header-cta-item--primary:before{border-top:3rem solid #4bc6df;border-left:0.3125rem solid transparent;border-right:1.25rem solid transparent;content:'';left:0;position:absolute;right:-0.625rem;top:-0.375rem;-webkit-transform:rotate(-3deg);transform:rotate(-3deg)}@media (min-width: 22.5em){.header-cta-item--primary:before{border-top-width:3.375rem}}@media (min-width: 46.25em) and (max-width: 61.24em){.header-cta-item--primary:before{border-top-width:4.125rem}}.header-cta-item--primary:hover,.header-cta-item--primary:focus{color:#00456e}.header-cta-item--primary:hover:before,.header-cta-item--primary:focus:before{border-top-color:#25b5d2}.header-cta-item--secondary:not(:last-child) .header-cta-item__label{padding-right:0}.header-cta-item--secondary:not(:last-child) .header-cta-item__label:after{color:#4bc6df;content:'/';display:inline-block;pointer-events:none;margin-right:-0.375rem}.menu{background-color:#00456e;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;color:#ffffff;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;font-size:1.25rem;left:0;line-height:1;margin-right:3.125rem;padding-bottom:1.5rem;top:0;z-index:1070}@media (max-width: 61.24em){.menu{-webkit-transform:translateX(-110%);transform:translateX(-110%);-webkit-transition:-webkit-transform 0.4s cubic-bezier(0.23, 1, 0.32, 1);transition:-webkit-transform 0.4s cubic-bezier(0.23, 1, 0.32, 1);transition:transform 0.4s cubic-bezier(0.23, 1, 0.32, 1);transition:transform 0.4s cubic-bezier(0.23, 1, 0.32, 1), -webkit-transform 0.4s cubic-bezier(0.23, 1, 0.32, 1);-webkit-overflow-scrolling:touch;-webkit-box-shadow:0.1875rem 0 1rem rgba(0,0,0,0.4);box-shadow:0.1875rem 0 1rem rgba(0,0,0,0.4);bottom:0;height:100%;overflow:auto;padding-top:0.375rem;position:fixed;right:0;-webkit-transition:-webkit-transform 0.2s cubic-bezier(0.23, 1, 0.32, 1);transition:-webkit-transform 0.2s cubic-bezier(0.23, 1, 0.32, 1);transition:transform 0.2s cubic-bezier(0.23, 1, 0.32, 1);transition:transform 0.2s cubic-bezier(0.23, 1, 0.32, 1), -webkit-transform 0.2s cubic-bezier(0.23, 1, 0.32, 1);will-change:transform}}@media (min-width: 22.5em){.menu{margin-right:4rem}}@media (min-width: 30em){.menu{margin-right:5.125rem}}@media (min-width: 46.25em){.menu{margin-right:6.375rem}}@media (min-width: 61.25em){.menu{display:none;left:50%;margin-left:-50vw;margin-right:-50vw;padding-bottom:0;padding-top:0;position:absolute;right:50%;top:100%;width:100vw}}@media (max-width: 61.24em){.new-header--open .menu{-webkit-transform:translateX(0%);transform:translateX(0%);-webkit-transition:-webkit-transform 0.4s cubic-bezier(0.23, 1, 0.32, 1);transition:-webkit-transform 0.4s cubic-bezier(0.23, 1, 0.32, 1);transition:transform 0.4s cubic-bezier(0.23, 1, 0.32, 1);transition:transform 0.4s cubic-bezier(0.23, 1, 0.32, 1), -webkit-transform 0.4s cubic-bezier(0.23, 1, 0.32, 1)}}@media (min-width: 61.25em){.new-header--open .menu{display:block}}.new-header--slim.new-header--open .menu{margin-right:2.3125rem}@media (min-width: 30em){.new-header--slim.new-header--open .menu{margin-right:2.9375rem}}x:-o-prefocus .menu{display:none}.menu__inner{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}@media (max-width: 61.24em){.menu__inner.gs-container{max-width:none}}@media (min-width: 61.25em){.menu__inner{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;padding-left:1.25rem;padding-right:1.25rem}}.menu__overlay{background-color:rgba(0,0,0,0.5);height:100%;left:0;opacity:0;position:fixed;top:0;-webkit-transition:opacity 0.2s cubic-bezier(0.23, 1, 0.32, 1);transition:opacity 0.2s cubic-bezier(0.23, 1, 0.32, 1);width:0;z-index:1069}.new-header--open .menu__overlay{opacity:1;width:100%}@media (min-width: 61.25em){.menu__overlay{display:none}}.menu-brand-extensions{background-color:#4bc6df;color:#00456e}.menu-brand-extensions__inner{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding:0.5rem 1.25rem}.menu-brand-extensions__list{display:inline-block;list-style:none;margin:0;padding:0;vertical-align:middle}.menu-brand-extensions__list-item{display:inline-block}.menu-brand-extensions__list-item+.menu-brand-extensions__list-item:before{color:currentColor;content:'/';display:inline-block;font-size:1.375rem;opacity:.6;margin-left:-0.125rem;margin-right:-0.125rem;pointer-events:none}.menu-brand-extensions__logo{display:inline-block;margin-right:0.41667rem;position:relative;top:0.125rem;vertical-align:middle}.menu-brand-extensions__logo__svg{height:1.75rem;width:8.75rem}.menu-brand-extensions__logo__svg path{fill:currentColor}.menu-brand-extensions-item{color:currentColor;font-size:1.5rem}.menu-brand-extensions-item:focus{color:currentColor;outline:none;text-decoration:underline}.menu-group{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;color:#ffffff;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;font-size:1.125rem;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;list-style:none;margin:0;padding:0 0 0.75rem}@media (min-width: 61.25em){.menu-group{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;padding-bottom:0}}@media (max-width: 61.24em){[aria-expanded='false'] ~ .menu-group{display:none}}.menu-group--primary{color:#aad8f1;padding-top:0}.menu-group--primary:after,.menu-group--primary:before{content:'';display:table}.menu-group--primary:after{clear:both}@media (min-width: 61.25em){.menu-group--primary{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-flex-wrap:nowrap;-ms-flex-wrap:nowrap;flex-wrap:nowrap;-webkit-box-ordinal-group:2;-webkit-order:1;-ms-flex-order:1;order:1}}.menu-group--secondary{background-color:#00385a;margin-top:0;padding-top:0}@media (min-width: 61.25em){.menu-group--secondary{background-color:transparent;padding-bottom:0;width:100%}}@media (max-width: 61.24em){.menu-group--membership,.menu-group--editions{color:#00456e;background-color:#4bc6df}}.menu-group--membership{padding-bottom:0;position:relative}@media (min-width: 61.25em) and (max-width: 71.24em){.menu-group--membership{border-top:0.0625rem solid #005689;-webkit-flex-wrap:nowrap;-ms-flex-wrap:nowrap;flex-wrap:nowrap;width:100%}}@media (min-width: 61.25em){.menu-group--membership{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-box-ordinal-group:4;-webkit-order:3;-ms-flex-order:3;order:3;padding-bottom:0;padding-top:0.75rem;width:100%}}@media (min-width: 71.25em){.menu-group--membership{border-left:0.125rem solid #005689;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;margin-left:0;padding-left:0.5625rem;width:9.25rem;position:absolute;right:0;top:0}@supports (display: flex){.menu-group--membership{position:relative;right:auto;top:auto}}}@media (min-width: 81.25em){.menu-group--membership{width:14.25rem}.has-page-skin .menu-group--membership{border-top:0.0625rem solid #005689;border-left-width:0;-webkit-flex-wrap:nowrap;-ms-flex-wrap:nowrap;flex-wrap:nowrap;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;width:100%;padding-left:0}}.menu-group--editions{padding-bottom:0}@media (min-width: 61.25em){.menu-group--editions{padding-bottom:1.5rem;margin-top:1.5rem;-webkit-box-ordinal-group:6;-webkit-order:5;-ms-flex-order:5;order:5}@supports (display: flex){.menu-group--editions{padding-bottom:0}}}@media (max-width: 61.24em){.menu-group--editions .menu-group{color:#00456e;background-color:#25b5d2}}@media (min-width: 61.25em){.menu-group--editions .menu-group{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-flex-wrap:nowrap;-ms-flex-wrap:nowrap;flex-wrap:nowrap}}@media (min-width: 61.25em){.menu-group--editions .menu-group .menu-item{display:inline-block;width:auto}}@media (max-width: 61.24em){.menu-group--membership-actions{background-color:#25b5d2;color:#00456e}}@media (min-width: 61.25em){.menu-group--membership-actions{color:#ffffff;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap}}@media (min-width: 61.25em){.menu-group--footer{color:#aad8f1;position:absolute;right:1.25rem;top:0;width:8.75rem}@supports (display: flex){.menu-group--footer{-webkit-box-ordinal-group:3;-webkit-order:2;-ms-flex-order:2;order:2;position:relative;right:auto;top:auto}}}@media (min-width: 71.25em){.menu-group--footer{margin-right:0.625rem;right:10.625rem}@supports (display: flex){.menu-group--footer{right:auto}}}@media (min-width: 81.25em){.menu-group--footer{margin-right:5.625rem}.has-page-skin .menu-group--footer{margin-right:0}}@media (min-width: 61.25em){.menu-group--search{margin-right:1.25rem;-webkit-box-ordinal-group:5;-webkit-order:4;-ms-flex-order:4;order:4;width:38.75rem}}.menu-item{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;overflow:hidden;position:relative;width:100%}@media (min-width: 61.25em){.menu-group--primary>.menu-item{float:left;margin-right:1.25rem;width:8.75rem}@supports (display: flex){.menu-group--primary>.menu-item{float:none}}}@media (min-width: 61.25em){.menu-group--secondary>.menu-item,.menu-group--footer>.menu-item{border-top:0.0625rem solid #005689;width:8.4375rem}}@media (min-width: 61.25em){.menu-group--secondary>.menu-item:nth-child(2),.menu-item.menu-item--no-border{border:transparent;margin-top:0.1875rem}}@media (min-width: 61.25em){.menu-group--editions>.menu-item{width:100%}}@media (min-width: 61.25em){.menu-group--editions>.menu-item{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex}}@media (min-width: 61.25em) and (max-width: 71.24em){.menu-group--membership-actions .menu-item{margin-left:0.625rem;width:9.375rem}}@media (min-width: 81.25em){.has-page-skin .menu-group--membership-actions .menu-item{margin-left:0.625rem;width:9.375rem}}@media (min-width: 61.25em){.menu-item--home{display:none}}@media (min-width: 61.25em) and (max-width: 71.24em){.menu-item--user-detail{width:19.375rem}}@media (min-width: 71.25em){.menu-item--user-detail{width:100%}}@media (min-width: 81.25em){.has-page-skin .menu-item--user-detail{width:19.375rem}}@media (min-width: 61.25em) and (max-width: 71.24em){.menu-item--membership{width:30rem}}@media (min-width: 71.25em){.menu-item--membership{width:100%}}@media (min-width: 81.25em){.has-page-skin .menu-item--membership{width:30rem}}.menu-item__title{background-color:transparent;border:0;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;color:currentColor;cursor:pointer;display:block;font-size:1.25rem;outline:none;padding:0.5rem 2.3125rem 0.5rem 3.125rem;position:relative;text-align:left;text-transform:lowercase;width:100%}@media (min-width: 46.25em){.menu-item__title{padding-left:3.75rem}}@media (min-width: 61.25em){.menu-item__title{font-size:1rem;letter-spacing:0.01875rem;line-height:1.125rem;padding-bottom:0.5625rem;padding-left:0;padding-right:0;padding-top:0.1875rem}}.menu-item__title:hover,.menu-item__title:focus{text-decoration:none}@media (min-width: 61.25em){.menu-item__title:hover,.menu-item__title:focus{color:#00d4ff}}@media (min-width: 61.25em){.menu-item__title:focus{text-decoration:underline}}.menu-item__title>*{pointer-events:none}@media (max-width: 61.24em){.menu-group--primary>*:not(:last-child)>.menu-item__title:not([aria-expanded='true']):after,.menu-item__title[data-link-name='nav2 : the guardian app']:not([aria-expanded='true']):after,.menu-item__title[data-link-name='nav2 : facebook']:not([aria-expanded='true']):after{background-color:#00385a;bottom:0;content:'';display:block;height:0.0625rem;left:3.125rem;position:absolute;width:100%}}@media (max-width: 61.24em) and (min-width: 46.25em){.menu-group--primary>*:not(:last-child)>.menu-item__title:not([aria-expanded='true']):after,.menu-item__title[data-link-name='nav2 : the guardian app']:not([aria-expanded='true']):after,.menu-item__title[data-link-name='nav2 : facebook']:not([aria-expanded='true']):after{left:3.75rem}}@media (max-width: 61.24em){.menu-item__title[data-link-name='nav2 : the guardian app'],.menu-item__title[data-link-name='nav2 : facebook']{margin-top:1.5rem}.menu-item__title[data-link-name='nav2 : the guardian app']:after,.menu-item__title[data-link-name='nav2 : facebook']:after{bottom:auto;top:0}}.menu-group--primary>.menu-item>.menu-item__title{font-size:1.5rem;padding-bottom:1rem;padding-top:0.375rem}@media (min-width: 61.25em){.menu-group--primary>.menu-item>.menu-item__title{font-size:2rem}}.menu-group--editions .menu-item__title[aria-haspopup='true']{margin-bottom:0.75rem}.menu-group--editions .menu-item__title[aria-haspopup='true'][aria-expanded='true']{margin-bottom:0}@media (min-width: 61.25em){.menu-group--membership .menu-item__title{color:#ffffff}.menu-group--membership .menu-item__title:hover,.menu-group--membership .menu-item__title:focus{color:#00d4ff}}@media (min-width: 61.25em){.menu-group--editions .menu-item__title{background-color:#005689;color:#aad8f1;display:block;font-size:0.9375rem;height:2.625rem;-webkit-border-radius:50%;border-radius:50%;line-height:2.625rem;margin-right:0.3125rem;padding:0;text-align:center;width:2.625rem}}@media (min-width: 61.25em){.menu-group--editions .menu-item__title:hover,.menu-group--editions .menu-item__title:focus{background-color:#00639d;color:#ffffff}}@media (min-width: 61.25em){.menu-item--edition-active .menu-item__title,.menu-item--edition-active .menu-item__title:hover,.menu-item--edition-active .menu-item__title:focus{background-color:#aad8f1;color:#00456e}}.menu-item__icon,.menu-item__toggle{color:#197caa;left:1.5625rem;position:absolute}@media (min-width: 46.25em){.menu-item__icon,.menu-item__toggle{left:2.1875rem}}@media (min-width: 61.25em){.menu-item__icon,.menu-item__toggle{display:none}}.menu-item__toggle{margin-top:-0.25rem}[aria-expanded='true']>.menu-item__toggle{margin-top:0.125rem}.menu-item__toggle:before{border:0.125rem solid currentColor;border-top:0;border-left:0;content:'';display:inline-block;height:0.5rem;-webkit-transform:rotate(45deg);transform:rotate(45deg);width:0.5rem}[aria-expanded='true']>.menu-item__toggle:before{-webkit-transform:rotate(-135deg);transform:rotate(-135deg)}.menu-item__icon{margin-left:-0.1875rem}.menu-item__icon .inline-icon__svg{fill:currentColor}.menu-item__icon .inline-home__svg{height:1rem;width:1rem}.menu-item__icon .inline-share-facebook__svg,.menu-item__icon .inline-share-twitter__svg{margin-left:-0.375rem;margin-top:-0.3125rem}.menu-item__editions-label{color:#ffffff;font-size:1rem;line-height:2.625rem;margin-right:0.625rem}.menu-search{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;display:block;margin-left:0.8125rem;max-width:23.75rem;position:relative;width:100%}@media (max-width: 61.24em){.menu-search{margin-bottom:1.5rem;margin-right:2.9375rem}}@media (min-width: 46.25em){.menu-search{margin-left:1.375rem}}@media (min-width: 61.25em){.menu-search{margin-bottom:1.5rem;margin-left:0;margin-top:1.5rem;max-width:none;padding-right:0}}.menu-search__search-box{background-color:#005689;border:0;-webkit-border-radius:62.5rem;border-radius:62.5rem;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;font-size:1.25rem;height:2.25rem;padding-left:2.375rem;vertical-align:middle;width:100%}@media (min-width: 61.25em){.menu-search__search-box{height:2.625rem;padding-left:3rem;font-size:1.5rem}.menu-search__search-box:hover{background:#00639d}}.menu-search__search-box::-webkit-input-placeholder{color:#aad8f1}.menu-search__search-box::-moz-placeholder{color:#aad8f1}.menu-search__search-box:-ms-input-placeholder{color:#aad8f1}.menu-search__search-box::placeholder{color:#aad8f1}.menu-search__search-box:focus{background-color:#ffffff;color:#333;outline:none;padding-right:2.5rem;-webkit-transition:background-color 500ms;transition:background-color 500ms}.menu-search__search-box:focus::-webkit-input-placeholder{color:#bdbdbd}.menu-search__search-box:focus::-moz-placeholder{color:#bdbdbd}.menu-search__search-box:focus:-ms-input-placeholder{color:#bdbdbd}.menu-search__search-box:focus::placeholder{color:#bdbdbd}.menu-search__glass{position:absolute;left:0.625rem;top:0.4375rem}@media (min-width: 61.25em){.menu-search__glass{left:0.75rem;top:0.625rem}}.menu-search__glass .inline-search-36__svg{fill:#4bc6df;height:1.375rem;width:1.375rem}.menu-search__search-box:focus ~ .menu-search__glass .inline-search-36__svg{fill:#767676}.menu-search__submit{background:transparent;border:0;bottom:0;cursor:pointer;display:block;opacity:0;pointer-events:none;position:absolute;right:0;top:0;width:3.125rem}.menu-search__submit:before,.menu-search__submit:after{border:0.125rem solid #005689;border-left:0;border-top:0;content:'';display:block;position:absolute;right:0.875rem}@media (min-width: 61.25em){.menu-search__submit:before,.menu-search__submit:after{right:1rem}}.menu-search__submit:before{height:0.75rem;top:0.6875rem;-webkit-transform:rotate(-45deg);transform:rotate(-45deg);width:0.75rem}@media (min-width: 61.25em){.menu-search__submit:before{top:0.875rem}}.menu-search__submit:after{border-right:0;top:1.0625rem;width:1.25rem}@media (min-width: 61.25em){.menu-search__submit:after{top:1.25rem}}.menu-search__submit:hover,.menu-search__submit:active{border-color:#005689}.menu-search__submit:focus:before,.menu-search__submit:focus:after{border-color:#ffffff}.menu-search__search-box:focus ~ .menu-search__submit,.menu-search__submit:focus,.menu-search__submit:active{opacity:1;outline:none;pointer-events:all}.menu-user{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;padding-top:0.25rem}@media (min-width: 71.25em){.menu-user{-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;margin-bottom:0.25rem}}@media (min-width: 81.25em){.has-page-skin .menu-user{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;margin-bottom:0}}.menu-user__avatar{-webkit-border-radius:50%;border-radius:50%}.menu-user__avatar-fallback{font-size:0}.menu-user__avatar-fallback__svg{opacity:.6}.menu-user__avatar-fallback__svg,.menu-user__avatar{height:3.75rem;margin-bottom:0.25rem;margin-right:1.25rem;width:3.75rem}.menu-user__name{font-size:1.5rem;text-transform:none}@media (max-width: 61.24em){.nav-is-open{overflow:hidden;width:100%}}@media (min-width: 61.25em){.nav-is-open{overflow-x:hidden}}.new-header{background-color:#005689;position:relative}@media (min-width: 46.25em){.new-header{display:block}}@media (min-width: 46.25em) and (min-width: 61.25em){.new-header{display:none}}@media (min-width: 61.25em){.new-header.new-header--mvt-desktop{display:block}}@media (min-width: 81.25em){.has-page-skin .new-header .gs-container{width:61.25rem}}.new-header__inner:after,.new-header__inner:before{content:'';display:table}.new-header__inner:after{clear:both}@supports (display: flex){.new-header__inner{-webkit-box-align:start;-webkit-align-items:flex-start;-ms-flex-align:start;align-items:flex-start;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;padding-bottom:0}}.new-header__cta-container{left:0.0625rem;overflow:hidden;padding-bottom:0.625rem;padding-left:0.25rem;padding-right:0.375rem;position:absolute;top:0}@media (min-width: 30em){.new-header__cta-container{left:0.375rem}}.new-header__logo{display:block;float:right}@supports (display: flex){.new-header__logo{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;float:none;margin-left:auto}}@media (min-width: 61.25em){.new-header__logo:focus{outline:none}}@media (min-width: 61.25em) and (max-width: 71.24em){.new-header--slim.new-header--open .new-header__logo{display:none}}.new-header__logo__svg{display:block;height:-webkit-calc(3 / 16 * 10.625rem);height:calc(3 / 16 * 10.625rem);margin-bottom:0.375rem;margin-right:0.625rem;margin-top:0.375rem;width:10.625rem}@media (min-width: 22.5em){.new-header__logo__svg{height:-webkit-calc(3 / 16 * 14.0625rem);height:calc(3 / 16 * 14.0625rem);width:14.0625rem}}@media (min-width: 30em){.new-header__logo__svg{height:-webkit-calc(3 / 16 * 16.25rem);height:calc(3 / 16 * 16.25rem);margin-bottom:0;margin-right:1.25rem;width:16.25rem}}@media (min-width: 46.25em){.new-header__logo__svg{height:-webkit-calc(3 / 16 * 21.5625rem);height:calc(3 / 16 * 21.5625rem);margin-bottom:-0.3125rem;width:21.5625rem}}@media (min-width: 71.25em){.new-header__logo__svg{height:-webkit-calc(3 / 16 * 24.0625rem);height:calc(3 / 16 * 24.0625rem);margin-bottom:-0.0625rem;width:24.0625rem}}.new-header--slim .new-header__logo__svg{height:-webkit-calc(3 / 16 * 9.6875rem);height:calc(3 / 16 * 9.6875rem);margin-right:1.25rem;margin-top:0.4375rem;width:9.6875rem}@media (min-width: 30em){.new-header--slim .new-header__logo__svg{margin-right:1.875rem}}@media (min-width: 46.25em){.new-header--slim .new-header__logo__svg{height:-webkit-calc(3 / 16 * 10.625rem);height:calc(3 / 16 * 10.625rem);margin-top:0.3125rem;width:10.625rem}}x:-o-prefocus,.new-header__cta-container{display:none}.pillars{clear:right;color:#aad8f1;font-size:0;list-style:none;margin:0;padding:0 0.625rem;width:100%}@media (min-width: 30em){.pillars{padding-left:1.25rem;padding-right:1.25rem}}@media (min-width: 61.25em){.new-header--open .pillars{z-index:1070}}.new-header--slim .pillars{width:auto;-webkit-box-ordinal-group:0;-webkit-order:-1;-ms-flex-order:-1;order:-1}@media (max-width: 46.24em){.new-header--slim .pillars{display:none}}.pillars__item{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;display:inline-block}@media (min-width: 61.25em){.pillars__item{min-width:0;padding-right:1.25rem;-webkit-transition:min-width 200ms ease;transition:min-width 200ms ease;will-change:min-width}.new-header--open .pillars__item{min-width:9.375rem}.new-header--open .pillars__item:not(:first-child){margin-left:0.625rem}}.pillars__item>*:after{content:'/';color:#4bc6df;display:inline-block;margin-left:-0.0625rem;margin-right:0.125rem;pointer-events:none}@media (min-width: 61.25em){.pillars__item>*:after{left:-0.83333rem;margin:0;position:absolute;top:0}}@media (max-width: 61.24em){.pillars__item:last-child>*:after{display:none}}@media (min-width: 61.25em){.pillars__item:first-child>*:after{display:none}}.pillar-link{font-size:1rem;line-height:1.375rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;color:currentColor;cursor:pointer;display:block;font-size:16px;font-size:4.9vw;line-height:1.875rem;position:relative;-webkit-transition:color 350ms;transition:color 350ms}@media (min-width: 22.5em){.pillar-link{line-height:2.25rem}}@media (min-width: 30em){.pillar-link{font-size:1.5rem;line-height:2.625rem}}@media (min-width: 46.25em){.pillar-link{font-size:1.75rem;letter-spacing:-.04rem}}@media (min-width: 61.25em){.pillar-link{font-size:2rem}}.pillar-link:focus,.pillar-link:hover{color:#ffffff;outline:none;text-decoration:none}@media (min-width: 46.25em){.new-header--slim .pillar-link{font-size:1.5rem}}.pillar-link--current-section{color:#ffffff}@media (min-width: 61.25em){.new-header--open .pillar-link--current-section{color:#aad8f1}.new-header--open .pillar-link--current-section:focus,.new-header--open .pillar-link--current-section:hover{color:#ffffff;text-decoration:none}}.pillar-link--current-section:before{content:'';position:absolute;left:50%;bottom:0;-webkit-transform:translateX(-100%);transform:translateX(-100%);border-bottom:0.375rem solid #5c6268;border-left:0.375rem solid transparent;border-right:0.375rem solid transparent}@media (min-width: 61.25em){.new-header--open .pillar-link--current-section:before{display:none}}.subnav{background-color:#5c6268;color:#dcdcdc;max-height:2.55rem;overflow:hidden;padding:0.25rem 0.625rem}@media (min-width: 20em){.subnav{max-height:2.625rem;max-height:13vw}}@media (min-width: 30em){.subnav{padding:0.375rem 0}}@media (min-width: 61.25em){.subnav{max-height:1.5rem}}.subnav:before{content:'';float:right;width:3.8125rem;height:0.0625rem}@media (min-width: 22.5em){.subnav:before{width:5.0625rem}}@media (min-width: 30em){.subnav:before{width:6.1875rem}}.subnav__list{line-height:1;list-style:none;margin:0;padding:0}@media (min-width: 30em){.subnav__list{padding-left:1.25rem;padding-right:1.25rem}}@media (min-width: 61.25em){.subnav__list{padding-right:11.25rem}}.subnav__item{display:inline-block}.subnav__item:focus,.subnav__item:hover{color:#ffffff}@media (max-width: 46.24em){.subnav__item>*:after{content:'/';color:rgba(255,255,255,0.3);display:inline-block;font-size:1em;pointer-events:none;margin-left:-0.125rem;margin-right:-0.125rem}.subnav__item:last-child>*:after{content:''}}@media (min-width: 46.25em){.subnav__item>*:before{content:'/';color:rgba(255,255,255,0.3);display:inline-block;font-size:1em;pointer-events:none;margin-left:-0.125rem;margin-right:-0.125rem}.subnav__item:first-child>*:before{content:''}}.subnav-link{font-size:1rem;line-height:1.375rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;color:currentColor;display:inline-block;font-size:16px;font-size:4.9vw;line-height:1.3em}@media (min-width: 30em){.subnav-link{font-size:1.1875rem;max-height:3.6rem}}@media (min-width: 61.25em){.subnav-link{margin-bottom:0.75rem}}.subnav-link:hover,.subnav-link:focus{text-decoration:none}.subnav-link--toggle-more{background:transparent;border:0;color:#bdbdbd;padding:0}.subnav-link--current-section{color:#ffffff}.veggie-burger{background-color:#4bc6df;bottom:-0.375rem;-webkit-box-shadow:0 0 0 0.0625rem rgba(0,0,0,0.08);box-shadow:0 0 0 0.0625rem rgba(0,0,0,0.08);color:#ffffff;cursor:pointer;height:2.625rem;min-width:2.625rem;position:absolute;border:0;-webkit-border-radius:50%;border-radius:50%;outline:none;right:1.8125rem;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;z-index:1}@media (min-width: 22.5em){.veggie-burger{height:3.375rem;width:3.375rem;right:2.3125rem}}@media (min-width: 30em){.veggie-burger{right:3.4375rem}}@media (min-width: 46.25em){.veggie-burger{right:4.6875rem}}@media (min-width: 71.25em){.veggie-burger{height:3.75rem;right:5rem;width:3.75rem}}.new-header--open .veggie-burger{z-index:1071}@media (max-width: 61.24em){.new-header--open .veggie-burger:before{-webkit-border-radius:5.25rem 0 0 5.25rem;border-radius:5.25rem 0 0 5.25rem;content:'';height:5.25rem;position:absolute;right:1.3125rem;top:-1.3125rem;width:2.625rem}}@media (max-width: 61.24em) and (min-width: 22.5em){.new-header--open .veggie-burger:before{height:6.75rem;width:3.375rem;top:-1.6875rem;right:1.6875rem;-webkit-border-radius:6.75rem 0 0 6.75rem;border-radius:6.75rem 0 0 6.75rem}}x:-o-prefocus .veggie-burger{display:none}.new-header--slim .veggie-burger{height:3.375rem;margin-bottom:-0.75rem;position:relative;right:0.625rem;top:-0.375rem;width:3.375rem}@media (min-width: 30em){.new-header--slim .veggie-burger{right:1.25rem}}.veggie-burger__label{font-size:1rem;line-height:1.375rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;bottom:-1.375rem;color:#ffffff;font-size:1.125rem;left:50%;position:absolute;text-align:center;text-transform:lowercase;-webkit-transform:translateX(-50%);transform:translateX(-50%);width:8.75rem}@media (max-width: 61.24em){.veggie-burger__label{border:0 !important;clip:rect(0 0 0 0) !important;height:0.0625rem !important;margin:-0.0625rem !important;overflow:hidden !important;padding:0 !important;position:absolute !important;width:0.0625rem !important}}.new-header--open .veggie-burger__label{display:none}.veggie-burger__icon{top:50%;display:block;margin-top:-0.0625rem;left:0;right:0;margin-left:auto;margin-right:auto}.veggie-burger__icon,.veggie-burger__icon:before,.veggie-burger__icon:after{background-color:currentColor;content:'';height:0.125rem;left:0;position:absolute;width:1.25rem}@media (min-width: 22.5em){.veggie-burger__icon,.veggie-burger__icon:before,.veggie-burger__icon:after{height:0.1875rem;width:1.625rem}}@media (min-width: 71.25em){.veggie-burger__icon,.veggie-burger__icon:before,.veggie-burger__icon:after{height:0.25rem;width:1.875rem}}.veggie-burger__icon:before{top:-0.3125rem}@media (min-width: 22.5em){.veggie-burger__icon:before{top:-0.4375rem}}@media (min-width: 71.25em){.veggie-burger__icon:before{top:-0.5rem}}.veggie-burger__icon:after{bottom:-0.3125rem}@media (min-width: 22.5em){.veggie-burger__icon:after{bottom:-0.4375rem}}@media (min-width: 71.25em){.veggie-burger__icon:after{bottom:-0.5rem}}.new-header--open .veggie-burger__icon{background-color:transparent}.new-header--open .veggie-burger__icon:before{top:0;-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}.new-header--open .veggie-burger__icon:after{bottom:0;-webkit-transform:rotate(45deg);transform:rotate(45deg)}@media (max-width: 61.24em){.veggie-burger-fallback:checked ~ .menu{-webkit-transform:translateX(0%);transform:translateX(0%);-webkit-transition:-webkit-transform 0.4s cubic-bezier(0.23, 1, 0.32, 1);transition:-webkit-transform 0.4s cubic-bezier(0.23, 1, 0.32, 1);transition:transform 0.4s cubic-bezier(0.23, 1, 0.32, 1);transition:transform 0.4s cubic-bezier(0.23, 1, 0.32, 1), -webkit-transform 0.4s cubic-bezier(0.23, 1, 0.32, 1)}}@media (min-width: 61.25em){.veggie-burger-fallback:checked ~ .menu{display:block}}@media (max-width: 61.24em){.veggie-burger-fallback:checked ~ .menu__overlay{opacity:1;width:100%}}@media (min-width: 61.25em){.veggie-burger-fallback:checked ~ .pillars .pillars__item{min-width:9.375rem}}@media (min-width: 61.25em){.veggie-burger-fallback:checked ~ .pillars .pillars__item:not(:first-child){margin-left:0.625rem}}@media (min-width: 61.25em){.veggie-burger-fallback:checked ~ .pillars .pillar-link--current-section:before{display:none}}.veggie-burger-fallback:checked ~ .veggie-burger{z-index:1071}.veggie-burger-fallback:checked ~ .veggie-burger .veggie-burger__icon{background-color:transparent}.veggie-burger-fallback:checked ~ .veggie-burger .veggie-burger__icon:before{top:0;-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}.veggie-burger-fallback:checked ~ .veggie-burger .veggie-burger__icon:after{bottom:0;-webkit-transform:rotate(45deg);transform:rotate(45deg)}@media (min-width: 61.25em){.veggie-burger-fallback:checked ~ .veggie-burger .veggie-burger__label{border:0 !important;clip:rect(0 0 0 0) !important;height:0.0625rem !important;margin:-0.0625rem !important;overflow:hidden !important;padding:0 !important;position:absolute !important;width:0.0625rem !important}}.veggie-burger-fallback:focus ~ .veggie-burger{background-color:#25b5d2}.monocolumn-wrapper{padding-left:0.625rem;padding-right:0.625rem}@media (min-width: 30em){.monocolumn-wrapper{padding-left:1.25rem;padding-right:1.25rem}}@media (min-width: 46.25em){.monocolumn-wrapper{max-width:38.75rem;margin-left:auto;margin-right:auto}}.monocolumn-wrapper .page-header{margin-left:0;margin-right:0}@media (min-width: 61.25em){.monocolumn-wrapper--no-limit-desktop{max-width:none}}.component{margin-bottom:1.25rem}.component--rhc{display:none}@media (min-width: 61.25em){.component--rhc{display:block;margin-top:2.25rem}}.component--rhc:first-child{margin-top:0}.component--rhc:last-child{margin-bottom:2.25rem}@media (min-width: 46.25em){.gs-container{max-width:46.25rem}}@media (min-width: 61.25em){.gs-container{max-width:61.25rem}}@media (min-width: 71.25em){.gs-container{max-width:71.25rem}}@media (min-width: 81.25em){.gs-container{max-width:81.25rem}}.img--inline{float:left;clear:left;width:7.125rem}@media (min-width: 30em){.img--inline{width:8.75rem}}.img--inline figcaption{padding-top:0.25rem;word-wrap:break-word}.loading,.preload-msg{padding:3.125rem 3.125rem 15.625rem;text-align:center}.loading .loading__link,.loading .accessible-link,.preload-msg .loading__link,.preload-msg .accessible-link{font-size:0.8125rem;line-height:1.125rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;display:inline-block}.loading .loading__animation,.preload-msg .is-updating{display:block;margin:0.625rem auto}.l-side-margins{position:relative;height:100%}@media (min-width: 46.25em){.l-side-margins:after,.l-side-margins:before{content:'';position:absolute;z-index:1;background:rgba(51,51,51,0.05);top:0;height:100%;width:0}.l-side-margins:before{left:0}.l-side-margins:after{right:0}.l-side-margins:before,.l-side-margins:after{width:-webkit-calc((100% - 46.25rem) / 2);width:calc((100% - 46.25rem) / 2)}}@media (min-width: 61.25em){.l-side-margins:before,.l-side-margins:after{width:-webkit-calc((100% - 61.25rem) / 2);width:calc((100% - 61.25rem) / 2)}}@media (min-width: 71.25em){.l-side-margins:before,.l-side-margins:after{width:-webkit-calc((100% - 71.25rem) / 2);width:calc((100% - 71.25rem) / 2)}}@media (min-width: 81.25em){.l-side-margins:before,.l-side-margins:after{width:-webkit-calc((100% - 81.25rem) / 2);width:calc((100% - 81.25rem) / 2)}.has-page-skin .l-side-margins{margin-left:auto;margin-right:auto;width:61.25rem}.has-page-skin .l-side-margins:before,.has-page-skin .l-side-margins:after{display:none}}@media (min-width: 46.25em){.l-side-margins--media:after,.l-side-margins--media:before{background:rgba(0,0,0,0.25)}.container__banding+.container__banding .l-side-margins--media:after,.container__banding+.container__banding .l-side-margins--media:before{background:rgba(51,51,51,0.15)}}.l-side-margins--paidgallery:before,.l-side-margins--paidgallery:after{content:none}@media (min-width: 46.25em){.has-flex .l-row{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-flex-wrap:nowrap;-ms-flex-wrap:nowrap;flex-wrap:nowrap;-webkit-align-content:stretch;-ms-flex-line-pack:stretch;align-content:stretch;-webkit-box-align:stretch;-webkit-align-items:stretch;-ms-flex-align:stretch;align-items:stretch;width:100%}.has-flex .l-row--reverse{-webkit-box-orient:horizontal;-webkit-box-direction:reverse;-webkit-flex-direction:row-reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse}.has-flex .l-row__item{-webkit-box-flex:1;-webkit-flex:1;-ms-flex:1;flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;-webkit-flex-basis:0;-ms-flex-preferred-size:0;flex-basis:0;width:0}.has-flex .l-row__item--boost-1{-webkit-box-flex:1.5;-webkit-flex-grow:1.5;-ms-flex-positive:1.5;flex-grow:1.5}.has-flex .l-row__item--boost-2{-webkit-box-flex:2;-webkit-flex-grow:2;-ms-flex-positive:2;flex-grow:2}}@media (max-width: 46.24em){.has-flex .l-row--layout-m{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap}.has-flex .l-row--layout-m .l-row__item{-webkit-flex-basis:50%;-ms-flex-preferred-size:50%;flex-basis:50%}.has-flex .l-row--layout-m .l-row__item--break-m{-webkit-box-flex:1;-webkit-flex:1 100%;-ms-flex:1 100%;flex:1 100%}}.has-no-flex .l-row{width:58.75rem}.has-no-flex .l-row:after,.has-no-flex .l-row:before{content:'';display:table}.has-no-flex .l-row:after{clear:both}.has-no-flex .l-row__item{float:left}.has-no-flex .l-row--items-2 .l-row__item{width:29.375rem}.has-no-flex .l-row--items-3 .l-row__item{width:19.58333rem}.has-no-flex .l-row--items-4 .l-row__item{width:14.6875rem}.popup--default{background:#f6f6f6;-webkit-box-shadow:0 0.0625rem 0.0625rem 0 rgba(0,0,0,0.25);box-shadow:0 0.0625rem 0.0625rem 0 rgba(0,0,0,0.25);left:0;top:2.6875rem;padding:0}.popup{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;position:absolute;margin:0;list-style:none;min-width:8.75rem}@media (min-width: 30em){.popup{right:auto;bottom:auto;top:2.8125rem}}@media (min-width: 46.25em){.brand-bar__item--has-control .popup{left:2.875rem}}.l-header--is-slim .brand-bar__item--has-control .popup{left:0}@media (min-width: 46.25em){.brand-bar__item--right .popup{left:auto;right:0}}.popup__group{z-index:3;margin:0;padding:0 0.625rem}.popup__group-header{font-size:0.8125rem;line-height:1.125rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;color:#767676;padding:0.375rem 0.625rem;border-top:0.0625rem solid #dcdcdc;padding-bottom:0;margin:0}.popup__group-header:first-of-type{border-top:0}.has-popup{cursor:default;position:relative}.popup-container{position:relative;z-index:11}.popup__toggle:after{content:'';display:inline-block;pointer-events:none;width:0;height:0;border-bottom:0;margin-top:0.125rem;margin-bottom:0.125rem;margin-left:0.25rem;border-left:0.25rem solid transparent;border-right:0.25rem solid transparent;border-top:0.25rem solid #f6f6f6}.popup__toggle.is-active:after,.is-active>.popup__toggle:after,.is-not-modern .brand-bar__item--has-control:hover .popup__toggle:after,.is-not-modern .is-signed-in.brand-bar__item--profile:hover .popup__toggle:after{border-top:0;border-bottom:0.25rem solid #f6f6f6}.popup__toggle.is-active:before,.is-active>.popup__toggle:before,.is-not-modern .brand-bar__item--has-control:hover .popup__toggle:before,.is-not-modern .is-signed-in.brand-bar__item--profile:hover .popup__toggle:before{content:'';display:inline-block;width:0;height:0;border-top:0;position:absolute;left:50%;border-left:0.375rem solid transparent;border-right:0.375rem solid transparent;border-bottom:0.375rem solid #f6f6f6;top:2.4375rem}@media (min-width: 46.25em){.has-popup .popup__toggle.is-active:before,.has-popup .is-active>.popup__toggle:before{margin-left:1.0625rem}}@media (max-width: 46.24em){.brand-bar__item--search .popup__toggle.is-active:before,.brand-bar__item--search .is-active>.popup__toggle:before{margin-left:-0.375rem}}@media (min-width: 46.25em){.brand-bar__item--right .popup__toggle.is-active:before,.brand-bar__item--right .is-active>.popup__toggle:before{margin-left:-0.75rem}}.popup__toggle.is-active:before,.l-header--is-slim .popup__toggle.is-active:before,.is-active>.popup__toggle:before,.l-header--is-slim .is-active>.popup__toggle:before{margin-left:-0.375rem}@media (max-width: 46.24em){.l-header .popup__toggle:after{display:none}}.l-header--is-slim.l-header .popup__toggle:after{display:none}.popup__item{display:block;line-height:2.25rem}.popup__item a{border-bottom:0.0625rem solid #dfdfdf}.popup__item:last-child{border-bottom:0}.popup__item,.popup__action{text-align:left}.popup .brand-bar__item--action,.popup .brand-bar__item--action:hover{display:block;white-space:nowrap;color:#333;line-height:2.25rem}.popup .brand-bar__item--inline-action{display:inline-block !important;margin-right:0.3125rem}.brand-bar__item--profile:not(.is-signed-in) .popup__toggle:before,.brand-bar__item--profile:not(.is-signed-in) .popup__toggle:after{display:none !important}.popup--search{z-index:1030;padding:0;right:0;padding-top:0.3125rem;min-height:3.1875rem;top:2.25rem 0.25rem}@media (min-width: 30em){.popup--search{top:2.8125rem}}@media (min-width: 46.25em){.popup--search{right:auto;width:40rem;min-height:4.25rem;left:0.625rem;padding:1.25rem;padding-top:1.5625rem}}@media (min-width: 71.25em){.popup--search{left:50%;margin-left:-35rem}}@media (min-width: 81.25em){.popup--search{margin-left:-40rem}}.popup--search .search-box{margin-bottom:-0.0625rem}.ad-feedback.popup__toggle{display:inline-block;cursor:pointer}.ad-feedback.popup__toggle::after{border-top-color:#6e6e6e;border-bottom-color:#6e6e6e}.ad-feedback.popup__toggle::before{display:none}.ad-feedback.popup{width:15rem;top:100%;border:0.0625rem solid #dcdcdc;z-index:1050;padding:0}.ad-feedback.popup ul{margin:0}.ad-feedback.popup li.popup__item::before{content:none}.ad-feedback.popup .popup__group-header{padding-bottom:0.375rem}.ad-feedback.popup .popup__item--option{position:relative;border-top:0.0625rem solid #dcdcdc}.ad-feedback.popup .popup__item--option>button{cursor:pointer;padding:0 0.625rem;width:100%;border:0;background:transparent;text-align:left}.ad-feedback.popup .popup__item--option>button:focus,.ad-feedback.popup .popup__item--option>button:hover{background:#dfdfdf}.ad-slot--dark .ad-feedback.popup{background:#161616;border-color:#333;color:#bdbdbd}.ad-slot--dark .ad-feedback.popup .popup__group-header{color:#bdbdbd}.ad-slot--dark .ad-feedback.popup .popup__item--option{border-top-color:#333}.ad-slot--dark .ad-feedback.popup .popup__item--option>button:hover{background:#333}@media (max-width: 46.24em){.fc-container .ad-slot--container-inline .ad-feedback.popup{top:-0.625rem;left:0.625rem}}@media (max-width: 61.24em){.fc-slice__popular-mpu .ad-feedback.popup{top:-0.625rem;left:0.625rem}}.nav{list-style:none;margin:0;padding:0.5rem 0 0.25rem}.nav .nav__item--full{width:100%;margin:0}.nav>li,.nav>li>a{display:inline-block;zoom:1}.nav--columns{padding:0 0.625rem}@media (min-width: 30em){.nav--columns{padding-left:1.25rem;padding-right:1.25rem}}.nav--columns>.nav__item{float:left;width:50%;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-right:0.625rem}.nav--columns>.nav__item:nth-child(odd){clear:left}.nav--columns>.nav__item:nth-child(even){padding-right:0;padding-left:0.625rem}.nav--columns .nav__link{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:900;display:block;padding:0.1875rem 0 1rem;border-top:0.0625rem solid #f0f0f0;height:auto;background-color:transparent;-webkit-font-smoothing:subpixel-antialiased;text-decoration:none}.nav--columns .nav__link:link,.nav--columns .nav__link:visited{color:#333}.nav--columns .nav__link:hover,.nav--columns .nav__link:focus{color:#94b1ca}.nav--columns-football{padding-top:0.5rem;padding-bottom:0.25rem}.nav .nav__item .nav__link--faded:link,.nav .nav__item .nav__link--faded:visited{color:#767676}.nav .nav__item .nav__link--faded:hover,.nav .nav__item .nav__link--faded:focus{color:#94b1ca}.nav--columns-football,.nav--no-horizontal-spacing{padding-left:0;padding-right:0}@media (min-width: 46.25em){.nav--guardian-services .nav__link{position:relative;top:-0.0625rem}}.video-nav-test-icon svg{height:0.625rem;width:0.9375rem;margin-left:0.3125rem}.brand-bar{background-color:#005689;line-height:0;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-left:0.625rem;padding-right:0.625rem}.brand-bar__item{font-size:0.875rem;line-height:1.25rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;float:left;color:#fff;height:2.25rem;padding-top:0.375rem;padding-bottom:0.375rem}.brand-bar__item,.l-header--is-slim .brand-bar__item{margin-right:0.1875rem;margin-left:0.1875rem}@media (min-width: 46.25em){.brand-bar__item{margin-right:0.625rem;margin-left:0.625rem}}.brand-bar__item .brand-bar__item--split--first{margin-left:0.3125rem;height:2.25rem}.brand-bar__item--split--first::after{content:'\200B';border-right:0.0625rem solid rgba(255,255,255,0.2);left:0.625rem;position:relative;height:1.5rem;bottom:-0.375rem;display:block}.brand-bar__item--split--last{padding-left:0.625rem;height:2.25rem}.brand-bar__item--action:active .control__icon-wrapper,.brand-bar__item--action:focus .control__icon-wrapper,.brand-bar__item--action.is-active .control__icon-wrapper{border-color:#ffffff}.brand-bar__item--action:hover .control__icon-wrapper{border-color:#ffffff}.brand-bar__item--action:hover .control__icon-wrapper--text{border-color:rgba(255,255,255,0.3)}.brand-bar__item--action,.brand-bar__item--action:focus{cursor:pointer;color:#fff;display:inline-block;vertical-align:middle;text-decoration:none;line-height:2.25rem}.brand-bar__item--action:focus,.brand-bar__item--action:focus .control__info,.brand-bar__item--action:active,.brand-bar__item--action:active .control__info{text-decoration:underline}.brand-bar__item--action:hover,.brand-bar__item--action:hover .control__info{text-decoration:underline}.brand-bar__item--right{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;float:right}.l-header--is-slim .brand-bar__item--right{float:left}.brand-bar__item--search{padding-left:0}.brand-bar__item--search .popup__toggle:after{display:none}.brand-bar__item--edition{cursor:pointer}.brand-bar__item--subscribe .control__icon-wrapper{border:0}.is-not-modern .brand-bar__item--has-control:hover .popup,.is-not-modern .brand-bar__item--has-control:focus .popup,.is-not-modern .is-signed-in.brand-bar__item--profile:hover .popup,.is-not-modern .is-signed-in.brand-bar__item--profile:focus .popup{display:block}.brand-bar__item__badge{background-color:rgba(75,198,223,0.4);color:#ffffff;margin-left:-0.25rem;float:left;z-index:-1;display:inline-block}.l-header--is-slim .brand-bar__item__badge{display:none}.control__info{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;display:none;height:1.875rem;line-height:2.25rem;margin-left:0.625rem;max-width:8.75rem;vertical-align:top;float:left;text-align:left}@media (min-width: 33.75em){.control__info{max-width:12.5rem}}@media (min-width: 46.25em){.brand-bar__item--right .control__info{margin:0}}@media (min-width: 46.25em){.control__info{display:block}}.l-header--is-slim .control__info{display:none}.control__icon-wrapper{border:0.0625rem solid rgba(255,255,255,0.3);float:left;height:2.125rem;width:2.125rem;text-align:center;line-height:3}@media (min-width: 46.25em){.brand-bar__item--right .control__icon-wrapper{display:none}}.l-header--is-slim .brand-bar__item--right .control__icon-wrapper{display:block}.control__icon-wrapper--text{-webkit-border-radius:62.5rem;border-radius:62.5rem;line-height:2.25rem;border-color:transparent}@media (min-width: 20em){.control__icon-wrapper--text{display:none}}@media (min-width: 46.25em){.control__icon-wrapper--text{display:inline-block}}.control__icon-wrapper--text:hover{color:#ffffff}.ad-slot{position:relative;z-index:1010;overflow:initial}.js-off .ad-slot{display:none}.ad-slot-container>:last-child{margin-bottom:0;padding-bottom:1.5rem}.ad-slot--dark{background-color:#1c1c1c}.ad-slot--right{position:-webkit-sticky;position:sticky;top:0}.has-sticky .paidfor-band ~ .content__main .ad-slot--right{top:2.875rem}.ad-slot--right.is-sticky{width:18.75rem}.ad-slot__label{font-size:0.75rem;line-height:1.25rem;position:relative;height:1.5rem;background-color:#f6f6f6;margin:0 auto;padding:0 0.5rem;border-top:0.0625rem solid #dfdfdf;color:#6e6e6e;text-align:left;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif}.ad-slot--dark .ad-slot__label{color:#bdbdbd;border-top-color:#333;background-color:transparent}.ad-slot__label.feedback-submitted .ad-feedback,.ad-slot__label .ad-feedback__thanks-message{display:none}.ad-slot__label.feedback-submitted .ad-feedback__thanks-message{display:inline-block;float:right}.top-banner-ad-container{background-color:#f6f6f6;top:0}.top-banner-ad-container:not(.top-banner-ad-container--not-sticky){position:-webkit-sticky;position:sticky;z-index:1020}@media (min-width: 61.25em){.top-banner-ad-container:not(.top-banner-ad-container--not-sticky){z-index:1080}}.top-banner-ad-container--fabric{overflow:hidden}.sticky-top-banner-ad{-webkit-transform:translate3d(0, 0, 0);transform:translate3d(0, 0, 0);contain:layout;z-index:1040;width:100%;position:fixed;top:0}.sticky-top-banner-ad--animate{will-change:transform;-webkit-transition:height 1s cubic-bezier(0, 0, 0, 0.985);transition:height 1s cubic-bezier(0, 0, 0, 0.985)}.ad-slot--top-banner-ad{text-align:center}.ad-slot--top-banner-ad .ad-slot__label{width:45.5rem;border-top:0;padding:0;height:1.125rem}@media (min-width: 81.25em){.ad-slot--top-banner-ad .ad-slot__label{margin:0}}@media (min-width: 81.25em){.has-page-skin .ad-slot--top-banner-ad{width:auto !important;padding-left:0 !important;text-align:center}.has-page-skin .ad-slot--top-banner-ad .ad-slot__label{margin-left:auto;margin-right:auto}}.ad-slot--top-banner-ad-desktop{margin:0 auto;min-height:5.625rem;padding-bottom:1.125rem;padding-top:1.125rem}@media (max-width: 46.24em){.ad-slot--top-banner-ad-desktop{display:none}}@media (min-width: 81.25em){.ad-slot--top-banner-ad-desktop{padding-left:16.25rem;margin-left:-webkit-calc(50% - 40.625rem);margin-left:calc(50% - 40.625rem);text-align:left}.ad-slot--top-banner-ad-desktop:not(.ad-slot--fluid):not(.ad-slot--fabric):not(.ad-slot--fluid250){max-width:60.625rem}.has-page-skin .ad-slot--top-banner-ad-desktop{margin-left:auto}}.ad-slot--top-banner-ad-desktop.ad-slot--fabric>.ad-slot__label{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box;margin-left:0.625rem;margin-right:0.625rem}@media (min-width: 30em){.ad-slot--top-banner-ad-desktop.ad-slot--fabric>.ad-slot__label{margin-left:1.25rem;margin-right:1.25rem}}@media (min-width: 41.25em){.ad-slot--top-banner-ad-desktop.ad-slot--fabric>.ad-slot__label{margin-left:auto;margin-right:auto;width:38.75rem}}@media (min-width: 46.25em){.ad-slot--top-banner-ad-desktop.ad-slot--fabric>.ad-slot__label{padding-left:1.25rem;padding-right:1.25rem}}@media (min-width: 46.25em){.ad-slot--top-banner-ad-desktop.ad-slot--fabric>.ad-slot__label{width:43.75rem}}@media (min-width: 61.25em){.ad-slot--top-banner-ad-desktop.ad-slot--fabric>.ad-slot__label{width:58.75rem}}@media (min-width: 71.25em){.ad-slot--top-banner-ad-desktop.ad-slot--fabric>.ad-slot__label{width:68.75rem}}@media (min-width: 81.25em){.ad-slot--top-banner-ad-desktop.ad-slot--fabric>.ad-slot__label{width:78.75rem}}.ad-slot--top-banner-ad-desktop .ad-slot__label{margin-top:-1.125rem}.ad-slot--inline,.ad-slot--container-inline,.ad-slot--container-inline.ad-slot--fluid,.ad-slot--gallery-inline,.ad-slot--liveblog-inline{width:18.75rem;margin:0.75rem auto;min-width:18.75rem;min-height:17.125rem;text-align:center}@media (min-width: 30em){.ad-slot--inline,.ad-slot--container-inline,.ad-slot--container-inline.ad-slot--fluid,.ad-slot--gallery-inline,.ad-slot--liveblog-inline{width:20rem}}@media (min-width: 46.25em){.ad-slot--inline,.ad-slot--container-inline,.ad-slot--container-inline.ad-slot--fluid,.ad-slot--gallery-inline,.ad-slot--liveblog-inline{width:auto}}.ad-slot--inline .ad-slot__label,.ad-slot--container-inline .ad-slot__label,.ad-slot--container-inline.ad-slot--fluid .ad-slot__label,.ad-slot--gallery-inline .ad-slot__label,.ad-slot--liveblog-inline .ad-slot__label{background-color:transparent}@media (min-width: 30em){.ad-slot--container-inline,.ad-slot--container-inline.ad-slot--fluid{margin-top:0}}@media (min-width: 46.25em){.ad-slot--container-inline,.ad-slot--container-inline.ad-slot--fluid{margin:0 0.625rem}}.ad-slot--gallery-inline{background-color:#161616}@media (min-width: 30em){.ad-slot--gallery-inline{width:18.75rem}}@media (min-width: 46.25em){.ad-slot--gallery-inline{width:auto}}@media (min-width: 61.25em){.ad-slot--gallery-inline,.ad-slot--gallery-inline .ad-slot__label{text-align:left}}.ad-slot--inline,.ad-slot--container-inline{background-color:#f6f6f6}@media (min-width: 46.25em){.ad-slot--inline,.ad-slot--container-inline{width:18.75rem}}@media (min-width: 46.25em){.ad-slot--inline{float:right;margin-top:0.25rem;margin-left:1.25rem}}@media (min-width: 46.25em) and (max-width: 71.24em){.ad-slot--inline{clear:left}}.ad-slot__content>div{margin:0 auto}.ad-slot--container-inline:not(.ad-slot--fluid) .ad-slot__content{margin:0 auto}@media (min-width: 46.25em){.ad-slot--container-inline:not(.ad-slot--fluid){position:relative;height:auto}.content-footer .ad-slot--container-inline:not(.ad-slot--fluid){width:18.75rem}.linkslist-container .ad-slot--container-inline:not(.ad-slot--fluid){position:absolute;top:0;right:0}.ad-slot--container-inline:not(.ad-slot--fluid) .ad-slot__label{padding:0 1.25rem}.ad-slot--container-inline:not(.ad-slot--fluid) .ad-slot__content{position:absolute;right:0;bottom:0;left:0;top:1.5rem;height:15.625rem}}@media (min-width: 46.25em){.ad-slot--liveblog-inline{padding-bottom:1.5rem}.ad-slot--liveblog-inline>div:not(.ad-slot__label){width:18.75rem;margin-left:auto;margin-right:auto}}.ad-slot--liveblog-inline{background-color:#eaeaea}.ad-slot--liveblog-inline .ad-slot__label{color:#767676;border-top-color:#bdbdbd}.ad-slot--mpu-banner-ad{display:none;width:18.75rem;min-height:17.125rem;margin-bottom:1.5rem}@media (min-width: 61.25em){.ad-slot--mpu-banner-ad{display:block}}.ad-slot--adfeature{background-color:#ccc}@media (min-width: 61.25em){.ad-slot--outstream{width:38.75rem;height:23.375rem}}@media (min-width: 81.25em){.has-page-skin .ad-slot--commercial-component,.has-page-skin .ad-slot--commercial-component-high{margin-left:auto;margin-right:auto;width:61.25rem}}.fc-container--commercial .ad-slot--commercial-component-high{margin-bottom:1.5rem}.ad-slot--im{float:left;width:8.125rem}@media (min-width: 30em){.ad-slot--im{width:13.75rem}}.ad-slot--im:not(.ad-slot--rendered){width:0;height:0}.ad-slot--im.ad-slot--rendered{margin:0.3125rem 0.625rem 0.375rem 0}@media (min-width: 30em){.ad-slot--im.ad-slot--rendered{margin-bottom:0.75rem;margin-right:1.25rem}}@media (min-width: 30em){.ad-slot--inline-book,.ad-slot--books-inline{width:8.75rem}}@media (min-width: 46.25em) and (max-width: 71.24em){.fc-container--sponsored .fc-container:first-child .fc-container__header+.fc-container__body,.fc-container--paid-content .fc-container:first-child .fc-container__header+.fc-container__body,.fc-container--sponsored .fc-container__header+.fc-container__body,.fc-container--paid-content .fc-container__header+.fc-container__body{margin-top:4.875rem}}.ad-slot--page-skin{height:0;overflow:hidden}@media (min-width: 20em) and (max-width: 81.24em){.has-page-skin{background-image:none !important}}.ad-slot--fluid{min-height:15.625rem;line-height:0.625rem;padding:0;margin:0}.ad-slot--fluid:not(.ad-slot--im){width:auto}.ad-slot--fluid.ad-slot--commercial-component-high,.ad-slot--fluid.ad-slot--commercial-component-high>.ad-slot__content>iframe{-webkit-transition:height 1s;transition:height 1s}@media (min-width: 20em) and (max-width: 29.99em){.ad-slot--fluid.ad-slot--liveblog-inline{margin-left:-0.625rem;margin-right:-0.625rem}}@media (min-width: 30em) and (max-width: 46.24em){.ad-slot--fluid.ad-slot--liveblog-inline{margin-left:-1.25rem;margin-right:-1.25rem}}.ad-slot--fabric-v1{min-height:15.625rem}.ad-slot--fabric{overflow:hidden;width:auto;min-height:15.625rem;padding-left:0;padding-right:0;padding-bottom:0}@media (min-width: 81.25em){.ad-slot--fabric.ad-slot--top-banner-ad-desktop{margin-left:0}}.ad-slot--fabric-v1,.ad-slot--fluid250{width:auto;margin-left:0;padding:0}.ad-slot--fabric-v1 .ad-slot__label,.ad-slot--fluid250 .ad-slot__label{display:none}@media (min-width: 61.25em){.ad-slot--fluid250{min-height:15.625rem}}@media (min-width: 61.25em){.ad-slot--offset-right{margin-right:-20em}}@media (min-width: 81.25em){.ad-slot--offset-right{margin-right:-25em}}.ad-slot--survey{height:0}.media:after,.media:before,.media__body:after,.media__body:before{content:'';display:table}.media:after,.media__body:after{clear:both}.media__img{float:left;margin-right:0.9375rem}.media__img img{display:block}.media__container--hidden{display:none !important}.media__placeholder--active{display:block;position:relative}.media__container--active{display:block}.media__placeholder--hidden{display:none !important}.page-header{font-size:1.25rem;line-height:1.5rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;padding:0 0 1rem;margin:0 0.625rem 0.25rem;border-bottom:0.0625rem dotted #dcdcdc}@media (min-width: 30em){.page-header{margin-left:1.25rem;margin-right:1.25rem}}.page-sub-header{font-size:1.125rem;line-height:1.5rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:900;padding:0.125rem 0 0.25rem;margin-bottom:0.75rem}.no-indent-article__zone .page-sub-header,.monocolumn-wrapper .page-sub-header,.fc-container__inner .page-sub-header{margin-left:0;margin-right:0}.page-sub-header>a{display:block}.message{padding:0.6875rem;background-color:#ffffee}.is-modern .has-localnav h2.article__zone:only-child,.is-modern .has-localnav .hide-on-mobile-if-localnav{display:none}@media (min-width: 46.25em){.is-modern .has-localnav h2.article__zone:only-child,.is-modern .has-localnav .hide-on-mobile-if-localnav{display:block}}.navigation-container{background:#005689}.navigation{position:relative;overflow:hidden;clear:both;background:#e5e5e5;height:2.25rem}.navigation:before,.navigation:after{content:'';display:block;position:absolute;top:0;left:0;right:0;height:2.25rem}.navigation:before{background:#00507f;-webkit-background-clip:padding-box;background-clip:padding-box}.navigation:after{top:auto;bottom:0;z-index:-1}.navigation-container--collapsed .navigation:after{display:none}.top-navigation,.local-navigation,.global-navigation,.signposting{font-size:1rem;line-height:1.375rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;line-height:2.25rem;font-weight:600;-webkit-font-feature-settings:'kern' 1}.top-navigation a,.top-navigation a:active,.top-navigation a:focus,.local-navigation a,.local-navigation a:active,.local-navigation a:focus,.global-navigation a,.global-navigation a:active,.global-navigation a:focus,.signposting a,.signposting a:active,.signposting a:focus{text-decoration:none}.top-navigation a:hover,.local-navigation a:hover,.global-navigation a:hover,.signposting a:hover{text-decoration:underline}.top-navigation{background:#00456e}.navigation__container--first{background:#00456e;min-height:2.25rem}.navigation__expandable{background:#333;overflow:hidden}.signposting,.local-navigation,.top-navigation,.global-navigation,.global-navigation__children{list-style-type:none;margin:0;padding:0}.signposting{background:#dfdfdf;border-right:0.0625rem solid #ececec;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-right:0.625rem}@media (min-width: 30em){.signposting{padding-left:0.625rem}}@media (max-width: 61.24em){.navigation-container--expanded .navigation--has-local-navigation .signposting{border-bottom:0.0625rem solid #ececec}}@media (min-width: 46.25em){.signposting{border-right-width:0}.navigation--has-local-navigation .signposting{border-right-width:0.0625rem}}@media (min-width: 46.25em){.navigation-container--expanded .signposting{min-width:10rem}}@media (min-width: 81.25em){.navigation-container--expanded .signposting{min-width:15rem}}.signposting__item{white-space:nowrap;display:table-cell}.signposting__action{color:#005689;text-decoration:none;display:table-cell}.signposting__separator{display:table-cell;vertical-align:top;line-height:1}.signposting__separator__inner{font-weight:200;color:#767676;font-size:1.6875rem;line-height:2.25rem}.local-navigation{background:#dfdfdf}.signposting__action,.local-navigation__action,.top-navigation__action,.global-navigation__action{padding-left:0.625rem;padding-right:0.625rem;height:100%}@media (min-width: 61.25em) and (max-width: 71.24em){.signposting__action,.local-navigation__action,.top-navigation__action,.global-navigation__action{padding-right:0.3125rem;padding-left:0.3125rem}.signposting__action:first-child,.local-navigation__action:first-child,.top-navigation__action:first-child,.global-navigation__action:first-child{padding-left:0.625rem}}@media (min-width: 81.25em){.has-page-skin .signposting__action,.has-page-skin .local-navigation__action,.has-page-skin .top-navigation__action,.has-page-skin .global-navigation__action{padding-right:0.3125rem;padding-left:0.3125rem}.has-page-skin .signposting__action:first-child,.has-page-skin .local-navigation__action:first-child,.has-page-skin .top-navigation__action:first-child,.has-page-skin .global-navigation__action:first-child{padding-left:0.625rem}}.local-navigation__action,.top-navigation__action{color:#333;z-index:3}.top-navigation__action{color:#fff;display:block}.global-navigation__action{color:#333;display:block}.local-navigation__item,.top-navigation__item,.global-navigation__item{overflow:hidden;white-space:nowrap}.top-navigation__item--current{margin-right:0.625rem}.local-navigation__item,.top-navigation__item{display:table-cell}.navigation-container--collapsed .navigation--has-signposting .local-navigation,.navigation-container--collapsed .navigation--has-signposting .top-navigation{padding-left:0.625rem}@media (min-width: 30em){.navigation-container--collapsed .local-navigation,.navigation-container--collapsed .top-navigation{padding-left:0.625rem}}.top-navigation__item--home{min-width:0.9375rem}.navigation--has-signposting .top-navigation__item--home{display:none}@media (min-width: 61.25em){.top-navigation__item--home{display:table-cell}}.top-navigation__icon{display:inline-block;background-repeat:no-repeat;-webkit-background-size:cover;background-size:cover}.top-navigation__icon--home{width:0.9375rem;height:1.125rem;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAASCAQAAAAul0yEAAAAO0lEQVQoz9XPsQ0AIAwDwYzuzZ8iQjIQUiLh9r5xhA0BinqInDqsggX34EAPSpzBFTOg3Su2o3+wGtYAGI94niPCbrMAAAAASUVORK5CYII=");margin-bottom:-0.1875rem}@media (-webkit-min-device-pixel-ratio: 1.3), (min-resolution: 124.8dpi), (min-resolution: 1.3dppx){.top-navigation__icon--home{background:url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNSAxOCI+PHBhdGggZD0ibTggMC0xIDAtNyA3IDAgMTAgMSAxIDQgMCAwLTcgNSAwIDAgNyA0IDAgMS0xIDAtMTB6IiBmaWxsPSIjZmZmIiAvPjwvc3ZnPg==")}}.global-navigation{background:#dfdfdf;clear:both}.global-navigation:after,.global-navigation:before{content:'';display:table}.global-navigation:after{clear:both}.global-navigation__section{display:block;clear:both;margin-right:0;overflow:hidden;position:relative;-webkit-box-shadow:inset 0 0.0625rem #ececec;box-shadow:inset 0 0.0625rem #ececec;background:#dfdfdf;min-height:2.25rem}@media (min-width: 46.25em){.global-navigation__section{padding-left:10rem}}@media (min-width: 81.25em){.global-navigation__section{padding-left:15rem}}.global-navigation__title{color:#fff;background:#00456e;float:left;border-top:0.0625rem solid #005689}@media (min-width: 46.25em){.global-navigation__title{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;position:absolute;top:0;bottom:0;left:0;background:#00456e;width:10rem;padding-left:1.25rem}}@media (min-width: 81.25em){.global-navigation__title{width:15rem}}.global-navigation__title.global-navigation__title--history{color:#333;background:#bdbdbd;border:0;padding-bottom:0}.global-navigation__children{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;min-height:2.25rem;padding-top:0.1875rem;overflow:hidden}@media (min-width: 46.25em){.global-navigation__children{padding-bottom:0.1875rem;padding-left:0.625rem}}.global-navigation__children.global-navigation__children--history{background:#bdbdbd}.global-navigation__children.global-navigation__children--history .button--tag{margin-top:0.375rem;margin-left:0.3125rem;margin-right:0;margin-bottom:0}.global-navigation__children.global-navigation__children--history .button--tag:hover{text-decoration:none}@media (max-width: 29.99em){.global-navigation__children.global-navigation__children--history{margin-left:0;padding-top:0;padding-left:0.41667rem}}@media (min-width: 46.25em){.global-navigation__action{float:left;line-height:1.875rem;white-space:nowrap}}.navigation-container--collapsed .navigation-container--collapsed__hide{display:none !important}.navigation-container--collapsed .navigation__container{display:table-cell;vertical-align:top}@media (max-width: 61.24em){.navigation-container--collapsed .navigation__scroll{overflow-x:scroll;white-space:nowrap;-webkit-backface-visibility:hidden;backface-visibility:hidden}}.navigation-container--collapsed .navigation__scroll::-webkit-scrollbar{display:none}.navigation-container--collapsed .navigation__expandable{display:none}.navigation-container--collapsed .navigation,.navigation-container--collapsed .signposting,.navigation-container--collapsed .local-navigation{height:2.25rem}.navigation-container--collapsed .signposting,.navigation-container--collapsed .local-navigation{display:table-cell}.navigation-container--collapsed .top-navigation{overflow:hidden}@media (min-width: 61.25em){.navigation-container--collapsed .top-navigation{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;position:absolute;top:0;left:0;right:0}}.navigation-container--collapsed .top-navigation__item:last-child{padding-right:5rem}@media (min-width: 61.25em){.navigation-container--collapsed .top-navigation__item:last-child{padding-right:0}}.navigation-container--default .navigation,.navigation-container--expanded .navigation{z-index:2;height:auto}.navigation-container--default .top-navigation,.navigation-container--expanded .top-navigation{display:none}.navigation-container--default .local-navigation,.navigation-container--expanded .local-navigation{overflow:hidden;background:#dfdfdf}@media (min-width: 30em){.navigation-container--default .local-navigation,.navigation-container--expanded .local-navigation{padding-left:0.625rem;padding-right:0.625rem}}.navigation-container--default .local-navigation__item,.navigation-container--expanded .local-navigation__item{float:left}.navigation-container--default .local-navigation__action,.navigation-container--expanded .local-navigation__action{display:block;float:left}@media (min-width: 61.25em){.navigation--has-signposting .navigation__inner:before{content:'';position:absolute;display:block;left:0;right:0;top:2.25rem;height:0.0625rem;background:#ececec;z-index:1}.navigation-container--collapsed .navigation--has-signposting{height:4.5rem}.navigation-container--expanded .navigation--has-signposting .top-navigation__item{visibility:hidden}.navigation--has-signposting .top-navigation{margin-left:0 !important}.navigation--has-signposting .top-navigation__item{display:table-cell}.navigation--has-signposting .signposting,.navigation--has-signposting .local-navigation{vertical-align:top;display:table-cell;height:2.25rem}.navigation--has-signposting .local-navigation{width:100%}.navigation--has-signposting .local-navigation__action{display:block;line-height:2.25rem}.navigation--has-signposting .navigation__container{display:table !important;width:100%}.navigation--has-signposting .navigation__container--first{background:#dfdfdf;border-top:2.25rem solid #00456e}.navigation--has-signposting .navigation__container--second{position:absolute;top:0}}.navigation .global-navigation__section--home,.navigation .top-navigation__item--current,.navigation .global-navigation--top .global-navigation__section--current{display:none}@media (min-width: 61.25em){.navigation .top-navigation__item--current{display:table-cell}}.navigation-toggle{font-size:1rem;line-height:1.375rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;font-weight:600;z-index:4;position:absolute;right:0;top:0;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;line-height:2.25rem;padding:0 0.625rem;background:#333;-webkit-background-clip:padding-box;background-clip:padding-box;text-align:left;border-left:0.125rem solid rgba(0,0,0,0.333333);outline:none;min-width:2.75rem}.navigation-toggle,.navigation-toggle:hover,.navigation-toggle:focus,.navigation-toggle:active{color:#fff}.navigation-toggle:focus{background:#434343}.navigation-container--expanded .navigation-toggle{border-left-color:transparent}@media (min-width: 61.25em){.navigation-toggle{border-left:0}}@media (min-width: 71.25em){.navigation-toggle{min-width:8.25rem}}@media (min-width: 81.25em){.navigation-toggle{min-width:11.625rem}}@media (min-width: 71.25em){.has-page-skin .navigation-toggle{min-width:2.75rem}}.is-not-modern .l-footer .navigation-toggle{min-width:2.75rem;font-size:1.5rem}.navigation-toggle-label__extra{display:none}@media (min-width: 71.25em){.navigation-toggle-label__extra{display:inline}}@media (max-width: 81.24em){.navigation-toggle-label__extra.navigation-toggle-label__extra--browse{display:none}}.l-header--slim-all .navigation-toggle-label__extra{display:none}@media (min-width: 81.25em){.has-page-skin .navigation-toggle-label__extra{display:none}}.navigation-toggle-label--close,.navigation-container--default .navigation-toggle-label--open,.navigation-container--expanded .navigation-toggle-label--open{display:none}.navigation-container--expanded .navigation-toggle-label--close{display:inline}.l-header--no-navigation:before{display:none}.l-header--no-navigation .navigation-container--collapsed .navigation__scroll{display:none}.l-header--no-navigation .navigation-container--collapsed .navigation,.l-header--no-navigation .navigation-container--collapsed .signposting,.l-header--no-navigation .navigation-container--collapsed .local-navigation{height:auto}@media (min-width: 61.25em){.l-header--no-navigation .navigation--has-signposting .navigation__container--first{border-top:0}}.l-header--no-navigation .navigation-toggle{float:left;min-width:0;line-height:3rem;position:static;border-left:0}.l-header--no-navigation .navigation-toggle-label__extra{display:none}.l-header--no-navigation .burger-icon{margin-top:1.125rem}.burger-icon,.burger-icon:before,.burger-icon:after{width:100%;height:0.125rem;background-color:#ebebeb}.burger-icon{width:1rem;display:inline-block;vertical-align:top;margin:0.8125rem 0.375rem 0 0;position:relative}.burger-icon:before,.burger-icon:after{content:'';position:absolute}.burger-icon:before{top:0.25rem}.burger-icon:after{top:0.5rem}.navigation-container--expanded .burger-icon{height:0}.navigation-container--expanded .burger-icon:before{-webkit-transform:rotate(45deg);transform:rotate(45deg);top:0.25rem}.navigation-container--expanded .burger-icon:after{-webkit-transform:rotate(-45deg) translate(0.1875rem, -0.1875rem);transform:rotate(-45deg) translate(0.1875rem, -0.1875rem);top:0.5rem}@media (min-width: 46.25em){.burger-icon,.burger-icon:before,.burger-icon:after{-webkit-transition:opacity .1s, -webkit-transform .1s ease-in;transition:opacity .1s, -webkit-transform .1s ease-in;transition:opacity .1s, transform .1s ease-in;transition:opacity .1s, transform .1s ease-in, -webkit-transform .1s ease-in}}.l-header--slim-all .burger-icon{margin-top:1.125rem}.rounded-icon{-webkit-border-radius:62.5rem;border-radius:62.5rem;display:inline-block;vertical-align:middle;position:relative}.rich-link{background-color:#eaeaea;margin:0;position:relative;overflow:hidden}.rich-link a{color:inherit}.rich-link .u-faux-block-link--hover{background-color:#eaeaea}.rich-link__title{font:inherit;line-height:inherit;padding:0}.rich-link .rich-link__header{font-size:1.25rem;line-height:1.5rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;font-weight:500;padding:0.25rem 0.3125rem 0.5em;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;min-height:2.25rem}.rich-link__read-more{padding-left:0.3125rem}.rich-link__arrow{display:inline-block}.rich-link__read-more-text{font-size:0.875rem;line-height:1.125rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;display:inline-block;height:1.875rem;line-height:1.625rem;padding-left:0.125rem;vertical-align:top;font-weight:500}.rich-link__link .u-faux-block-link__overlay{z-index:2}.rich-link__container{position:relative}.rich-link__container:before{background-color:#4bc6df;content:'';position:absolute;top:0;left:0;right:0;height:0.0625rem;z-index:2}.rich-link__container:after{content:'';display:table;clear:both}.element-rich-link{float:left;margin:0.3125rem 1.25rem 0.75rem 0;clear:both}@media (max-width: 29.99em){.element-rich-link{width:8.125rem;margin-bottom:0.375rem;margin-right:0.625rem}.element-rich-link .rich-link__header{font-size:0.875rem;line-height:1.125rem}}@media (min-width: 30em){.element-rich-link{width:13.75rem}}@media (min-width: 71.25em){.element-rich-link{margin-left:-10rem}.element-rich-link.element--supporting{width:18.75rem}}@media (min-width: 81.25em){.element-rich-link{margin-left:-15rem}.element-rich-link.element--supporting{width:23.75rem}}.reveal-caption{position:absolute;right:0.3125rem;width:2rem;height:2rem;z-index:1;background-color:rgba(51,51,51,0.4);-webkit-border-radius:50%;border-radius:50%}.reveal-caption:hover{background-color:#333}.reveal-caption--img{bottom:0.375rem}.caption--main{min-height:1.75rem;max-width:33.75rem;padding:0.5rem 0.625rem 1.5rem}@media (min-width: 46.25em){.caption--main{max-width:38.75rem;padding-left:0;padding-right:0}}@media (min-width: 61.25em){.caption--main{max-width:none}}@media (max-width: 46.24em){.caption--main.caption--img{position:absolute;left:0;right:0;bottom:0;background:rgba(22,22,22,0.8);color:#ffffff;display:none;padding:0.375rem 2.5rem 0.75rem 0.625rem;max-width:100%}.caption--main.caption--img a{color:currentColor}.caption--main.caption--img:before{content:none}}@media (max-width: 46.24em){.caption--main.caption--video,.content__main-column--image .caption--main{padding-bottom:0}}@media (max-width: 46.24em){.reveal-caption__checkbox:checked ~ .caption--main{display:block}.reveal-caption__checkbox:checked ~ .reveal-caption{background-color:#161616}.reveal-caption__checkbox:checked ~ .reveal-caption:hover{background-color:#333}.reveal-caption__checkbox:focus ~ .reveal-caption{background-color:#333}}.linkslist-container{position:relative;margin:0 !important}@media (min-width: 46.25em){.linkslist-container{margin-top:0.5625rem}}.linkslist-container.tone-feature:before{background:#fdadba}.linkslist-container.tone-comment:before{background:#ff9b0b}.linkslist-container.tone-media:before{background:#fb0}.linkslist-container.show-more--hidden,.linkslist-container.show-more--hidden:before{display:none}.linkslist{margin-top:0;width:100%}@media (min-width: 46.25em) and (max-width: 61.24em){.linkslist .fc-slice__item{width:50%}.linkslist .fc-slice__item:nth-child(2n+1){clear:both}.linkslist .fc-slice__item:nth-child(2n+1):before{border:0}.linkslist .fc-slice__item:nth-child(2n+1):nth-last-child(-n+4),.linkslist .fc-slice__item:nth-child(2n+2):nth-last-child(-n+3){padding-bottom:0}.linkslist .fc-slice__item:nth-child(2n+1):nth-last-child(-n+2),.linkslist .fc-slice__item:nth-child(2n+2):last-child{padding-top:0.75rem}}@media (min-width: 61.25em){.linkslist .fc-slice__item{width:33.33333%}.linkslist .fc-slice__item:nth-child(3n+1){clear:both}.linkslist .fc-slice__item:nth-child(3n+1):before{border:0}.linkslist .fc-slice__item:nth-child(3n+1):nth-last-child(-n+6),.linkslist .fc-slice__item:nth-child(3n+2):nth-last-child(-n+5),.linkslist .fc-slice__item:nth-child(3n+3):nth-last-child(-n+4){padding-bottom:0}.linkslist .fc-slice__item:nth-child(3n+1):nth-last-child(-n+3),.linkslist .fc-slice__item:nth-child(3n+2):nth-last-child(-n+2),.linkslist .fc-slice__item:nth-child(3n+3):last-child{padding-top:0.75rem}}@media (min-width: 46.25em){.has-flex-wrap .linkslist .fc-slice__item{-webkit-box-flex:0;-webkit-flex-grow:0;-ms-flex-positive:0;flex-grow:0;-webkit-flex-basis:50%;-ms-flex-preferred-size:50%;flex-basis:50%}}@media (min-width: 61.25em){.has-flex-wrap .linkslist .fc-slice__item{-webkit-flex-basis:33.33333%;-ms-flex-preferred-size:33.33333%;flex-basis:33.33333%}}.linkslist .item--has-cutout{padding-bottom:1.875rem}.fc-container__inner,.facia-container__inner,.fc-container__pagination,.index-page-header{overflow:hidden;position:relative;margin-left:0.625rem;margin-right:0.625rem}@media (min-width: 30em){.fc-container__inner,.facia-container__inner,.fc-container__pagination,.index-page-header{margin-left:1.25rem;margin-right:1.25rem}}@media (min-width: 46.25em){.fc-container__inner,.facia-container__inner,.fc-container__pagination,.index-page-header{margin-left:auto;margin-right:auto;padding-left:1.25rem;padding-right:1.25rem;width:38.75rem}}@media (min-width: 46.25em){.fc-container__inner,.facia-container__inner,.fc-container__pagination,.index-page-header{width:43.75rem}}@media (min-width: 61.25em){.fc-container__inner,.facia-container__inner,.fc-container__pagination,.index-page-header{width:58.75rem}}@media (min-width: 71.25em){.fc-container__inner,.facia-container__inner,.fc-container__pagination,.index-page-header{width:68.75rem}}@media (min-width: 81.25em){.fc-container__inner,.facia-container__inner,.fc-container__pagination,.index-page-header{width:78.75rem}}@media (min-width: 46.25em){.fc-container__inner--full-span,.facia-container__inner--full-span{width:46.25rem}}@media (min-width: 61.25em){.fc-container__inner--full-span,.facia-container__inner--full-span{width:61.25rem}}@media (min-width: 71.25em){.fc-container__inner--full-span,.facia-container__inner--full-span{width:71.25rem}}@media (min-width: 81.25em){.fc-container__inner--full-span,.facia-container__inner--full-span{width:81.25rem}}@media (min-width: 46.25em){.fc-container__inner--full-span,.facia-container__inner--full-span{padding-left:0;padding-right:0}}.js-on .js-hidden,.js-off .js-visible,.is-modern .modern-hidden,.is-not-modern .modern-visible{display:none}.is-off{display:none}.current{font-weight:bold}.is-on{display:block}.has-cursor{cursor:pointer}.maxed{width:100%}.shut>.panel{overflow:hidden;position:relative;max-height:0;padding-top:0}.update{float:right}.is-updating{display:none;width:2.5rem;height:1.25rem;-webkit-background-size:100% 100%;background-size:100%;margin-top:1.125rem}.is-updating.is-active{display:inline-block}.is-updating--dark{width:2.25rem;height:0.75rem}.is-live-icon{padding:0.0625rem 0.25rem 0.125rem;margin:0.0625rem 0.1875rem 0 0;font-size:0.625rem;font-style:normal;line-height:1;color:#ffffff;background-color:#ec1c1c;display:inline-block}.id--signed-out .sign-in-required{display:none}.is-sticky{position:fixed;top:0}.l-list{width:100%}@media (min-width: 46.25em){.has-flex-wrap .l-list{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap}}.l-list__item{float:left}.has-flex-wrap .l-list__item{-webkit-box-flex:0;-webkit-flex-grow:0;-ms-flex-positive:0;flex-grow:0;-webkit-flex-basis:100%;-ms-flex-preferred-size:100%;flex-basis:100%}@media (min-width: 46.25em){.l-row--cols-2 .l-row__item--span-1{width:50%;float:left}.has-flex .l-row--cols-2 .l-row__item--span-1{-webkit-box-flex:1;-webkit-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto}}@media (min-width: 46.25em){.l-row--cols-2 .l-row__item--span-2{width:100%;float:left}.has-flex .l-row--cols-2 .l-row__item--span-2{-webkit-box-flex:2;-webkit-flex:2 1 auto;-ms-flex:2 1 auto;flex:2 1 auto}}@media (min-width: 46.25em){.l-row--cols-2 .l-row__item--span-3{width:150%;float:left}.has-flex .l-row--cols-2 .l-row__item--span-3{-webkit-box-flex:3;-webkit-flex:3 1 auto;-ms-flex:3 1 auto;flex:3 1 auto}}@media (min-width: 46.25em){.l-row--cols-2 .l-row__item--span-4{width:200%;float:left}.has-flex .l-row--cols-2 .l-row__item--span-4{-webkit-box-flex:4;-webkit-flex:4 1 auto;-ms-flex:4 1 auto;flex:4 1 auto}}@media (min-width: 46.25em){.l-row--cols-2 .l-row__item--span-5{width:250%;float:left}.has-flex .l-row--cols-2 .l-row__item--span-5{-webkit-box-flex:5;-webkit-flex:5 1 auto;-ms-flex:5 1 auto;flex:5 1 auto}}@media (min-width: 46.25em){.l-row--cols-3 .l-row__item--span-1{width:33.33333%;float:left}.has-flex .l-row--cols-3 .l-row__item--span-1{-webkit-box-flex:1;-webkit-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto}}@media (min-width: 46.25em){.l-row--cols-3 .l-row__item--span-2{width:66.66667%;float:left}.has-flex .l-row--cols-3 .l-row__item--span-2{-webkit-box-flex:2;-webkit-flex:2 1 auto;-ms-flex:2 1 auto;flex:2 1 auto}}@media (min-width: 46.25em){.l-row--cols-3 .l-row__item--span-3{width:100%;float:left}.has-flex .l-row--cols-3 .l-row__item--span-3{-webkit-box-flex:3;-webkit-flex:3 1 auto;-ms-flex:3 1 auto;flex:3 1 auto}}@media (min-width: 46.25em){.l-row--cols-3 .l-row__item--span-4{width:133.33333%;float:left}.has-flex .l-row--cols-3 .l-row__item--span-4{-webkit-box-flex:4;-webkit-flex:4 1 auto;-ms-flex:4 1 auto;flex:4 1 auto}}@media (min-width: 46.25em){.l-row--cols-3 .l-row__item--span-5{width:166.66667%;float:left}.has-flex .l-row--cols-3 .l-row__item--span-5{-webkit-box-flex:5;-webkit-flex:5 1 auto;-ms-flex:5 1 auto;flex:5 1 auto}}@media (min-width: 46.25em){.l-row--cols-4 .l-row__item--span-1{width:25%;float:left}.has-flex .l-row--cols-4 .l-row__item--span-1{-webkit-box-flex:1;-webkit-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto}}@media (min-width: 46.25em){.l-row--cols-4 .l-row__item--span-2{width:50%;float:left}.has-flex .l-row--cols-4 .l-row__item--span-2{-webkit-box-flex:2;-webkit-flex:2 1 auto;-ms-flex:2 1 auto;flex:2 1 auto}}@media (min-width: 46.25em){.l-row--cols-4 .l-row__item--span-3{width:75%;float:left}.has-flex .l-row--cols-4 .l-row__item--span-3{-webkit-box-flex:3;-webkit-flex:3 1 auto;-ms-flex:3 1 auto;flex:3 1 auto}}@media (min-width: 46.25em){.l-row--cols-4 .l-row__item--span-4{width:100%;float:left}.has-flex .l-row--cols-4 .l-row__item--span-4{-webkit-box-flex:4;-webkit-flex:4 1 auto;-ms-flex:4 1 auto;flex:4 1 auto}}@media (min-width: 46.25em){.l-row--cols-4 .l-row__item--span-5{width:125%;float:left}.has-flex .l-row--cols-4 .l-row__item--span-5{-webkit-box-flex:5;-webkit-flex:5 1 auto;-ms-flex:5 1 auto;flex:5 1 auto}}@media (min-width: 46.25em){.l-list--columns-1 .l-list__item{width:100%}.l-list--columns-1 .l-list__item:nth-child(1n+1){clear:both}.l-list--columns-1 .l-list__item:nth-child(1n+1):before{border:0}.l-list--columns-1 .l-list__item:nth-last-child(1):nth-child(1n+1),.l-list--columns-1 .l-list__item:nth-last-child(1):nth-child(1n+1) ~ .l-list__item{padding-bottom:0}.has-flex-wrap .l-list--columns-1 .l-list__item{-webkit-flex-basis:100%;-ms-flex-preferred-size:100%;flex-basis:100%}}@media (min-width: 46.25em){.l-list--columns-2 .l-list__item{width:50%}.l-list--columns-2 .l-list__item:nth-child(2n+1){clear:both}.l-list--columns-2 .l-list__item:nth-child(2n+1):before{border:0}.l-list--columns-2 .l-list__item:nth-last-child(2):nth-child(2n+1),.l-list--columns-2 .l-list__item:nth-last-child(2):nth-child(2n+1) ~ .l-list__item{padding-bottom:0}.has-flex-wrap .l-list--columns-2 .l-list__item{-webkit-flex-basis:50%;-ms-flex-preferred-size:50%;flex-basis:50%}}@media (min-width: 46.25em){.l-list--columns-3 .l-list__item{width:33.33333%}.l-list--columns-3 .l-list__item:nth-child(3n+1){clear:both}.l-list--columns-3 .l-list__item:nth-child(3n+1):before{border:0}.l-list--columns-3 .l-list__item:nth-last-child(3):nth-child(3n+1),.l-list--columns-3 .l-list__item:nth-last-child(3):nth-child(3n+1) ~ .l-list__item{padding-bottom:0}.has-flex-wrap .l-list--columns-3 .l-list__item{-webkit-flex-basis:33.33333%;-ms-flex-preferred-size:33.33333%;flex-basis:33.33333%}}@media (min-width: 46.25em){.l-list--columns-4 .l-list__item{width:25%}.l-list--columns-4 .l-list__item:nth-child(4n+1){clear:both}.l-list--columns-4 .l-list__item:nth-child(4n+1):before{border:0}.l-list--columns-4 .l-list__item:nth-last-child(4):nth-child(4n+1),.l-list--columns-4 .l-list__item:nth-last-child(4):nth-child(4n+1) ~ .l-list__item{padding-bottom:0}.has-flex-wrap .l-list--columns-4 .l-list__item{-webkit-flex-basis:25%;-ms-flex-preferred-size:25%;flex-basis:25%}}.fc-container,.facia-container{position:relative;padding-bottom:0.75rem;margin-bottom:0}.fc-container:after,.fc-container:before,.facia-container:after,.facia-container:before{content:'';display:table}.fc-container:after,.facia-container:after{clear:both}@media (min-width: 81.25em){.has-page-skin .fc-container,.has-page-skin .facia-container{overflow:hidden;margin-left:auto;margin-right:auto;width:61.25rem}}.fc-container--commercial{padding-bottom:0}.fc-container__inner,.facia-container__inner{padding-top:0.1875rem}@media (min-width: 46.25em){.fc-container__inner,.facia-container__inner{padding-top:0.375rem}}@media (min-width: 81.25em){.has-page-skin .fc-container__inner,.has-page-skin .facia-container__inner{width:58.75rem}}.fc-container .fc-container__inner,.fc-container .facia-container__inner{border-top:0.0625rem solid #4bc6df}@media (min-width: 81.25em){.has-page-skin .fc-container__pagination{width:58.75rem}}.fc-container--rolled-up .fc-container--rolled-up-hide{display:none}.fc-slice-wrapper{padding-top:0.00063rem;margin:0 -0.625rem}.show-more--hidden .fc-slice-wrapper{display:none}.fc-container__header,.container__header{position:relative}@media (min-width: 46.25em) and (max-width: 71.24em){.fc-container--paid-for .fc-container__header,.fc-container[data-sponsorship] .fc-container__header,.fc-container[data-sponsorship] .fc-container:first-child .fc-container__header,.fc-container--paid-for .container__header,.fc-container[data-sponsorship] .container__header,.fc-container[data-sponsorship] .fc-container:first-child .container__header{float:left}}@media (min-width: 46.25em) and (max-width: 61.24em){.fc-container--paid-for .fc-container__header,.fc-container[data-sponsorship] .fc-container__header,.fc-container[data-sponsorship] .fc-container:first-child .fc-container__header,.fc-container--paid-for .container__header,.fc-container[data-sponsorship] .container__header,.fc-container[data-sponsorship] .fc-container:first-child .container__header{width:50%;padding-right:0.625rem}}@media (min-width: 61.25em) and (max-width: 71.24em){.fc-container--paid-for .fc-container__header,.fc-container[data-sponsorship] .fc-container__header,.fc-container[data-sponsorship] .fc-container:first-child .fc-container__header,.fc-container--paid-for .container__header,.fc-container[data-sponsorship] .container__header,.fc-container[data-sponsorship] .fc-container:first-child .container__header{width:66%;padding-right:0.625rem}}@media (min-width: 71.25em){.fc-container__header,.container__header{float:left;width:8.75rem}}@media (min-width: 81.25em){.fc-container__header,.container__header{width:13.75rem}.has-page-skin .fc-container__header,.has-page-skin .container__header{width:auto;float:none}}@media (max-width: 46.24em){.fc-container__header{overflow:hidden}.fc-container__header .fc-container__header__title{float:left;padding-right:0.3125rem}.fc-container__header .fc-container__header__description{margin-top:0.125rem;text-align:left}.fc-container--tag .fc-container__header{border-bottom:0}}@media (min-width: 46.25em) and (max-width: 71.24em){.fc-container--tag .fc-container__header{float:left;clear:left}}.fc-container__header__title,.fc-container__header__title--sticky,.container__title{font-size:1.375rem;line-height:1.75rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:900;position:relative;padding-bottom:0.25rem;line-height:1.5rem;color:#00456e}@media (min-width: 46.25em) and (max-width: 71.24em){.fc-container__header__title,.fc-container__header__title--sticky,.container__title{float:left;width:18.75rem}}@media (min-width: 71.25em) and (max-width: 81.24em){.fc-container__header__title,.fc-container__header__title--sticky,.container__title{font-size:1.25rem;line-height:1.5rem}}@media (min-width: 81.25em){.has-page-skin .fc-container__header__title,.has-page-skin .fc-container__header__title--sticky,.has-page-skin .container__title{float:left;width:18.75rem}}.fc-container__header__title a,.fc-container__header__title--sticky a,.container__title a{color:inherit}.fc-container__header__title a:hover,.fc-container__header__title--sticky a:hover,.container__title a:hover{color:#4bc6df}.fc-container__header__title a:hover .inline-icon,.fc-container__header__title--sticky a:hover .inline-icon,.container__title a:hover .inline-icon{fill:#4bc6df}.fc-container__header__title a .inline-icon,.fc-container__header__title--sticky a .inline-icon,.container__title a .inline-icon{fill:#005689;position:relative;height:.7em;width:1em}.fc-container__header__title--sticky{display:block;width:100%;text-align:left;margin-left:-1.25rem;padding:0.375rem 0 0 1.25rem;background:#ffffff;border:0}.fc-container__header__title--sticky button{color:#bdbdbd;font-weight:500;text-align:left;background:#ffffff;margin:0;padding:0;border:0;cursor:pointer}.fc-container__header__title--sticky:last-child{padding-bottom:1.5rem}.fc-container__header__title--stickies{display:none;visibility:hidden;margin-top:6.25rem}.has-page-skin .fc-container__header__title--stickies{display:none}.fc-container__header__title--stickies.fixed{position:fixed;bottom:0;z-index:99}@media (min-width: 71.25em){.fc-container__header__title--stickies{display:block;width:8.75rem}}@media (min-width: 81.25em){.fc-container__header__title--stickies{width:13.75rem}}.fc-container__header__image{display:table-cell;margin:0 1.25rem 0 0;overflow:hidden;float:left}@media (min-width: 71.25em){.fc-container__header__image{float:none;display:block;margin:0 0 0.75rem}}.fc-container__header__image img{display:block;width:5rem}@media (min-width: 61.25em){.fc-container__header__image img{width:6.25rem}}.fc-container__header__description{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;padding-bottom:0.375rem;color:#767676}@media (min-width: 46.25em){.fc-container__header__description{padding-bottom:0.75rem}}@media (min-width: 71.25em){.fc-container__header__description{width:8.75rem;clear:left;float:left;margin-top:0}}@media (min-width: 81.25em){.fc-container__header__description{width:13.75rem}}@media (max-width: 71.24em){.fc-container__header__social__action{position:absolute;right:0;top:0}.fc-container__header__social__action+.fc-container__header__social__action{display:none}}@media (min-width: 71.25em){.fc-container__header__social__action{border-top:0.0625rem dotted #dfdfdf;padding-top:0.375rem;margin-top:0.75rem;width:100%}.fc-container__header__social__action+.fc-container__header__social__action{border-top:0;margin-top:0;padding-top:0}}.fc-container__header__description--image{vertical-align:middle;display:table-cell}@media (min-width: 61.25em){.fc-container__header__description--image{max-width:33.75rem}}@media (min-width: 71.25em){.fc-container__header__description--image{display:block;height:auto;clear:both}}.fc-today{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;display:none}@media (min-width: 46.25em){.fc-today{display:block}}@media (min-width: 81.25em){.has-page-skin .fc-today .fc-today__sub{border-top:0;margin-top:0}}@media (min-width: 71.25em){.fc-today__sub{display:block}}@media (min-width: 81.25em){.has-page-skin .fc-today__sub{display:inline}}@media (min-width: 46.25em){.fc-show-more--mobile-only .button--show-more{display:none}}@media (max-width: 46.24em){.js-on .fc-show-more--hidden .fc-show-more--hide-on-mobile{display:none !important}}.js-on .fc-show-more--hidden .fc-show-more--hide{display:none !important}.fc-container__updated{font-size:0.875rem;line-height:1.125rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;display:block;position:absolute;right:0;bottom:0;padding-bottom:0.375rem;color:#767676}@media (min-width: 71.25em){.fc-container__updated{position:static;margin-top:1.25rem;border-top:0.0625rem dotted #bdbdbd;padding-top:0.1875rem}}@media (min-width: 81.25em){.has-page-skin .fc-container__updated{position:absolute;bottom:0;border-top:0}}.fc-timestamp{display:inline-block}.fc-container__body,.container__body{padding-top:0.375rem;padding-bottom:0.75rem;opacity:1;-webkit-transition:opacity .25s linear;transition:opacity .25s linear}@media (min-width: 46.25em){.fc-container__body,.container__body{padding-top:0.1875rem}}@media (min-width: 71.25em){.fc-container__body,.container__body{margin-left:10rem}}@media (min-width: 81.25em){.fc-container__body,.container__body{margin-left:15rem;width:58.75rem}.has-page-skin .fc-container__body,.has-page-skin .container__body{margin-left:0;clear:left}}@media (max-width: 71.24em){.fc-container__body,.container__body{clear:left}}@media (min-width: 71.25em) and (max-width: 81.24em){.fc-container--will-have-toggle .fc-container__body,.fc-container--has-toggle .fc-container__body,.fc-container--will-have-toggle .container__body,.fc-container--has-toggle .container__body{padding-top:2.25rem}}.fc-container__body--is-hidden{opacity:0;-webkit-transition:opacity .25s linear;transition:opacity .25s linear}.fc-container__toggle{font-size:0.875rem;line-height:1.25rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;min-height:2.25rem;min-width:3.75rem;position:absolute;top:-0.1875rem;right:0;border:0;background-color:transparent;color:#ffffff}.fc-container__toggle .inline-icon{-webkit-transform:rotate(180deg);transform:rotate(180deg);position:absolute;top:0.375rem;left:50%;margin-left:-0.75rem;fill:#333}.fc-container--rolled-up .fc-container__toggle .inline-icon{-webkit-transform:rotate(0deg);transform:rotate(0deg)}@media (min-width: 46.25em){.fc-container__toggle{text-align:right;color:#767676}.fc-container--paid-content .fc-container__toggle{border-left-width:0}.fc-container__toggle:hover,.fc-container__toggle:focus{color:#333}.fc-container__toggle .inline-icon{display:none}.fc-container__toggle .fc-container__toggle__text{display:block}}@media (min-width: 71.25em){.fc-container__toggle{left:65rem}}@media (min-width: 81.25em){.fc-container__toggle{left:75rem}.has-page-skin .fc-container__toggle{left:auto}}.fc-container__toggle__text{display:none;position:relative;top:-0.125rem}.fc-container--media .fc-container__inner,.fc-container--media .fc-slice__item+.fc-slice__item:before{border-color:#333}.fc-container--media .fc-container__header__title{color:#eaeaea}@media (max-width: 46.24em){.fc-container--media .fc-item__media-wrapper{padding-left:0 !important}}.fc-date-headline{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;color:#333;display:block;padding-bottom:0.375rem}.fc-container--tag{padding-bottom:0}.fc-container--tag .fc-container__inner{border-top:0.0625rem solid #dfdfdf}.fc-trending-topics{border-top:0 !important}.facia-page,.index-page{background-color:#ffffff}.index-page-header{padding-top:0.375rem;padding-bottom:0.75rem}.has-page-skin .index-page-header{width:58.75rem}.index-page-header__content{width:100%}@media (min-width: 81.25em){.index-page-header__content{width:73.75rem}.has-page-skin .index-page-header__content{width:100%}}.index-page-header__title{display:block;line-height:1.5rem;font-size:1.375rem;line-height:1.75rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:900}.index-page-header__title,.index-page-header__title a{color:#00456e}@media (min-width: 71.25em){.index-page-header__title{float:left;width:8.75rem;margin-right:1.25rem}}@media (min-width: 81.25em){.index-page-header__title{width:13.75rem}.has-page-skin .index-page-header__title{float:none}}@media (min-width: 71.25em) and (max-width: 81.24em){.index-page-header__title{font-size:1.25rem;line-height:1.5rem}}.index-page-header__description{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;color:#767676}@media (min-width: 71.25em){.index-page-header__description{float:left}}@media (min-width: 81.25em){.has-page-skin .index-page-header__description{float:none}}@media (min-width: 46.25em){.index-page-header__description{width:50%}}.index-page-header__image-wrapper{overflow:hidden;float:right}.index-page-header__image{display:block;float:right;height:5rem}@media (min-width: 61.25em){.index-page-header__image{height:6.25rem}}.index-page-header__image-wrapper--contributor-circle{-webkit-border-radius:62.5rem;border-radius:62.5rem}@media (max-width: 61.24em){.fc-container--lazy-load{display:none}.is-not-modern .fc-container--lazy-load{display:block}}.fc-container--video{background-color:#040404;padding-bottom:0;margin-bottom:0.75rem}.fc-container--video .gs-container{background-color:#161616;border-top:0.0625rem solid #fb0}.fc-container--video .fc-container__inner{border-top:0}@media (min-width: 71.25em){.fc-container--video .fc-container__inner{display:none}.has-page-skin .fc-container--video .fc-container__inner{display:block}}.fc-container--video .fc-item__image-container{display:block}.fc-container--video .u-responsive-ratio{padding-bottom:56.3%}.fc-container--video .gu-media-wrapper .vjs-paused.vjs-has-started .vjs-control-bar{bottom:-3.75rem}@media (min-width: 61.25em){.fc-container--video .vjs-big-play-button{display:none}}.fc-container--video .media__container--hidden{display:block !important;position:absolute;top:0;left:0;right:0;bottom:0;pointer-events:none;z-index:2}.fc-container--video .media__container--hidden video{display:none}.fc-container--video .gu-media-wrapper{background-color:transparent}@media (min-width: 61.25em){.fc-container--video .fc-item__video-fallback,.fc-container--video .gu-media{opacity:.3;-webkit-transition:opacity .4s ease-out;transition:opacity .4s ease-out}}.fc-container--video .treats__treat{background-color:transparent;border-color:#fb0}.fc-container--video .treats__treat:hover{border-color:#fb0;background-color:#fb0;color:#161616}@media (max-width: 61.24em){.fc-container--video .u-responsive-ratio video{top:inherit;bottom:0;height:auto}.fc-container--video .fc-item__video-container .vjs-big-play-button{top:3.375rem}.fc-container--video .fc-item__video-fallback{margin-top:6.75rem}}.fc-container--video-no-fill-sides{background-color:transparent}.video-title{color:#fb0;display:block;margin-bottom:0.75rem}.video-title a:hover{color:#ffffff;border-bottom:#ffffff}.video-playlist{position:relative;overflow:hidden}@media (min-width: 61.25em) and (max-width: 71.24em){.video-playlist{background-color:#090909}.has-page-skin .video-playlist{background-color:transparent}}.video-playlist--start .video-playlist__control--prev,.video-playlist--end .video-playlist__control--next{opacity:0;pointer-events:none}.video-playlist__inner{margin:0;font-size:0;white-space:nowrap;padding-right:0.625rem}@media (min-width: 30em){.video-playlist__inner{padding-right:1.25rem}}@media (max-width: 61.24em){.video-playlist__inner{overflow-x:scroll;overflow-y:hidden;-webkit-overflow-scrolling:touch;-webkit-transform:none !important;transform:none !important}}@media (min-width: 61.25em){.video-playlist__inner{padding-right:0;-webkit-transition:-webkit-transform .4s ease-out;transition:-webkit-transform .4s ease-out;transition:transform .4s ease-out;transition:transform .4s ease-out, -webkit-transform .4s ease-out}}.video-playlist__inner::-webkit-scrollbar{display:none}.video-playlist__control{display:none}@media (min-width: 61.25em){.video-playlist__control{width:8.75rem;position:absolute;display:block;top:0;bottom:0;z-index:2;cursor:pointer}.video-playlist__control:hover .video-playlist__icon{background-color:#fb0}.video-playlist__control:hover .video-playlist__icon svg{fill:#161616}}.video-playlist__control--prev{left:0}@media (min-width: 71.25em){.video-playlist__control--prev{width:11.25rem}.has-page-skin .video-playlist__control--prev{width:8.75rem}}@media (min-width: 81.25em){.video-playlist__control--prev{width:16.25rem}.has-page-skin .video-playlist__control--prev{width:8.75rem}}.video-playlist__control--prev .video-playlist__icon{right:1.25rem}.video-playlist__control--prev .video-playlist__icon svg{margin-left:-0.125rem}.video-playlist__control--next{right:0}@media (min-width: 71.25em){.video-playlist__control--next{width:16.25rem}.has-page-skin .video-playlist__control--next{width:8.75rem}}@media (min-width: 81.25em){.video-playlist__control--next{width:21.25rem}.has-page-skin .video-playlist__control--next{width:8.75rem}}.video-playlist__control--next .video-playlist__icon{left:1.25rem}.video-playlist__control--next .video-playlist__icon svg{margin-right:-0.125rem}.video-playlist__icon{position:absolute;top:0;bottom:0;width:1.875rem;height:1.875rem;margin:auto;-webkit-border-radius:50%;border-radius:50%;background-color:rgba(0,0,0,0.5);text-align:center}.video-playlist__icon svg{fill:#ffffff;width:0.5625rem;height:1.875rem}.video-playlist__item{position:relative;display:inline-block;vertical-align:top;width:70%;background-color:#161616;margin-left:0.625rem;margin-bottom:0.75rem}@media (min-width: 30em){.video-playlist__item{margin-left:1.25rem}}@media (min-width: 61.25em){.video-playlist__item{width:43.75rem;margin:0}}@media (min-width: 61.25em) and (max-width: 71.24em){.video-playlist__item--first{margin-left:8.75rem}.has-page-skin .video-playlist__item--first{margin-left:0}}@media (min-width: 71.25em){.video-playlist__item--first{margin-left:0}.has-page-skin .video-playlist__item--first{margin-left:0}}.video-playlist__item--active .vjs-big-play-button{display:block}.video-playlist__item--active .fc-item__video-fallback,.video-playlist__item--active .video-overlay,.video-playlist__item--active .gu-media{opacity:1}.video-title--leftcol{display:none}@media (min-width: 71.25em){.video-title--leftcol{position:relative;height:24.60938rem;display:inline-block;width:11.25rem;padding:0.375rem 1.25rem;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;margin-bottom:0;white-space:normal}}@media (min-width: 81.25em){.video-title--leftcol{width:16.25rem}.has-page-skin .video-title--leftcol{width:11.25rem}}.video-title--leftcol .inline-guardian-video-logo svg{margin-top:0.25rem;max-width:100%}.video-title--leftcol .inline-guardian-video-logo svg:hover .inline-guardian-video-logo__title{fill:#ffffff}.has-page-skin .video-title--leftcol{display:none}@media (min-width: 61.25em){.video-playlist__item--first{margin-left:8.75rem}}@media (min-width: 71.25em){.video-playlist__item--first{margin-left:0}.has-page-skin .video-playlist__item--first{margin-left:8.75rem}}.video-overlay{position:relative;z-index:2;white-space:normal;padding:0 0.3125rem 1.5rem;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;border-top:0.0625rem solid #fb0;color:#ffffff;background-color:rgba(0,0,0,0.5);height:8.25rem;margin-bottom:-1.5rem;pointer-events:auto}@media (min-width: 61.25em) and (max-width: 71.24em){.video-overlay{opacity:0;-webkit-transition:opacity .4s ease-out;transition:opacity .4s ease-out}}@media (min-width: 61.25em){.video-overlay{position:absolute;top:0.75rem;left:1.25rem;width:13.75rem}}@media (min-width: 61.25em){.video-playlist__item .vjs-playing ~ .video-overlay{visibility:hidden;opacity:0}}.video-overlay .video-overlay__headline{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;font-weight:500}@media (min-width: 30em){.video-overlay .video-overlay__headline{font-size:1.25rem;line-height:1.5rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;font-weight:500}}@media (min-width: 61.25em){.video-overlay .video-overlay__headline{height:6rem;overflow:hidden}}.video-overlay .inline-icon svg{position:relative}.video-overlay .fc-item__title--quoted .inline-quote{fill:#ffffff}.video-overlay .fc-item__link{color:#ffffff}.video-overlay .fc-item__link:visited{color:#bdbdbd}.video-overlay .fc-item__byline,.video-overlay .fc-item__kicker{color:#fb0}.video-overlay__duration{font-size:0.875rem;line-height:1.25rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;position:absolute;bottom:0.125rem;color:#bdbdbd}.fc-item__video-container .youtube-media-atom{z-index:1}.fc-item__video-container .youtube-media-atom.no-player{z-index:0}.fc-item__video-container .youtube-media-atom__iframe:not(.youtube__video-ready) ~ .youtube-media-atom__overlay{visibility:hidden}.fc-container--first{margin-top:0;padding-top:0}.fc-container--first .fc-container__inner{border:0}@media (min-width: 46.25em){.fc-container--first{padding-top:0.375rem}}@media (min-width: 71.25em){.fc-container--first .fc-container__header__title{border-top:0.0625rem solid #4bc6df;padding-top:0.1875rem}.fc-container--first .fc-container__body{padding-top:0}}@media (min-width: 71.25em) and (max-width: 81.24em){.fc-container--first .fc-slice-wrapper:first-child{padding-top:0}}@media (min-width: 81.25em){.has-page-skin .fc-container--first .fc-container__header__title{border-top:0;padding-top:0}}.fc-container--outbrain{background-color:#f6f6f6;display:none}@media (min-width: 20em){.fc-container--outbrain .fc-container__inner{min-height:38.8125rem}}@media (min-width: 46.25em){.fc-container--outbrain .fc-container__inner{min-height:28.4375rem}}@media (min-width: 61.25em){.fc-container--outbrain .fc-container__inner{min-height:24.375rem}}#membership-ab-thrasher{display:none}#membership-ab-thrasher.visible{display:block}.fc-container--thrasher{border-top:0;margin-top:0;margin-bottom:1.5rem;padding-bottom:0;background:#f1f1f1}.fc-container--thrasher .fc-container__inner{border-top:0;padding-top:0}@media (max-width: 46.24em){.fc-container--thrasher .fc-container__inner{margin-left:0;margin-right:0;width:100%}}.fc-container--thrasher .fc-container__header{display:none}.fc-container--thrasher .fc-container__body{padding-top:0;padding-bottom:0;margin-left:0;width:100%;overflow:initial}.fc-container--thrasher .fc-slice-wrapper{margin-left:0;margin-right:0}@media (min-width: 46.25em){.fc-container--thrasher .fc-slice-wrapper{margin-left:-1.25rem;margin-right:-1.25rem}}.fc-container--thrasher .fc-slice{margin:0;width:100%}.fc-container--thrasher .fc-slice__item{margin-bottom:0;width:100%}.fc-container--thrasher .fc-item{margin:0;width:100%}.fc-slice{overflow:hidden;margin-left:auto;margin-right:auto}@media (min-width: 46.25em){.fc-slice{overflow:visible}}.has-flex .fc-slice--hl4-h{-webkit-box-orient:horizontal;-webkit-box-direction:reverse;-webkit-flex-direction:row-reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse}.has-flex .fc-slice--hl4-h .fc-slice__item:before{display:none}.has-flex .fc-slice--hl4-h .fc-item--half-tablet:before{content:'';display:block;position:absolute;top:0;bottom:0;left:0;width:0.0625rem;height:100%;border-left:0.0625rem solid #dfdfdf}@media (min-width: 61.25em){.has-flex .fc-slice--hl4-h .fc-item--half-tablet .fc-item__standfirst{display:none}}@media (min-width: 46.25em) and (max-width: 61.24em){.fc-slice--h-ql4-ql4 .fc-item--half-tablet .fc-item__standfirst{display:block}}@media (min-width: 46.25em){.fc-slice--h-q-q .fc-item--half-tablet .fc-item__standfirst{display:none}}@media (min-width: 61.25em){.fc-slice--h-q-q .fc-item--standard-tablet .fc-item__standfirst{display:block}}@media (min-width: 46.25em){.fc-slice--h-q_ql2-ql4 .fc-item--half-tablet .fc-item__standfirst{display:block !important}}@media (max-width: 46.24em){.fc-slice--q-qqq .fc-item--list-mobile .fc-item__header{font-size:1.25rem;line-height:1.5rem}}@media (min-width: 46.25em) and (max-width: 61.24em){.facia-slice--q-q-ql-ql .fc-item--standard-tablet .fc-item__standfirst,.facia-slice--q-q-q-ql .fc-item--standard-tablet .fc-item__standfirst{display:block}}@media (min-width: 46.25em){.fc-slice-wrapper+.fc-slice-wrapper .fc-slice--q-q-q-q .fc-item--standard-tablet .fc-item__header{font-size:1rem;line-height:1.25rem}}.has-flex .fc-slice--h14-q-q{-webkit-box-orient:horizontal;-webkit-box-direction:reverse;-webkit-flex-direction:row-reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse}.has-flex .fc-slice--h14-q-q .fc-slice__item:before{display:none}@media (min-width: 46.25em){.has-flex .fc-slice--h14-q-q .fc-item--standard-tablet:before{content:'';display:block;position:absolute;top:0;bottom:0;left:0;width:0.0625rem;height:100%;border-left:0.0625rem solid #dfdfdf}}@media (min-width: 46.25em){.fc-slice--h14-q-q .fc-item--standard-tablet .fc-item__standfirst{display:block}}@media (min-width: 46.25em) and (max-width: 61.24em){.fc-slice--tl-tl-mpu>.fc-slice__item .fc-slice__item:before{border:0}.fc-slice--tl-tl-mpu>.fc-slice__item:first-child{-webkit-box-flex:1;-webkit-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto;width:50%}.fc-slice--tl-tl-mpu>.fc-slice__item:first-child .fc-slice__item{-webkit-flex-basis:100%;-ms-flex-preferred-size:100%;flex-basis:100%}.fc-slice--tl-tl-mpu>.fc-slice__item:first-child .fc-slice__item:nth-child(5){padding-bottom:0.75rem}.fc-slice--tl-tl-mpu>.fc-slice__item:last-child{width:50%}}@media (min-width: 46.25em) and (max-width: 61.24em){.fc-slice--t-t-mpu .fc-slice__item{width:25%}.fc-slice--t-t-mpu .fc-slice__item .fc-item__title{font-size:1rem;line-height:1.25rem}.fc-slice--t-t-mpu .fc-slice__item--mpu-candidate{width:50%}}@media (min-width: 46.25em) and (max-width: 61.24em){.fc-slice--t-tl-mpu>.fc-slice__item{width:25% !important}.fc-slice--t-tl-mpu>.fc-slice__item:last-child{-webkit-box-flex:2;-webkit-flex:2 1 auto;-ms-flex:2 1 auto;flex:2 1 auto;width:50% !important}}.popular-trails.fc-container__body{padding-top:0.75rem}@media (min-width: 61.25em){.popular-trails.fc-container__body{min-height:23.25rem;display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex}}@media (min-width: 61.25em){.popular-trails__content{min-width:38.75rem;max-width:66.66667%}}.fc-slice--popular .fc-slice__item:before{display:none}.fc-slice--popular .live-pulse-icon:before{content:none}@media (min-width: 61.25em){.fc-slice--popular .tabs__pane{min-width:38.75rem;min-height:18.75rem}.fc-slice--popular .tabs__pane--without-mpu{width:100%;min-height:18.75rem}}.fc-slice__popular-mpu{width:20rem;min-width:18.75rem;margin:0.75rem auto 0}.fc-slice__popular-mpu .ad-slot{min-height:17.125rem;margin:0}@media (min-width: 61.25em){.fc-slice__popular-mpu{width:auto;margin-left:auto;border-top:0.0625rem solid #dfdfdf;padding:0.75rem 0 0 1.25rem;margin-top:2.4375rem}.tabs__content .fc-slice__popular-mpu{border-top:0;margin-top:0;padding-top:0}.has-no-flex .fc-slice__popular-mpu{position:absolute;top:0.75rem;right:-0.625rem}}@media (max-width: 61.24em){.fc-slice__popular-mpu .fc-slice__item--no-mpu{min-height:0}}.fc-container--dynamic-slow-mpu .ad-slot--container-inline{width:18.75rem;padding-bottom:0.375rem}@media (min-width: 46.25em){.fc-container--dynamic-slow-mpu .ad-slot--container-inline{width:23.75rem}}@media (min-width: 61.25em){.fc-container--dynamic-slow-mpu .ad-slot--container-inline{width:18.75rem}}.fc-container--dynamic-slow-mpu .ad-slot__label{text-align:left}@media (max-width: 46.24em){.fc-slice--nav-list{-webkit-column-count:1;-moz-column-count:1;column-count:1;-webkit-column-gap:0;-moz-column-gap:0;column-gap:0;-webkit-column-rule:0.0625rem solid #dfdfdf;-moz-column-rule:0.0625rem solid #dfdfdf;column-rule:0.0625rem solid #dfdfdf}}@media (min-width: 46.25em) and (max-width: 61.24em){.fc-slice--nav-list{-webkit-column-count:3;-moz-column-count:3;column-count:3;-webkit-column-gap:0.625rem;-moz-column-gap:0.625rem;column-gap:0.625rem;-webkit-column-rule:0.0625rem solid #dfdfdf;-moz-column-rule:0.0625rem solid #dfdfdf;column-rule:0.0625rem solid #dfdfdf}}@media (min-width: 61.25em){.fc-slice--nav-list{-webkit-column-count:4;-moz-column-count:4;column-count:4;-webkit-column-gap:0.625rem;-moz-column-gap:0.625rem;column-gap:0.625rem;-webkit-column-rule:0.0625rem solid #dfdfdf;-moz-column-rule:0.0625rem solid #dfdfdf;column-rule:0.0625rem solid #dfdfdf}}.fc-slice__item--nav-list{display:inline-block;width:100%}@media (max-width: 46.24em){.fc-slice--nav-list--media{-webkit-column-count:1;-moz-column-count:1;column-count:1;-webkit-column-gap:0;-moz-column-gap:0;column-gap:0;-webkit-column-rule:0.0625rem solid #dfdfdf;-moz-column-rule:0.0625rem solid #dfdfdf;column-rule:0.0625rem solid #dfdfdf}}@media (min-width: 46.25em){.fc-slice--nav-list--media{-webkit-column-count:3;-moz-column-count:3;column-count:3;-webkit-column-gap:0.625rem;-moz-column-gap:0.625rem;column-gap:0.625rem;-webkit-column-rule:0.0625rem solid #dfdfdf;-moz-column-rule:0.0625rem solid #dfdfdf;column-rule:0.0625rem solid #dfdfdf}}.fc-sublink{position:relative;padding-top:0.1875rem;margin:0.5625rem 0}.fc-sublink a{display:block;z-index:1 !important}.fc-sublink__title{font-size:0.875rem;line-height:1.125rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;padding-top:0;margin:0;color:#333}.fc-sublink__title:before{display:block;position:absolute;top:0;left:0;content:'';width:40%;border-top:0.0625rem dotted #bdbdbd}.fc-sublink__title .fc-sublink__kicker{font-weight:500;float:left;margin-right:.2em}@media (max-width: 46.24em){.fc-item{width:100%}}@media (min-width: 46.25em){.has-flex .fc-item{-webkit-box-flex:1;-webkit-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto}.has-flex-wrap .fc-item{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex}.has-no-flex-wrap .fc-item:after,.has-no-flex-wrap .fc-item:before{content:'';display:table}.has-no-flex-wrap .fc-item:after{clear:both}}.fc-item__container{display:block;width:100%;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}@media (min-width: 46.25em){.has-flex-wrap .fc-item__container{-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-flex:1;-webkit-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto;width:0}}.fc-item__container,.item__container{position:relative}.fc-item__container:before,.item__container:before{content:'';position:absolute;top:0;left:0;right:0;height:0.0625rem;z-index:2}.fc-item--has-metadata .fc-item__content{padding-bottom:1.5rem}@media (min-width: 46.25em) and (max-width: 61.24em){.fc-slice--q-q-q-q .fc-item--has-timestamp .fc-item__content,.fc-slice--ql-ql-ql-ql .fc-item--has-timestamp .fc-item__content{padding-bottom:3rem}.fc-slice--q-q-q-q .fc-item--has-timestamp.fc-item--has-cutout .fc-item__content,.fc-slice--ql-ql-ql-ql .fc-item--has-timestamp.fc-item--has-cutout .fc-item__content{padding-bottom:1.5rem}}@media (max-width: 46.24em){.fc-item,.item{padding-left:0.625rem;padding-right:0.625rem;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}}@media (min-width: 46.25em){.fc-item,.item{padding-left:0;padding-right:0;margin-left:0.625rem;margin-right:0.625rem}}.fc-item a,.item a{color:#333;color:inherit}.u-faux-block-link .fc-item a.fc-item__link,.u-faux-block-link .fc-item abbr[title].fc-item__link,.fc-item .u-faux-block-link__promote.fc-item__link,.u-faux-block-link .item a.fc-item__link,.u-faux-block-link .item abbr[title].fc-item__link,.item .u-faux-block-link__promote.fc-item__link{z-index:0}@media (max-width: 61.24em){.u-faux-block-link .fc-item a,.u-faux-block-link .fc-item abbr[title],.fc-item .u-faux-block-link__promote,.u-faux-block-link .item a,.u-faux-block-link .item abbr[title],.item .u-faux-block-link__promote{z-index:initial}}.fc-item.fc-item--video .u-faux-block-link__overlay,.item.fc-item--video .u-faux-block-link__overlay{z-index:0}.fc-item.fc-item--video .u-faux-block-link__promote,.item.fc-item--video .u-faux-block-link__promote{z-index:1}.fc-item .u-faux-block-link--hover,.fc-item .fc-item__image-container,.item .u-faux-block-link--hover,.item .fc-item__image-container{background-color:#eaeaea}.fc-slice--nav-list--media .fc-item .u-faux-block-link--hover,.fc-slice--nav-list--media .fc-item .fc-item__image-container,.fc-slice--nav-list--media .item .u-faux-block-link--hover,.fc-slice--nav-list--media .item .fc-item__image-container{background-color:inherit}.fc-item .u-faux-block-link--hover .youtube-media-atom,.fc-item .u-faux-block-link--hover .fc-item__image-container,.item .u-faux-block-link--hover .youtube-media-atom,.item .u-faux-block-link--hover .fc-item__image-container{background-color:#000000;opacity:.9}.fc-item .u-faux-block-link--hover .u-faux-block-link__cta,.item .u-faux-block-link--hover .u-faux-block-link__cta{text-decoration:none}.fc-item .tone-colour,.fc-item .tone-colour:hover,.fc-item .tone-colour:active,.fc-item .tone-colour:visited,.item .tone-colour,.item .tone-colour:hover,.item .tone-colour:active,.item .tone-colour:visited{color:inherit}.fc-item .stars,.item .stars{display:block;white-space:nowrap;overflow:hidden;margin-top:0;margin-bottom:0;line-height:1}.fc-item .star__item,.item .star__item{margin-right:0;width:0.875rem;height:0.875rem}.fc-item .star__item--golden,.item .star__item--golden{fill:#ffce4b}.fc-item .star__item--grey,.item .star__item--grey{fill:#000000;opacity:.15}.fc-item .stars,.item .stars{margin-bottom:0;margin-top:.1em}.fc-item .stars .star__item,.item .stars .star__item{vertical-align:bottom}.fc-item .stars .star__item svg,.item .stars .star__item svg{height:.875em;width:.875em}.fc-item .gu-media-wrapper,.item .gu-media-wrapper{margin-bottom:0}.fc-item .vjs-big-play-button>.vjs-control-text,.item .vjs-big-play-button>.vjs-control-text{width:3.125rem;height:3.125rem;font-size:0.5625rem}.fc-item .vjs-big-play-button>.vjs-control-text:before,.item .vjs-big-play-button>.vjs-control-text:before{width:3.125rem;height:3.125rem;font-size:0.5625rem}.fc-item__title .inline-video-icon,.rich-link__title .inline-video-icon,.fc-sublink__link .inline-video-icon{fill:#fb0}.fc-item__title .inline-video-icon>svg,.rich-link__title .inline-video-icon>svg,.fc-sublink__link .inline-video-icon>svg{height:.75em;width:1.1em;margin-right:.3em}.fc-item--gallery .fc-item__title .inline-camera,.rich-link--gallery .rich-link__title .inline-camera,.fc-sublink--gallery .fc-sublink__link .inline-camera{fill:#fb0}.fc-item--gallery .fc-item__title .inline-camera svg,.rich-link--gallery .rich-link__title .inline-camera svg,.fc-sublink--gallery .fc-sublink__link .inline-camera svg{height:.72em;width:1.2em;margin-right:.1em}.fc-item--audio .fc-item__title .inline-volume-high,.rich-link--audio .rich-link__title .inline-volume-high,.fc-sublink--audio .fc-sublink__link .inline-volume-high{fill:#fb0}.fc-item--audio .fc-item__title .inline-volume-high svg,.rich-link--audio .rich-link__title .inline-volume-high svg,.fc-sublink--audio .fc-sublink__link .inline-volume-high svg{height:.72em;width:1.2em;margin-right:.1em}.fc-item__media-wrapper,.item__media-wrapper{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;position:relative}.fc-item__content{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}.fc-item__content,.fc-item__footer--horizontal{padding-left:0.3125rem;padding-right:0.3125rem}.fc-item__image-container{display:none}@media (max-width: 46.24em){.fc-item__slideshow picture:nth-child(1n+2) img{display:none}}@media (min-width: 46.25em){.fc-item__slideshow img{-webkit-animation-timing-function:linear;animation-timing-function:linear;-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite;-webkit-animation-direction:normal;animation-direction:normal;opacity:0}}@-webkit-keyframes fc-item__slideshow--2{0%{opacity:0}10%{opacity:1}50%{opacity:1}60%{opacity:0}}@keyframes fc-item__slideshow--2{0%{opacity:0}10%{opacity:1}50%{opacity:1}60%{opacity:0}}@media (min-width: 46.25em){.fc-item__slideshow--2 img{-webkit-animation-duration:10s;animation-duration:10s;-webkit-animation-name:fc-item__slideshow--2;animation-name:fc-item__slideshow--2}.fc-item__slideshow--2 picture:nth-child(2) img{-webkit-animation-delay:5s;animation-delay:5s}}@-webkit-keyframes fc-item__slideshow--3{0%{opacity:0}6.66667%{opacity:1}33.33333%{opacity:1}40%{opacity:0}}@keyframes fc-item__slideshow--3{0%{opacity:0}6.66667%{opacity:1}33.33333%{opacity:1}40%{opacity:0}}@media (min-width: 46.25em){.fc-item__slideshow--3 img{-webkit-animation-duration:15s;animation-duration:15s;-webkit-animation-name:fc-item__slideshow--3;animation-name:fc-item__slideshow--3}.fc-item__slideshow--3 picture:nth-child(2) img{-webkit-animation-delay:5s;animation-delay:5s}.fc-item__slideshow--3 picture:nth-child(3) img{-webkit-animation-delay:10s;animation-delay:10s}}@-webkit-keyframes fc-item__slideshow--4{0%{opacity:0}5%{opacity:1}25%{opacity:1}30%{opacity:0}}@keyframes fc-item__slideshow--4{0%{opacity:0}5%{opacity:1}25%{opacity:1}30%{opacity:0}}@media (min-width: 46.25em){.fc-item__slideshow--4 img{-webkit-animation-duration:20s;animation-duration:20s;-webkit-animation-name:fc-item__slideshow--4;animation-name:fc-item__slideshow--4}.fc-item__slideshow--4 picture:nth-child(2) img{-webkit-animation-delay:5s;animation-delay:5s}.fc-item__slideshow--4 picture:nth-child(3) img{-webkit-animation-delay:10s;animation-delay:10s}.fc-item__slideshow--4 picture:nth-child(4) img{-webkit-animation-delay:15s;animation-delay:15s}}@-webkit-keyframes fc-item__slideshow--5{0%{opacity:0}4%{opacity:1}20%{opacity:1}24%{opacity:0}}@keyframes fc-item__slideshow--5{0%{opacity:0}4%{opacity:1}20%{opacity:1}24%{opacity:0}}@media (min-width: 46.25em){.fc-item__slideshow--5 img{-webkit-animation-duration:25s;animation-duration:25s;-webkit-animation-name:fc-item__slideshow--5;animation-name:fc-item__slideshow--5}.fc-item__slideshow--5 picture:nth-child(2) img{-webkit-animation-delay:5s;animation-delay:5s}.fc-item__slideshow--5 picture:nth-child(3) img{-webkit-animation-delay:10s;animation-delay:10s}.fc-item__slideshow--5 picture:nth-child(4) img{-webkit-animation-delay:15s;animation-delay:15s}.fc-item__slideshow--5 picture:nth-child(5) img{-webkit-animation-delay:20s;animation-delay:20s}}.fc-item__video-play{display:block;z-index:1}.fc-item__live-indicator{color:#b51800}.fc-item__header,.item__title,.rich-link__header{font-size:1.25rem;line-height:1.5rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;font-weight:500;padding-bottom:.5em}.fc-item--has-boosted-title .fc-item__header,.fc-item--has-boosted-title .item__title,.fc-item--has-boosted-title .rich-link__header{font-size:1.5rem;line-height:1.75rem}.fc-item__title,.fc-item__byline,.fc-item__kicker,.rich-link__byline,.rich-link__title,.rich-link__kicker{font:inherit;line-height:inherit}.fc-item__title{padding-top:0.1875rem;padding-bottom:0;word-wrap:break-word}.fc-item__title .inline-external-link{fill:#1c6326}.fc-item__title .inline-external-link svg{width:1.2em;height:.75em;margin-right:.2em}.fc-item__title--quoted .inline-quote{fill:#767676}.fc-item__title--quoted .inline-quote svg{width:1.2em;height:.75em}.fc-item__kicker:after,.fc-sublink__kicker:after,.rich-link__kicker:after{content:'/';display:inline-block;margin-left:.2em;color:#d6d6d6}.fc-item__kicker:hover:after,.fc-sublink__kicker:hover:after,.rich-link__kicker:hover:after{text-decoration:none}.fc-item__kicker--dreamsnap{font-size:1.125rem;line-height:1.5rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:900;display:block;line-height:1.375rem;background-color:#e6e6e6;margin:0 -0.3125rem;padding:0.1875rem 0.3125rem}.fc-item__kicker--dreamsnap:hover:before{text-decoration:none}.fc-item__kicker--dreamsnap:after{display:none}.fc-item__kicker--dreamsnap-list{display:none}.fc-item__byline{margin-bottom:0}.fc-item__standfirst{font-size:0.875rem;line-height:1.125rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;padding-bottom:.5em;color:#767676;display:none}.fc-item--has-boosted-title .fc-item__standfirst{display:none !important}.fc-item__liveblog-blocks{display:none}@media (min-width: 61.25em){.fc-item__liveblog-blocks{display:block;-webkit-box-sizing:content-box !important;-moz-box-sizing:content-box !important;box-sizing:content-box !important;height:4.4375rem;overflow:hidden;border-bottom:0.3125rem solid transparent}}.fc-item__liveblog-blocks__inner{-webkit-transition:-webkit-transform .5s ease-in;transition:-webkit-transform .5s ease-in;transition:transform .5s ease-in;transition:transform .5s ease-in, -webkit-transform .5s ease-in}.fc-item__liveblog-blocks__inner--offset{-webkit-transform:translate3d(0, -4.4375rem, 0);transform:translate3d(0, -4.4375rem, 0)}.fc-item__liveblog-block{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;display:block;height:4.4375rem}.fc-item__liveblog-block:hover{text-decoration:none}.fc-item__liveblog-block__text{font-size:0.875rem;line-height:1.125rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;position:relative;overflow:hidden;line-height:1rem;color:#f9edeb;max-height:4.4375rem;padding:0.1875rem 0.375rem;border-top:0.0625rem solid #da8c80;border-bottom:0.25rem solid #cc2b12;background-color:#cc2b12}.fc-item__liveblog-block__text:after{font-size:0.875rem;line-height:1.125rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;content:'...';position:absolute;bottom:0;right:0;font-size:1.875rem;line-height:0.75rem;color:#f9edeb;height:1.125rem;padding-right:0.5rem;background-color:#cc2b12;-webkit-box-shadow:-0.3125rem 0 0.3125rem -0.125rem #cc2b12;box-shadow:-0.3125rem 0 0.3125rem -0.125rem #cc2b12}.fc-item__liveblog-block__time{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-weight:bold;color:#ffffff}.fc-item__meta{font-size:0.75rem;line-height:1rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;position:absolute;bottom:0;left:0.3125rem;right:0.3125rem;color:#767676}.fc-item__meta .inline-icon{fill:#bdbdbd}.fc-item__meta a,.fc-item__meta button{z-index:1 !important}.fc-item__timestamp,.fc-trail__count{position:relative;float:left;margin-bottom:0.1875rem;margin-right:1em}.fc-item__timestamp{margin-right:1em;padding-left:0}.fc-item__timestamp .inline-icon{margin:0;top:0.0625rem;position:relative;height:0.6875rem;width:0.6875rem;margin-right:0.125rem}@media (min-width: 46.25em) and (max-width: 61.24em){.fc-slice--ql-ql-ql-ql .fc-item__timestamp,.fc-slice--q-q-q-q .fc-item__timestamp{display:block;float:none}}.fc-trail__count .inline-icon{width:1rem;height:1rem;position:relative;top:0.1875rem;float:left;margin-right:0.0625rem}.fc-trail__count--inline-template{display:none}.fc-item--has-cutout .fc-item__media-wrapper{display:none !important}.fc-item__footer--vertical{clear:left}.fc-item__footer--horizontal{display:none}.has-no-flex-wrap .fc-item__footer--horizontal:after,.has-no-flex-wrap .fc-item__footer--horizontal:before{content:'';display:table}.has-no-flex-wrap .fc-item__footer--horizontal:after{clear:both}.fc-item__avatar{position:absolute;overflow:hidden;width:100%;bottom:0;right:0}.fc-item__avatar__media{position:absolute;height:100%;bottom:0;right:0}.fc-item__avatar__media .responsive-img{position:absolute;height:100%;bottom:0;right:0}.fc-item__avatar__media.image--portrait{top:0;height:auto;width:80%}.fc-item__avatar__media.image--portrait .responsive-img{position:absolute;height:auto;width:100%;bottom:auto}.fc-item__link:visited,.fc-sublink__link:visited{color:#5c5c5c}.fc-item__link:hover,.fc-item__link:focus{text-decoration:none}.fc-item__link:hover .fc-item__headline,.fc-item__link:focus .fc-item__headline{text-decoration:underline}.fc-slice__item{width:100%;position:relative;padding-bottom:0;margin-bottom:0.75rem}@media (min-width: 46.25em){.has-flex .fc-slice__item:not(.fc-slice__item--mpu-candidate){display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex}}@media (min-width: 20em){.fc-slice__item{float:none}}.fc-slice__item+.fc-slice__item:before{content:'';display:block;position:absolute;top:0;bottom:0;left:0;width:0.0625rem;height:100%;border-left:0.0625rem solid #dfdfdf}.fc-slice__item+.fc-slice__item--no-mpu:before{border-left:0 !important}.fc-slice__item.l-list__item{margin-bottom:0;padding-bottom:0.75rem}.fc-slice__item--no-mpu{-webkit-box-flex:0 !important;-webkit-flex:0 !important;-ms-flex:0 !important;flex:0 !important}@media (max-width: 46.24em){.fc-item--list-mobile .fc-item__header{font-size:1rem;line-height:1.25rem}.fc-item--has-boosted-title .fc-item--list-mobile .fc-item__header{font-size:1.25rem;line-height:1.5rem}.fc-item--list-mobile .fc-item__media-wrapper{display:none}.fc-item--list-mobile.fc-item--has-cutout .fc-item__avatar__media{display:none}.fc-item--list-mobile .fc-item__kicker--dreamsnap{display:none}.fc-item--list-mobile .fc-item__kicker--dreamsnap-list{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:900;display:block;margin:0}.fc-item--list-mobile .fc-item__video-play{display:none}}@media (min-width: 46.25em){.fc-item--list-tablet .fc-item__header{font-size:1rem;line-height:1.25rem}.fc-item--has-boosted-title .fc-item--list-tablet .fc-item__header{font-size:1.25rem;line-height:1.5rem}.fc-item--list-tablet .fc-item__media-wrapper{display:none}.fc-item--list-tablet.fc-item--has-cutout .fc-item__avatar__media{display:none}.fc-item--list-tablet .fc-item__kicker--dreamsnap{display:none}.fc-item--list-tablet .fc-item__kicker--dreamsnap-list{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:900;display:block;margin:0}}@media (min-width: 46.25em){.fc-item--list-compact-tablet .fc-item__header{font-size:1rem;line-height:1.25rem}.fc-item--has-boosted-title .fc-item--list-compact-tablet .fc-item__header{font-size:1.25rem;line-height:1.5rem}.fc-item--list-compact-tablet .fc-item__media-wrapper{display:none}.fc-item--list-compact-tablet.fc-item--has-cutout .fc-item__avatar__media{display:none}.fc-item--list-compact-tablet .fc-item__kicker--dreamsnap{display:none}.fc-item--list-compact-tablet .fc-item__kicker--dreamsnap-list{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:900;display:block;margin:0}.fc-item--list-compact-tablet .fc-item__header{padding-bottom:0}}@media (max-width: 46.24em){.fc-item--list-media-mobile .fc-item__header{font-size:1rem;line-height:1.25rem}.fc-item--has-boosted-title .fc-item--list-media-mobile .fc-item__header{font-size:1.25rem;line-height:1.5rem}.fc-item--list-media-mobile .fc-item__media-wrapper{display:none}.fc-item--list-media-mobile.fc-item--has-cutout .fc-item__avatar__media{display:none}.fc-item--list-media-mobile .fc-item__kicker--dreamsnap{display:none}.fc-item--list-media-mobile .fc-item__kicker--dreamsnap-list{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:900;display:block;margin:0}.fc-item--list-media-mobile .fc-item__content{min-height:5.25rem;position:relative}.fc-item--list-media-mobile.fc-item--has-metadata .fc-item__content{padding-bottom:0.875rem}}@media (max-width: 46.24em) and (min-width: 46.25em){.fc-item--list-media-mobile .fc-item__content{min-height:4.75rem}}@media (max-width: 46.24em){.fc-item--list-media-mobile .fc-item__container,.fc-item--list-media-mobile .fc-item__content,.fc-item--list-media-mobile .fc-item__footer,.fc-item--list-media-mobile .fc-item__image-container{display:block}.fc-item--list-media-mobile.fc-item{padding-bottom:0 !important}.fc-item--list-media-mobile.fc-item--has-image{position:relative}.fc-item--list-media-mobile.fc-item--has-image:before{content:'';position:absolute;left:0;top:0;bottom:0;width:7.91667rem}.fc-item--list-media-mobile.fc-item--has-image .fc-item__container{padding-left:8.16667rem}}@media (max-width: 46.24em) and (min-width: 46.25em){.fc-item--list-media-mobile.fc-item--has-image .fc-item__container{padding-left:7.91667rem}}@media (max-width: 46.24em){.fc-item--list-media-mobile .fc-item__header{font-size:1rem;line-height:1.25rem}.fc-item--has-boosted-title .fc-item--list-media-mobile .fc-item__header{font-size:1.25rem;line-height:1.5rem}.fc-item--list-media-mobile .fc-item__media-wrapper,.fc-item--list-media-mobile .fc-item__image-container{display:block}.fc-item--list-media-mobile .fc-item__media-wrapper{position:absolute;margin-left:-7.91667rem;width:7.91667rem;margin-top:0.25rem;margin-bottom:0.25rem}}@media (max-width: 46.24em) and (min-width: 46.25em){.fc-item--list-media-mobile .fc-item__media-wrapper{margin-top:0;margin-bottom:0}}@media (max-width: 46.24em){.fc-item--list-media-mobile .fc-item__kicker--dreamsnap-list{margin-left:-8.16667rem}}@media (max-width: 46.24em) and (min-width: 46.25em){.fc-item--list-media-mobile .fc-item__kicker--dreamsnap-list{margin-left:-7.91667rem}}@media (max-width: 46.24em){.fc-item--list-media-mobile[class*='fc-item--has-sublinks'] .fc-item__media-wrapper{position:relative;float:left}.fc-item--list-media-mobile.fc-item--has-no-image .fc-item__container,.fc-item--list-media-mobile.fc-item--has-cutout .fc-item__container{padding-left:0}.fc-item--list-media-mobile.fc-item--has-no-image .fc-item__meta,.fc-item--list-media-mobile.fc-item--has-cutout .fc-item__meta{margin-left:0}.fc-item--list-media-mobile.fc-item--has-no-image .fc-item__footer--vertical,.fc-item--list-media-mobile.fc-item--has-cutout .fc-item__footer--vertical{margin-left:0}.fc-item--list-media-mobile.fc-item--has-cutout .fc-item__media-wrapper{display:none}.fc-item--list-media-mobile .fc-item__footer--vertical,.fc-item--list-media-mobile[class*='fc-item--has-sublinks'] .fc-item__meta{margin-left:-8.16667rem}.fc-item--list-media-mobile.fc-item--has-cutout .fc-item__kicker--dreamsnap-list{margin-left:0}.fc-item--list-media-mobile.fc-item--has-cutout .fc-item__content{min-height:6rem;padding-right:3.75rem}.fc-item--list-media-mobile.fc-item--has-cutout .fc-item__avatar{height:6rem}.fc-item--list-media-mobile.fc-item--has-cutout .fc-item__avatar .fc-item__avatar__media{display:block;right:-1.25rem}.fc-item--list-media-mobile .fc-item__video-play{display:none !important}}@media (min-width: 46.25em){.fc-item--list-media-tablet .fc-item__header{font-size:1rem;line-height:1.25rem}.fc-item--has-boosted-title .fc-item--list-media-tablet .fc-item__header{font-size:1.25rem;line-height:1.5rem}.fc-item--list-media-tablet .fc-item__media-wrapper{display:none}.fc-item--list-media-tablet.fc-item--has-cutout .fc-item__avatar__media{display:none}.fc-item--list-media-tablet .fc-item__kicker--dreamsnap{display:none}.fc-item--list-media-tablet .fc-item__kicker--dreamsnap-list{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:900;display:block;margin:0}.fc-item--list-media-tablet .fc-item__content{min-height:5.75rem;position:relative}.fc-item--list-media-tablet.fc-item--has-metadata .fc-item__content{padding-bottom:0.875rem}}@media (min-width: 46.25em) and (min-width: 46.25em){.fc-item--list-media-tablet .fc-item__content{min-height:5.25rem}}@media (min-width: 46.25em){.fc-item--list-media-tablet .fc-item__container,.fc-item--list-media-tablet .fc-item__content,.fc-item--list-media-tablet .fc-item__footer,.fc-item--list-media-tablet .fc-item__image-container{display:block}.fc-item--list-media-tablet.fc-item{padding-bottom:0 !important}.fc-item--list-media-tablet.fc-item--has-image{position:relative}.fc-item--list-media-tablet.fc-item--has-image:before{content:'';position:absolute;left:0;top:0;bottom:0;width:8.75rem}.fc-item--list-media-tablet.fc-item--has-image .fc-item__container{padding-left:9rem}}@media (min-width: 46.25em) and (min-width: 46.25em){.fc-item--list-media-tablet.fc-item--has-image .fc-item__container{padding-left:8.75rem}}@media (min-width: 46.25em){.fc-item--list-media-tablet .fc-item__header{font-size:1rem;line-height:1.25rem}.fc-item--has-boosted-title .fc-item--list-media-tablet .fc-item__header{font-size:1.25rem;line-height:1.5rem}.fc-item--list-media-tablet .fc-item__media-wrapper,.fc-item--list-media-tablet .fc-item__image-container{display:block}.fc-item--list-media-tablet .fc-item__media-wrapper{position:absolute;margin-left:-8.75rem;width:8.75rem;margin-top:0.25rem;margin-bottom:0.25rem}}@media (min-width: 46.25em) and (min-width: 46.25em){.fc-item--list-media-tablet .fc-item__media-wrapper{margin-top:0;margin-bottom:0}}@media (min-width: 46.25em){.fc-item--list-media-tablet .fc-item__kicker--dreamsnap-list{margin-left:-9rem}}@media (min-width: 46.25em) and (min-width: 46.25em){.fc-item--list-media-tablet .fc-item__kicker--dreamsnap-list{margin-left:-8.75rem}}@media (min-width: 46.25em){.fc-item--list-media-tablet[class*='fc-item--has-sublinks'] .fc-item__media-wrapper{position:relative;float:left}.fc-item--list-media-tablet.fc-item--has-no-image .fc-item__container,.fc-item--list-media-tablet.fc-item--has-cutout .fc-item__container{padding-left:0}.fc-item--list-media-tablet.fc-item--has-no-image .fc-item__meta,.fc-item--list-media-tablet.fc-item--has-cutout .fc-item__meta{margin-left:0}.fc-item--list-media-tablet.fc-item--has-no-image .fc-item__footer--vertical,.fc-item--list-media-tablet.fc-item--has-cutout .fc-item__footer--vertical{margin-left:0}.fc-item--list-media-tablet.fc-item--has-cutout .fc-item__media-wrapper{display:none}.fc-item--list-media-tablet .fc-item__footer--vertical,.fc-item--list-media-tablet[class*='fc-item--has-sublinks'] .fc-item__meta{margin-left:-9rem}.fc-item--list-media-tablet.fc-item--has-cutout .fc-item__kicker--dreamsnap-list{margin-left:0}.fc-item--list-media-tablet.fc-item--has-cutout .fc-item__content{min-height:6rem;padding-right:3.75rem}.fc-item--list-media-tablet.fc-item--has-cutout .fc-item__avatar{height:6rem}.fc-item--list-media-tablet.fc-item--has-cutout .fc-item__avatar .fc-item__avatar__media{display:block;right:-1.25rem}.fc-item--list-media-tablet .fc-item__video-play{display:none !important}}@media (max-width: 46.24em){.fc-item--standard-mobile .fc-item__image-container{display:block}.fc-item--standard-mobile.fc-item--has-sublinks-1 .fc-item__media-wrapper{display:block}.fc-item--standard-mobile.fc-item--has-cutout .fc-item__media-wrapper{display:none}.fc-item--standard-mobile.fc-item--has-cutout .fc-item__header,.fc-item--standard-mobile.fc-item--has-cutout .fc-sublinks{padding-right:25%}.has-flex-wrap .fc-item--standard-mobile[class*='fc-item--has-sublinks'].fc-item--has-cutout .fc-item__header{padding-right:0}.has-flex-wrap .fc-item--standard-mobile[class*='fc-item--has-sublinks'].fc-item--has-cutout .fc-sublinks{min-height:9rem}.fc-item--standard-mobile .fc-item__avatar{height:6.75rem}.fc-item--standard-mobile .fc-item__avatar__media{right:-1.25rem}}@media (min-width: 46.25em){.fc-item--standard-tablet .fc-item__image-container{display:block}.fc-item--standard-tablet.fc-item--has-sublinks-1 .fc-item__media-wrapper{display:block}.fc-item--standard-tablet.fc-item--has-cutout .fc-item__media-wrapper{display:none}}@media (min-width: 46.25em) and (max-width: 61.24em){.fc-item--standard-tablet .fc-item__header{font-size:1rem;line-height:1.25rem}.fc-item--has-boosted-title .fc-item--standard-tablet .fc-item__header{font-size:1.25rem;line-height:1.5rem}}@media (min-width: 46.25em){.fc-item--standard-tablet[class*='fc-item--has-sublinks'] .fc-item__standfirst{display:none}.fc-item--standard-tablet.fc-item--has-sublinks-1 .fc-item__media-wrapper{display:block}.fc-item--standard-tablet.fc-item--has-cutout .fc-item__container{padding-bottom:10.5rem}.fc-item--standard-tablet .fc-item__avatar{height:11.25rem}.fc-item--standard-tablet .fc-item__avatar__media{right:-40%}}@media (max-width: 61.24em){.fc-item--standard-tablet.fc-item--video .fc-item__video-play{display:none}.fc-item--standard-tablet.fc-item--video .fc-item__video-fallback{display:block}}@media (min-width: 61.25em){.fc-item--standard-tablet.fc-item--has-cutout .fc-item__container{padding-bottom:9.75rem}.fc-item--standard-tablet .fc-item__avatar__media{right:-20%}}@media (min-width: 46.25em){.fc-item--third-tablet .fc-item__image-container{display:block}.fc-item--third-tablet.fc-item--has-sublinks-1 .fc-item__media-wrapper{display:block}.fc-item--third-tablet.fc-item--has-cutout .fc-item__media-wrapper{display:none}.fc-item--third-tablet.fc-item--has-cutout .fc-item__container{padding-bottom:8.25rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--third-tablet.fc-item--has-cutout[class*='fc-item--has-sublinks'] .fc-item__container{padding-bottom:0}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--third-tablet.fc-item--has-cutout .fc-sublinks{padding-right:8.75rem}}@media (min-width: 46.25em){.fc-item--third-tablet .fc-item__avatar{height:9.75rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--third-tablet .fc-item__avatar{height:11.25rem}}@media (min-width: 46.25em){.fc-item--third-tablet .fc-item__avatar__media{right:-20%}}@media (min-width: 46.25em){.fc-item--half-tablet .fc-item__header{font-size:1.5rem;line-height:1.75rem}.fc-item--has-boosted-title .fc-item--half-tablet .fc-item__header{font-size:1.75rem;line-height:2rem}}@media (min-width: 46.25em) and (min-width: 46.25em) and (max-width: 61.24em){.fc-item--half-tablet .fc-item__header{font-size:1.25rem;line-height:1.5rem}.fc-item--has-boosted-title .fc-item--half-tablet .fc-item__header{font-size:1.5rem;line-height:1.75rem}}@media (min-width: 46.25em){.fc-item--half-tablet .fc-item__image-container{display:block}.fc-item--half-tablet.fc-item--has-cutout .fc-item__container{padding-bottom:3.75rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--half-tablet.fc-item--has-cutout .fc-item__container{padding-bottom:8.25rem}}@media (min-width: 46.25em){.fc-item--half-tablet.fc-item--has-cutout .fc-item__standfirst{display:block}.fc-item--half-tablet.fc-item--has-cutout .fc-item__standfirst,.fc-item--half-tablet.fc-item--has-cutout .fc-sublinks{padding-right:11.25rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--half-tablet.fc-item--has-cutout .fc-item__standfirst,.fc-item--half-tablet.fc-item--has-cutout .fc-sublinks{padding-right:13.75rem}}@media (min-width: 46.25em){.fc-item--half-tablet .fc-item__standfirst{display:block}.fc-item--half-tablet .fc-item__avatar{height:20.25rem}.fc-item--half-tablet .fc-item__avatar{height:14.25rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--half-tablet .fc-item__avatar{height:17.25rem}}@media (min-width: 46.25em){.fc-item--half-tablet .fc-item__avatar__media{right:-15%}.fc-item--half-tablet[class*='fc-item--has-sublinks'] .fc-item__standfirst{display:none}.has-flex-wrap .fc-item--half-tablet[class*='fc-item--has-sublinks'].fc-item--has-cutout .fc-item__content{-webkit-box-flex:0;-webkit-flex:0 1 auto;-ms-flex:0 1 auto;flex:0 1 auto}.has-flex-wrap .fc-item--half-tablet:not(.fc-item--has-cutout) .fc-sublinks{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex}.has-flex-wrap .fc-item--half-tablet:not(.fc-item--has-cutout) .fc-sublink{-webkit-box-flex:1;-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%}.has-flex-wrap .fc-item--half-tablet:not(.fc-item--has-cutout) .fc-sublink+*{margin-left:1.25rem}.has-no-flex-wrap .fc-item--half-tablet:not(.fc-item--has-cutout) .fc-sublinks{display:table;table-layout:fixed;width:100%}.has-no-flex-wrap .fc-item--half-tablet:not(.fc-item--has-cutout) .fc-sublink{display:table-cell;padding-right:1.25rem}.has-no-flex-wrap .fc-item--half-tablet:not(.fc-item--has-cutout) .fc-sublink:last-child{padding-right:0}.fc-item--half-tablet .fc-item__footer--horizontal{-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--half-tablet .vjs-big-play-button>.vjs-control-text{width:4.375rem;height:4.375rem;font-size:0.75rem}.fc-item--half-tablet .vjs-big-play-button>.vjs-control-text:before{width:4.375rem;height:4.375rem;font-size:0.75rem}}@media (min-width: 46.25em){.fc-item--three-quarters-tablet .fc-item__image-container{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-left:0.3125rem}.fc-item--three-quarters-tablet .fc-item__content{position:relative}.fc-item--three-quarters-tablet .fc-item__content>*{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-right:0.9375rem}.has-flex-wrap .fc-item--three-quarters-tablet .fc-item__container{-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-orient:horizontal;-webkit-box-direction:reverse;-webkit-flex-direction:row-reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse}.has-flex-wrap .fc-item--three-quarters-tablet .fc-item__media-wrapper{-webkit-flex-basis:65.5%;-ms-flex-preferred-size:65.5%;flex-basis:65.5%}.has-flex-wrap .fc-item--three-quarters-tablet .fc-item__video-fallback{-webkit-flex-basis:65.5%;-ms-flex-preferred-size:65.5%;flex-basis:65.5%}.has-flex-wrap .fc-item--three-quarters-tablet .fc-item__content{-webkit-flex-basis:34.5%;-ms-flex-preferred-size:34.5%;flex-basis:34.5%;max-width:34.5%}.has-flex-wrap .fc-item--three-quarters-tablet .fc-item__footer--horizontal{-webkit-flex-basis:100%;-ms-flex-preferred-size:100%;flex-basis:100%}.has-no-flex-wrap .fc-item--three-quarters-tablet .fc-item__media-wrapper{width:65.5%;float:right}.has-no-flex-wrap .fc-item--three-quarters-tablet .fc-item__content{width:34.5%}.fc-item--three-quarters-tablet.fc-item--has-no-image .fc-item__content{-webkit-flex-basis:100%;-ms-flex-preferred-size:100%;flex-basis:100%;max-width:100%;padding-right:13.75rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--three-quarters-tablet .fc-item__header{font-size:1.5rem;line-height:1.75rem}.fc-item--has-boosted-title .fc-item--three-quarters-tablet .fc-item__header{font-size:1.75rem;line-height:2rem}}@media (min-width: 46.25em){.fc-item--three-quarters-tablet .fc-item__image-container{display:block}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--three-quarters-tablet .fc-item__standfirst{display:block}}@media (min-width: 46.25em){.fc-item--three-quarters-tablet .fc-item__liveblog-blocks{padding-right:0}.fc-item--three-quarters-tablet.fc-item--has-no-image .fc-item__standfirst{display:block}.fc-item--three-quarters-tablet.fc-item--has-cutout .fc-item__container{min-height:20.25rem}.has-flex-wrap .fc-item--three-quarters-tablet.fc-item--has-cutout .fc-item__container{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row}.fc-item--three-quarters-tablet.fc-item--has-cutout .fc-item__header{font-size:1.75rem;line-height:2rem}.fc-item--has-boosted-title .fc-item--three-quarters-tablet.fc-item--has-cutout .fc-item__header{font-size:2rem;line-height:2.25rem}.fc-item--three-quarters-tablet.fc-item--has-cutout .fc-item__content{width:auto;max-width:23.75rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--three-quarters-tablet.fc-item--has-cutout .fc-item__content{max-width:28.75rem}}@media (min-width: 46.25em){.has-flex-wrap .fc-item--three-quarters-tablet.fc-item--has-cutout .fc-item__content{-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto}.fc-item--three-quarters-tablet .fc-item__avatar{height:17.25rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--three-quarters-tablet .fc-item__avatar{height:20.25rem}}@media (min-width: 46.25em){.fc-item--three-quarters-tablet .fc-item__avatar__media{right:-12%}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--three-quarters-tablet .fc-item__avatar__media{right:-12%}}@media (min-width: 46.25em){.fc-item--three-quarters-tablet .vjs-big-play-button>.vjs-control-text{width:4.375rem;height:4.375rem;font-size:0.75rem}.fc-item--three-quarters-tablet .vjs-big-play-button>.vjs-control-text:before{width:4.375rem;height:4.375rem;font-size:0.75rem}.fc-item--three-quarters-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-item__footer--vertical{display:none}.fc-item--three-quarters-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-item__footer--horizontal{display:block;clear:both}.has-flex-wrap .fc-item--three-quarters-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-sublinks{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex}.has-flex-wrap .fc-item--three-quarters-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-sublink{-webkit-box-flex:1;-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%}.has-flex-wrap .fc-item--three-quarters-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-sublink+*{margin-left:1.25rem}.has-no-flex-wrap .fc-item--three-quarters-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-sublinks{display:table;table-layout:fixed;width:100%}.has-no-flex-wrap .fc-item--three-quarters-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-sublink{display:table-cell;padding-right:1.25rem}.has-no-flex-wrap .fc-item--three-quarters-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-sublink:last-child{padding-right:0}}@media (min-width: 46.25em){.fc-item--three-quarters-right-tablet .fc-item__image-container{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-left:0.3125rem}.fc-item--three-quarters-right-tablet .fc-item__content{position:relative}.fc-item--three-quarters-right-tablet .fc-item__content>*{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-right:0.9375rem}.has-flex-wrap .fc-item--three-quarters-right-tablet .fc-item__container{-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-orient:horizontal;-webkit-box-direction:reverse;-webkit-flex-direction:row-reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse}.has-flex-wrap .fc-item--three-quarters-right-tablet .fc-item__media-wrapper{-webkit-flex-basis:65.5%;-ms-flex-preferred-size:65.5%;flex-basis:65.5%}.has-flex-wrap .fc-item--three-quarters-right-tablet .fc-item__video-fallback{-webkit-flex-basis:65.5%;-ms-flex-preferred-size:65.5%;flex-basis:65.5%}.has-flex-wrap .fc-item--three-quarters-right-tablet .fc-item__content{-webkit-flex-basis:34.5%;-ms-flex-preferred-size:34.5%;flex-basis:34.5%;max-width:34.5%}.has-flex-wrap .fc-item--three-quarters-right-tablet .fc-item__footer--horizontal{-webkit-flex-basis:100%;-ms-flex-preferred-size:100%;flex-basis:100%}.has-no-flex-wrap .fc-item--three-quarters-right-tablet .fc-item__media-wrapper{width:65.5%;float:right}.has-no-flex-wrap .fc-item--three-quarters-right-tablet .fc-item__content{width:34.5%}.fc-item--three-quarters-right-tablet.fc-item--has-no-image .fc-item__content{-webkit-flex-basis:100%;-ms-flex-preferred-size:100%;flex-basis:100%;max-width:100%;padding-right:13.75rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--three-quarters-right-tablet .fc-item__header{font-size:1.5rem;line-height:1.75rem}.fc-item--has-boosted-title .fc-item--three-quarters-right-tablet .fc-item__header{font-size:1.75rem;line-height:2rem}}@media (min-width: 46.25em){.fc-item--three-quarters-right-tablet .fc-item__image-container{display:block}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--three-quarters-right-tablet .fc-item__standfirst{display:block}}@media (min-width: 46.25em){.fc-item--three-quarters-right-tablet .fc-item__liveblog-blocks{padding-right:0}.fc-item--three-quarters-right-tablet.fc-item--has-no-image .fc-item__standfirst{display:block}.fc-item--three-quarters-right-tablet.fc-item--has-cutout .fc-item__container{min-height:20.25rem}.has-flex-wrap .fc-item--three-quarters-right-tablet.fc-item--has-cutout .fc-item__container{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row}.fc-item--three-quarters-right-tablet.fc-item--has-cutout .fc-item__header{font-size:1.75rem;line-height:2rem}.fc-item--has-boosted-title .fc-item--three-quarters-right-tablet.fc-item--has-cutout .fc-item__header{font-size:2rem;line-height:2.25rem}.fc-item--three-quarters-right-tablet.fc-item--has-cutout .fc-item__content{width:auto;max-width:23.75rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--three-quarters-right-tablet.fc-item--has-cutout .fc-item__content{max-width:28.75rem}}@media (min-width: 46.25em){.has-flex-wrap .fc-item--three-quarters-right-tablet.fc-item--has-cutout .fc-item__content{-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto}.fc-item--three-quarters-right-tablet .fc-item__avatar{height:17.25rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--three-quarters-right-tablet .fc-item__avatar{height:20.25rem}}@media (min-width: 46.25em){.fc-item--three-quarters-right-tablet .fc-item__avatar__media{right:-12%}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--three-quarters-right-tablet .fc-item__avatar__media{right:-12%}}@media (min-width: 46.25em){.fc-item--three-quarters-right-tablet .vjs-big-play-button>.vjs-control-text{width:4.375rem;height:4.375rem;font-size:0.75rem}.fc-item--three-quarters-right-tablet .vjs-big-play-button>.vjs-control-text:before{width:4.375rem;height:4.375rem;font-size:0.75rem}.fc-item--three-quarters-right-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-item__footer--vertical{display:none}.fc-item--three-quarters-right-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-item__footer--horizontal{display:block;clear:both}.has-flex-wrap .fc-item--three-quarters-right-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-sublinks{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex}.has-flex-wrap .fc-item--three-quarters-right-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-sublink{-webkit-box-flex:1;-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%}.has-flex-wrap .fc-item--three-quarters-right-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-sublink+*{margin-left:1.25rem}.has-no-flex-wrap .fc-item--three-quarters-right-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-sublinks{display:table;table-layout:fixed;width:100%}.has-no-flex-wrap .fc-item--three-quarters-right-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-sublink{display:table-cell;padding-right:1.25rem}.has-no-flex-wrap .fc-item--three-quarters-right-tablet.fc-item--has-sublinks-3:not(.fc-item--has-cutout) .fc-sublink:last-child{padding-right:0}.has-flex-wrap .fc-item--three-quarters-right-tablet .fc-item__container{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row}.fc-item--three-quarters-right-tablet .fc-item__content>*{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-right:0;padding-left:0.9375rem}.has-no-flex-wrap .fc-item--three-quarters-right-tablet .fc-item__media-wrapper{float:left}.has-no-flex-wrap .fc-item--three-quarters-right-tablet .fc-item__content{float:right}.fc-item--three-quarters-right-tablet.fc-item--has-cutout .fc-item__content{float:left}.fc-item--three-quarters-right-tablet.fc-item--has-cutout .fc-item__content>*{padding-left:0}}@media (min-width: 46.25em){.fc-item--three-quarters-tall-tablet .fc-item__image-container{display:block}.fc-item--three-quarters-tall-tablet.fc-item--has-sublinks-1 .fc-item__media-wrapper{display:block}.fc-item--three-quarters-tall-tablet.fc-item--has-cutout .fc-item__media-wrapper{display:none}.fc-item--three-quarters-tall-tablet .fc-item__image-container{display:block}.fc-item--three-quarters-tall-tablet .fc-item__header{font-size:1.25rem;line-height:1.5rem}.fc-item--has-boosted-title .fc-item--three-quarters-tall-tablet .fc-item__header{font-size:1.5rem;line-height:1.75rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--three-quarters-tall-tablet .fc-item__header{font-size:1.75rem;line-height:2rem}.fc-item--has-boosted-title .fc-item--three-quarters-tall-tablet .fc-item__header{font-size:2rem;line-height:2.25rem}}@media (min-width: 46.25em){.fc-item--three-quarters-tall-tablet .fc-item__standfirst{display:block;width:66%}.has-flex-wrap .fc-item--three-quarters-tall-tablet:not(.fc-item--has-cutout) .fc-sublinks{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex}.has-flex-wrap .fc-item--three-quarters-tall-tablet:not(.fc-item--has-cutout) .fc-sublink{-webkit-box-flex:1;-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%}.has-flex-wrap .fc-item--three-quarters-tall-tablet:not(.fc-item--has-cutout) .fc-sublink+*{margin-left:1.25rem}.has-no-flex-wrap .fc-item--three-quarters-tall-tablet:not(.fc-item--has-cutout) .fc-sublinks{display:table;table-layout:fixed;width:100%}.has-no-flex-wrap .fc-item--three-quarters-tall-tablet:not(.fc-item--has-cutout) .fc-sublink{display:table-cell;padding-right:1.25rem}.has-no-flex-wrap .fc-item--three-quarters-tall-tablet:not(.fc-item--has-cutout) .fc-sublink:last-child{padding-right:0}}@media (min-width: 46.25em){.fc-item--full-media-50-tablet .fc-item__image-container{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-left:0.3125rem}.fc-item--full-media-50-tablet .fc-item__content{position:relative}.fc-item--full-media-50-tablet .fc-item__content>*{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-right:0.9375rem}.has-flex-wrap .fc-item--full-media-50-tablet .fc-item__container{-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-orient:horizontal;-webkit-box-direction:reverse;-webkit-flex-direction:row-reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse}.has-flex-wrap .fc-item--full-media-50-tablet .fc-item__media-wrapper{-webkit-flex-basis:50%;-ms-flex-preferred-size:50%;flex-basis:50%}.has-flex-wrap .fc-item--full-media-50-tablet .fc-item__video-fallback{-webkit-flex-basis:50%;-ms-flex-preferred-size:50%;flex-basis:50%}.has-flex-wrap .fc-item--full-media-50-tablet .fc-item__content{-webkit-flex-basis:50%;-ms-flex-preferred-size:50%;flex-basis:50%;max-width:50%}.has-flex-wrap .fc-item--full-media-50-tablet .fc-item__footer--horizontal{-webkit-flex-basis:100%;-ms-flex-preferred-size:100%;flex-basis:100%}.has-no-flex-wrap .fc-item--full-media-50-tablet .fc-item__media-wrapper{width:50%;float:right}.has-no-flex-wrap .fc-item--full-media-50-tablet .fc-item__content{width:50%}.fc-item--full-media-50-tablet.fc-item--has-no-image .fc-item__content{-webkit-flex-basis:100%;-ms-flex-preferred-size:100%;flex-basis:100%;max-width:100%;padding-right:13.75rem}.fc-item--full-media-50-tablet .fc-item__header{font-size:1.25rem;line-height:1.5rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--full-media-50-tablet .fc-item__header{font-size:1.75rem;line-height:2rem}.fc-item--has-boosted-title .fc-item--full-media-50-tablet .fc-item__header{font-size:2rem;line-height:2.25rem}}@media (min-width: 46.25em){.fc-item--full-media-50-tablet .fc-item__standfirst,.fc-item--full-media-50-tablet .fc-item__image-container{display:block}.fc-item--full-media-50-tablet.fc-item--has-no-image .fc-item__standfirst{display:block}.fc-item--full-media-50-tablet .fc-item__footer{clear:left}.fc-item--full-media-50-tablet.fc-item--has-sublinks-3 .fc-item__standfirst{display:none}.fc-item--full-media-50-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-item__footer--vertical{display:none}.fc-item--full-media-50-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-item__footer--horizontal{display:block;clear:both}.has-flex-wrap .fc-item--full-media-50-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-sublinks{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex}.has-flex-wrap .fc-item--full-media-50-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-sublink{-webkit-box-flex:1;-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%}.has-flex-wrap .fc-item--full-media-50-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-sublink+*{margin-left:1.25rem}.has-no-flex-wrap .fc-item--full-media-50-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-sublinks{display:table;table-layout:fixed;width:100%}.has-no-flex-wrap .fc-item--full-media-50-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-sublink{display:table-cell;padding-right:1.25rem}.has-no-flex-wrap .fc-item--full-media-50-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-sublink:last-child{padding-right:0}.fc-item--full-media-50-tablet.fc-item--has-cutout .fc-item__container{min-height:16.5rem}.has-flex-wrap .fc-item--full-media-50-tablet.fc-item--has-cutout .fc-item__container{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row}.fc-item--full-media-50-tablet.fc-item--has-cutout .fc-item__content{width:auto;max-width:28.75rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--full-media-50-tablet.fc-item--has-cutout .fc-item__content{max-width:38.75rem}}@media (min-width: 46.25em){.has-flex-wrap .fc-item--full-media-50-tablet.fc-item--has-cutout .fc-item__content{-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto}.fc-item--full-media-50-tablet.fc-item--has-cutout .fc-item__header{font-size:1.5rem;line-height:1.75rem}.fc-item--has-boosted-title .fc-item--full-media-50-tablet.fc-item--has-cutout .fc-item__header{font-size:1.75rem;line-height:2rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--full-media-50-tablet.fc-item--has-cutout .fc-item__header{font-size:2rem;line-height:2.25rem}.fc-item--has-boosted-title .fc-item--full-media-50-tablet.fc-item--has-cutout .fc-item__header{font-size:2.25rem;line-height:2.5rem}}@media (min-width: 46.25em){.fc-item--full-media-50-tablet.fc-item--has-cutout .fc-item__standfirst{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;padding-right:8.75rem;display:block}.fc-item--full-media-50-tablet .fc-item__avatar{height:17.25rem}.fc-item--full-media-50-tablet .fc-item__avatar__media{right:-5%}.fc-item--full-media-50-tablet .fc-sublink:nth-child(n+5){display:none}}@media (min-width: 46.25em){.fc-item--full-media-75-tablet .fc-item__image-container{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-left:0.3125rem}.fc-item--full-media-75-tablet .fc-item__content{position:relative}.fc-item--full-media-75-tablet .fc-item__content>*{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-right:0.9375rem}.has-flex-wrap .fc-item--full-media-75-tablet .fc-item__container{-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-orient:horizontal;-webkit-box-direction:reverse;-webkit-flex-direction:row-reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse}.has-flex-wrap .fc-item--full-media-75-tablet .fc-item__media-wrapper{-webkit-flex-basis:74%;-ms-flex-preferred-size:74%;flex-basis:74%}.has-flex-wrap .fc-item--full-media-75-tablet .fc-item__video-fallback{-webkit-flex-basis:74%;-ms-flex-preferred-size:74%;flex-basis:74%}.has-flex-wrap .fc-item--full-media-75-tablet .fc-item__content{-webkit-flex-basis:26%;-ms-flex-preferred-size:26%;flex-basis:26%;max-width:26%}.has-flex-wrap .fc-item--full-media-75-tablet .fc-item__footer--horizontal{-webkit-flex-basis:100%;-ms-flex-preferred-size:100%;flex-basis:100%}.has-no-flex-wrap .fc-item--full-media-75-tablet .fc-item__media-wrapper{width:74%;float:right}.has-no-flex-wrap .fc-item--full-media-75-tablet .fc-item__content{width:26%}.fc-item--full-media-75-tablet.fc-item--has-no-image .fc-item__content{-webkit-flex-basis:100%;-ms-flex-preferred-size:100%;flex-basis:100%;max-width:100%;padding-right:13.75rem}.fc-item--full-media-75-tablet .fc-item__header{font-size:1.25rem;line-height:1.5rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--full-media-75-tablet .fc-item__header{font-size:1.75rem;line-height:2rem}.fc-item--has-boosted-title .fc-item--full-media-75-tablet .fc-item__header{font-size:2rem;line-height:2.25rem}}@media (min-width: 46.25em){.fc-item--full-media-75-tablet .fc-item__standfirst,.fc-item--full-media-75-tablet .fc-item__image-container{display:block}.fc-item--full-media-75-tablet.fc-item--has-no-image .fc-item__standfirst{display:block}.fc-item--full-media-75-tablet .fc-item__footer{clear:left}.fc-item--full-media-75-tablet.fc-item--has-sublinks-3 .fc-item__standfirst{display:none}.fc-item--full-media-75-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-item__footer--vertical{display:none}.fc-item--full-media-75-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-item__footer--horizontal{display:block;clear:both}.has-flex-wrap .fc-item--full-media-75-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-sublinks{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex}.has-flex-wrap .fc-item--full-media-75-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-sublink{-webkit-box-flex:1;-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%}.has-flex-wrap .fc-item--full-media-75-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-sublink+*{margin-left:1.25rem}.has-no-flex-wrap .fc-item--full-media-75-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-sublinks{display:table;table-layout:fixed;width:100%}.has-no-flex-wrap .fc-item--full-media-75-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-sublink{display:table-cell;padding-right:1.25rem}.has-no-flex-wrap .fc-item--full-media-75-tablet.fc-item--has-sublinks-4:not(.fc-item--has-cutout) .fc-sublink:last-child{padding-right:0}.fc-item--full-media-75-tablet.fc-item--has-cutout .fc-item__container{min-height:16.5rem}.has-flex-wrap .fc-item--full-media-75-tablet.fc-item--has-cutout .fc-item__container{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row}.fc-item--full-media-75-tablet.fc-item--has-cutout .fc-item__content{width:auto;max-width:28.75rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--full-media-75-tablet.fc-item--has-cutout .fc-item__content{max-width:38.75rem}}@media (min-width: 46.25em){.has-flex-wrap .fc-item--full-media-75-tablet.fc-item--has-cutout .fc-item__content{-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto}.fc-item--full-media-75-tablet.fc-item--has-cutout .fc-item__header{font-size:1.5rem;line-height:1.75rem}.fc-item--has-boosted-title .fc-item--full-media-75-tablet.fc-item--has-cutout .fc-item__header{font-size:1.75rem;line-height:2rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--full-media-75-tablet.fc-item--has-cutout .fc-item__header{font-size:2rem;line-height:2.25rem}.fc-item--has-boosted-title .fc-item--full-media-75-tablet.fc-item--has-cutout .fc-item__header{font-size:2.25rem;line-height:2.5rem}}@media (min-width: 46.25em){.fc-item--full-media-75-tablet.fc-item--has-cutout .fc-item__standfirst{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;padding-right:8.75rem;display:block}.fc-item--full-media-75-tablet .fc-item__avatar{height:17.25rem}.fc-item--full-media-75-tablet .fc-item__avatar__media{right:-5%}.fc-item--full-media-75-tablet .fc-sublink:nth-child(n+5){display:none}}@media (min-width: 46.25em){.fc-item--full-media-100-tablet .fc-item__image-container{display:block;padding-bottom:40%}.fc-item--full-media-100-tablet .responsive-img{top:-25%;height:auto}.fc-item--full-media-100-tablet .fc-item__header{font-size:1.5rem;line-height:1.75rem}.fc-item--has-boosted-title .fc-item--full-media-100-tablet .fc-item__header{font-size:1.75rem;line-height:2rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--full-media-100-tablet .fc-item__header{font-size:2rem;line-height:2.25rem}.fc-item--has-boosted-title .fc-item--full-media-100-tablet .fc-item__header{font-size:2.25rem;line-height:2.5rem}}@media (min-width: 46.25em){.fc-item--full-media-100-tablet.fc-item--has-cutout .fc-item__container{min-height:16.5rem}.fc-item--full-media-100-tablet.fc-item--has-cutout .responsive-img{top:auto;height:100%}.fc-item--full-media-100-tablet.fc-item--has-cutout .fc-item__content{width:auto;max-width:28.75rem}}@media (min-width: 46.25em) and (min-width: 61.25em){.fc-item--full-media-100-tablet.fc-item--has-cutout .fc-item__content{max-width:38.75rem}}@media (min-width: 46.25em){.fc-item--full-media-100-tablet.fc-item--has-cutout .fc-item__standfirst{font-size:1rem;line-height:1.25rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;padding-right:8.75rem;display:block}.fc-item--full-media-100-tablet .fc-item__avatar{height:17.25rem}.fc-item--full-media-100-tablet .fc-item__avatar__media{right:-15%}}@media (min-width: 46.25em) and (min-width: 46.25em){.fc-item--full-media-100-tablet .fc-item__avatar__media{right:-5%}}@media (min-width: 46.25em){.has-flex-wrap .fc-item--full-media-100-tablet:not(.fc-item--has-cutout) .fc-sublinks{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex}.has-flex-wrap .fc-item--full-media-100-tablet:not(.fc-item--has-cutout) .fc-sublink{-webkit-box-flex:1;-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%}.has-flex-wrap .fc-item--full-media-100-tablet:not(.fc-item--has-cutout) .fc-sublink+*{margin-left:1.25rem}.has-no-flex-wrap .fc-item--full-media-100-tablet:not(.fc-item--has-cutout) .fc-sublinks{display:table;table-layout:fixed;width:100%}.has-no-flex-wrap .fc-item--full-media-100-tablet:not(.fc-item--has-cutout) .fc-sublink{display:table-cell;padding-right:1.25rem}.has-no-flex-wrap .fc-item--full-media-100-tablet:not(.fc-item--has-cutout) .fc-sublink:last-child{padding-right:0}.fc-item--full-media-100-tablet .fc-item__footer--horizontal{-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto}}@media (max-width: 46.24em){.fc-item--fluid-mobile .fc-item__content{padding-bottom:0}.fc-item--fluid-mobile .fc-item__image-container,.fc-item--fluid-mobile .fc-item__standfirst{display:block}}@media (min-width: 30em) and (max-width: 46.24em){.fc-item--fluid-mobile .fc-item__image-container{display:none}.fc-item--fluid-mobile .fc-item__header{font-size:1.75rem;line-height:2rem}}@media (min-width: 46.25em){.fc-item--fluid-tablet .fc-item__content{padding-bottom:0}.fc-item--fluid-tablet .fc-item__image-container,.fc-item--fluid-tablet .fc-item__standfirst{display:block}.fc-item--fluid-tablet .fc-item__image-container{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-left:0.3125rem}.fc-item--fluid-tablet .fc-item__content{position:relative}.fc-item--fluid-tablet .fc-item__content>*{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding-right:0.9375rem}.has-flex-wrap .fc-item--fluid-tablet .fc-item__container{-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-orient:horizontal;-webkit-box-direction:reverse;-webkit-flex-direction:row-reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse}.has-flex-wrap .fc-item--fluid-tablet .fc-item__media-wrapper{-webkit-flex-basis:20%;-ms-flex-preferred-size:20%;flex-basis:20%}.has-flex-wrap .fc-item--fluid-tablet .fc-item__video-fallback{-webkit-flex-basis:20%;-ms-flex-preferred-size:20%;flex-basis:20%}.has-flex-wrap .fc-item--fluid-tablet .fc-item__content{-webkit-flex-basis:80%;-ms-flex-preferred-size:80%;flex-basis:80%;max-width:80%}.has-flex-wrap .fc-item--fluid-tablet .fc-item__footer--horizontal{-webkit-flex-basis:100%;-ms-flex-preferred-size:100%;flex-basis:100%}.has-no-flex-wrap .fc-item--fluid-tablet .fc-item__media-wrapper{width:20%;float:right}.has-no-flex-wrap .fc-item--fluid-tablet .fc-item__content{width:80%}.fc-item--fluid-tablet.fc-item--has-no-image .fc-item__content{-webkit-flex-basis:100%;-ms-flex-preferred-size:100%;flex-basis:100%;max-width:100%;padding-right:13.75rem}.has-flex-wrap .fc-item--fluid-tablet .fc-item__container{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row}.fc-item--fluid-tablet .fc-item__header{font-size:1.25rem;line-height:1.5rem}}@media (min-width: 61.25em){.fc-item--fluid-tablet .fc-item__header{font-size:2rem;line-height:2.25rem}.fc-item--fluid-tablet .fc-item__header,.fc-item--fluid-tablet .fc-item__standfirst{padding-right:30%}}.fc-item--list-compact{font-size:1rem;line-height:1.5rem;font-family:"Guardian Text Egyptian Web",Georgia,serif;font-weight:bold;color:#333;padding-top:0.25rem;padding-bottom:0.75rem;border-top:0.0625rem solid #eaeaea;display:block !important;background-color:transparent}.fc-item--list-compact .fc-item__container{font-size:1rem;line-height:1.25rem;display:block !important}.fc-item--list-compact--media{font-size:1rem;line-height:1.5rem;font-family:"Guardian Text Egyptian Web",Georgia,serif;font-weight:bold;color:#333;padding-top:0.25rem;padding-bottom:0.75rem;border-top:0.0625rem solid #eaeaea;display:block !important;background-color:transparent;min-height:4.5rem;padding-left:7.5rem}.fc-item--list-compact--media .fc-item__container{font-size:1rem;line-height:1.25rem;display:block !important}.fc-item--list-compact--media .fc-item__image-container{overflow:visible}.fc-item--list-compact--media .fc-item__image-container{display:block}.fc-item--list-compact--media .fc-item__media-wrapper{width:7.5rem;padding-right:0.625rem;margin-left:-7.5rem;float:left}.fc-slice--single-col .fc-slice__item{padding-bottom:0}.fc-slice--single-col .fc-slice__item:before{display:none}.fc-slice--single-col .fc-item{margin-left:0;margin-right:0}.linkslist-container{position:relative;margin:0 !important}@media (min-width: 46.25em){.linkslist-container{margin-top:0.5625rem}}.linkslist-container.tone-feature:before{background:#fdadba}.linkslist-container.tone-comment:before{background:#ff9b0b}.linkslist-container.tone-media:before{background:#fb0}.linkslist-container.show-more--hidden,.linkslist-container.show-more--hidden:before{display:none}.linkslist{margin-top:0;width:100%}@media (min-width: 46.25em) and (max-width: 61.24em){.linkslist .fc-slice__item{width:50%}.linkslist .fc-slice__item:nth-child(2n+1){clear:both}.linkslist .fc-slice__item:nth-child(2n+1):before{border:0}.linkslist .fc-slice__item:nth-child(2n+1):nth-last-child(-n+4),.linkslist .fc-slice__item:nth-child(2n+2):nth-last-child(-n+3){padding-bottom:0}.linkslist .fc-slice__item:nth-child(2n+1):nth-last-child(-n+2),.linkslist .fc-slice__item:nth-child(2n+2):last-child{padding-top:0.75rem}}@media (min-width: 61.25em){.linkslist .fc-slice__item{width:33.33333%}.linkslist .fc-slice__item:nth-child(3n+1){clear:both}.linkslist .fc-slice__item:nth-child(3n+1):before{border:0}.linkslist .fc-slice__item:nth-child(3n+1):nth-last-child(-n+6),.linkslist .fc-slice__item:nth-child(3n+2):nth-last-child(-n+5),.linkslist .fc-slice__item:nth-child(3n+3):nth-last-child(-n+4){padding-bottom:0}.linkslist .fc-slice__item:nth-child(3n+1):nth-last-child(-n+3),.linkslist .fc-slice__item:nth-child(3n+2):nth-last-child(-n+2),.linkslist .fc-slice__item:nth-child(3n+3):last-child{padding-top:0.75rem}}@media (min-width: 46.25em){.has-flex-wrap .linkslist .fc-slice__item{-webkit-box-flex:0;-webkit-flex-grow:0;-ms-flex-positive:0;flex-grow:0;-webkit-flex-basis:50%;-ms-flex-preferred-size:50%;flex-basis:50%}}@media (min-width: 61.25em){.has-flex-wrap .linkslist .fc-slice__item{-webkit-flex-basis:33.33333%;-ms-flex-preferred-size:33.33333%;flex-basis:33.33333%}}.linkslist .item--has-cutout{padding-bottom:1.875rem}.tone-news--item.fc-item,.tone-news--item.rich-link{background-color:#f6f6f6}.tone-news--item .rich-link__container:before,.tone-news--item .fc-item__container:before{background-color:#4bc6df}.tone-news--item .fc-item__kicker,.tone-news--item .fc-item__byline,.tone-news--item .rich-link__read-more-text{color:#005689}.tone-news--item .fc-item__kicker--dreamsnap{background-color:#ddd}.tone-news--item .fc-item__kicker--breaking-news{color:#b51800}.tone-news--item .rich-link__arrow-icon{fill:#005689}.tone-news--sublink .fc-sublink__kicker,.tone-news--sublink .fc-sublink__byline{color:#005689}.tone-editorial--item .tone-news--sublink .fc-sublink__kicker{color:#ffffff}.tone-feature--item .tone-news--sublink .fc-sublink__kicker{color:#ffffff}.tone-live--item .tone-news--sublink .fc-sublink__kicker{color:#ffffff}.tone-media--item .tone-news--sublink .fc-sublink__kicker{color:#ffffff}.tone-special-report--item .tone-news--sublink .fc-sublink__kicker{color:#ffffff}.tone-news--most-popular .fc-item__kicker{color:#005689}.tone-live--item{background-color:#b51800}.tone-live--item,.tone-live--item .fc-sublink__title{color:#fff}.tone-live--item .u-faux-block-link--hover,.tone-live--item .fc-item__image-container{background-color:#a11500}.tone-live--item .fc-item__link:visited,.tone-live--item .fc-sublink__link:visited{color:#f0d1cc}.tone-live--item .inline-quote{fill:#fff}.tone-live--item .fc-item__container:before,.tone-live--item .rich-link__container:before{background-color:#fdadba}.tone-live--item .fc-item__kicker,.tone-live--item .fc-item__byline,.tone-live--item .fc-item__meta,.tone-live--item .rich-link__read-more-text{color:#fdadba}.tone-live--item .rich-link__arrow-icon{fill:#fdadba}.tone-live--item .fc-item__kicker:after,.tone-live--item .rich-link__kicker:after,.tone-live--item .fc-sublink__kicker:after{color:#c44633}.tone-live--item .fc-item__kicker--dreamsnap{background-color:#a31600}.tone-live--item .fc-item__standfirst{color:#f0d1cc}.tone-live--item .fc-item__live-indicator,.tone-live--item .fc-item__breaking-indicator{color:#ffffff;font-weight:400}.tone-live--item .fc-sublink__title:before{border-color:#c44633}.tone-live--item .fc-item__meta .inline-icon{fill:#fdadba}.tone-live--sublink .fc-sublink__kicker{color:#cc2b12}.tone-live--sublink .fc-sublink__live-indicator,.tone-live--sublink .fc-sublink__breaking-indicator{color:#b51800}.tone-editorial--item .tone-live--sublink .fc-sublink__kicker{color:#ffffff}.tone-feature--item .tone-live--sublink .fc-sublink__kicker{color:#ffffff}.tone-live--item .tone-live--sublink .fc-sublink__kicker{color:#ffffff}.tone-media--item .tone-live--sublink .fc-sublink__kicker{color:#ffffff}.tone-review--item .tone-live--sublink .fc-sublink__kicker{color:#ffffff}.tone-live--most-popular .fc-item__kicker{color:#cc2b12}.tone-comment--item.fc-item,.tone-comment--item.rich-link,.fc-item.tone-letters--item,.rich-link.tone-letters--item{background-color:#efefec}.tone-comment--item .u-faux-block-link--hover,.tone-comment--item .fc-item__image-container,.tone-letters--item .u-faux-block-link--hover,.tone-letters--item .fc-item__image-container{background-color:#e3e3de}.tone-comment--item .fc-item__container:before,.tone-comment--item .rich-link__container:before,.tone-letters--item .fc-item__container:before,.tone-letters--item .rich-link__container:before{background-color:#e6711b}.tone-comment--item .fc-item__kicker,.tone-comment--item .rich-link__kicker,.tone-comment--item .fc-item__byline,.tone-comment--item .rich-link__byline,.tone-comment--item .rich-link__read-more-text,.tone-letters--item .fc-item__kicker,.tone-letters--item .rich-link__kicker,.tone-letters--item .fc-item__byline,.tone-letters--item .rich-link__byline,.tone-letters--item .rich-link__read-more-text{color:#e6711b}.tone-comment--item .fc-item__kicker--dreamsnap,.tone-letters--item .fc-item__kicker--dreamsnap{background-color:#d7d7d4}.tone-comment--item .rich-link__arrow-icon,.tone-letters--item .rich-link__arrow-icon{fill:#e6711b}.tone-comment--item .fc-item__standfirst ul>li:before,.tone-comment--item .rich-link__standfirst ul>li:before,.tone-letters--item .fc-item__standfirst ul>li:before,.tone-letters--item .rich-link__standfirst ul>li:before{background:#bdbdbd}.tone-comment--sublink .fc-sublink__kicker,.tone-letters--sublink .fc-sublink__kicker{color:#e6711b}.tone-live--item .tone-comment--sublink .fc-sublink__kicker,.tone-live--item .tone-letters--sublink .fc-sublink__kicker{color:#efefec}.tone-review--item .tone-comment--sublink .fc-sublink__kicker,.tone-review--item .tone-letters--sublink .fc-sublink__kicker{color:#efefec}.tone-media--item .tone-comment--sublink .fc-sublink__kicker,.tone-media--item .tone-letters--sublink .fc-sublink__kicker{color:#efefec}.tone-comment--most-popular .fc-item__kicker,.tone-letters--most-popular .fc-item__kicker{color:#e6711b}.tone-feature--item{background-color:#951c55}.tone-feature--item,.tone-feature--item .rich-link__link,.tone-feature--item .fc-sublink__title{color:#fff}.tone-feature--item .u-faux-block-link--hover,.tone-feature--item .fc-item__image-container{background-color:#84194b}.tone-feature--item .fc-item__link:visited,.tone-feature--item .rich-link__link:visited,.tone-feature--item .fc-sublink__link:visited{color:#ead2dd}.tone-feature--item .inline-quote,.tone-feature--item .fc-item__meta .inline-icon{fill:#fdadba}.tone-feature--item .fc-item__container:before,.tone-feature--item .rich-link__container:before{background-color:#fdadba}.tone-feature--item .fc-item__kicker,.tone-feature--item .fc-item__byline,.tone-feature--item .fc-item__meta,.tone-feature--item .rich-link__read-more-text{color:#fdadba}.tone-feature--item .fc-item__kicker--dreamsnap{background-color:#86194d}.tone-feature--item .rich-link__arrow-icon{fill:#fdadba}.tone-feature--item .fc-item__kicker:after,.tone-feature--item .fc-sublink__kicker:after{color:#aa4977}.tone-feature--item .fc-item__standfirst,.tone-feature--item .rich-link__standfirst{color:#ead2dd}.tone-feature--item .fc-item__standfirst ul>li:before,.tone-feature--item .rich-link__standfirst ul>li:before{background:#bf7799}.tone-feature--item .fc-item__title .i{display:inline-block;height:.9em;width:1em;background-position:center}.tone-feature--item .fc-sublink__title:before{border-color:#bf7799}.tone-feature--sublink .fc-sublink__kicker{color:#951c55}.tone-editorial--item .tone-feature--sublink .fc-sublink__kicker{color:#fdadba}.tone-feature--item .tone-feature--sublink .fc-sublink__kicker{color:#fdadba}.tone-live--item .tone-feature--sublink .fc-sublink__kicker{color:#fdadba}.tone-media--item .tone-feature--sublink .fc-sublink__kicker{color:#fdadba}.tone-review--item .tone-feature--sublink .fc-sublink__kicker{color:#fdadba}.tone-feature--most-popular .fc-item__kicker{color:#951c55}.tone-analysis--item.fc-item,.tone-analysis--item.rich-link{background-color:#f1f1f1;color:#005689}.tone-analysis--item .u-faux-block-link--hover,.tone-analysis--item .fc-item__image-container{background-color:#e4e4e4}.tone-analysis--item .fc-item__container:before,.tone-analysis--item .rich-link__container:before{background-color:#4bc6df}.tone-analysis--item .rich-link__read-more-text{color:#005689}.tone-analysis--item .rich-link__arrow-icon{fill:#005689}.tone-analysis--item .fc-item__kicker,.tone-analysis--item .rich-link__kicker,.tone-analysis--item .fc-item__byline,.tone-analysis--item .rich-link__standfirst{color:#63717a}.tone-analysis--item .fc-item__kicker--dreamsnap{background-color:#d9d9d9}.tone-analysis--item .fc-item__meta{color:#767676}.tone-analysis--sublink .fc-item__kicker,.tone-analysis--most-popular .fc-item__kicker{color:#4bc6df}.tone-live--item .tone-analysis--sublink .fc-sublink__kicker,.tone-live--item .tone-analysis--most-popular .fc-sublink__kicker{color:#ffffff}.tone-media--item{background-color:#333}.tone-media--item,.tone-media--item .fc-sublink__title{color:#fff}.tone-media--item .u-faux-block-link--hover,.tone-media--item .fc-item__image-container{background-color:#202020}.tone-media--item .fc-item__link:visited,.tone-media--item .rich-link__link:visited,.tone-media--item .fc-sublink__link:visited{color:#d6d6d6}.tone-media--item .rich-link__arrow-icon{fill:#fb0}.tone-media--item .inline-quote{fill:#bdbdbd}.tone-media--item .fc-item__container:before,.tone-media--item .rich-link__container:before{background-color:#fb0}.tone-media--item .fc-item__kicker,.tone-media--item .rich-link__kicker,.tone-media--item .fc-item__byline,.tone-media--item .rich-link__read-more-text{color:#fb0}.tone-media--item .fc-item__kicker:after,.tone-media--item .rich-link__kicker:after,.tone-media--item .fc-sublink__kicker:after{color:#737373}.tone-media--item .fc-item__kicker--dreamsnap{background-color:#141414}.tone-media--item .fc-item__standfirst,.tone-media--item .rich-link__standfirst,.tone-media--item .fc-item__meta{color:#bdbdbd}.tone-media--sublink .fc-sublink__kicker{color:#fb0}.tone-analysis--item .tone-media--sublink .fc-sublink__kicker{color:#161616}.tone-comment--item .tone-media--sublink .fc-sublink__kicker{color:#161616}.tone-letters--item .tone-media--sublink .fc-sublink__kicker{color:#161616}.tone-dead--item .tone-media--sublink .fc-sublink__kicker{color:#161616}.tone-news--item .tone-media--sublink .fc-sublink__kicker{color:#161616}.tone-media--most-popular .fc-item__kicker{color:#005689}.tone-review--item{background-color:#7d7569}.tone-review--item,.tone-review--item .fc-sublink__title{color:#fff}.tone-review--item .u-faux-block-link--hover,.tone-review--item .fc-item__image-container{background-color:#6c655b}.tone-review--item .fc-item__link:visited,.tone-review--item .fc-sublink__link:visited{color:#e5e3e1}.tone-review--item .inline-quote{fill:#ffce4b}.tone-review--item .fc-item__container:before,.tone-review--item .rich-link__container:before{background-color:#ffce4b}.tone-review--item .fc-item__kicker,.tone-review--item .fc-item__byline,.tone-review--item .rich-link__read-more-text{color:#ffce4b}.tone-review--item .fc-item__kicker--dreamsnap{background-color:#71695f}.tone-review--item .rich-link__arrow-icon{fill:#ffce4b}.tone-review--item .fc-item__kicker:after,.tone-review--item .fc-sublink__kicker:after{color:#979187}.tone-review--item .fc-item__standfirst{color:#cbc8c3}.tone-review--item .fc-item__meta{color:#dcdcdc}.tone-review--item .tone-news--sublink .fc-sublink__kicker{color:#ffffff}.tone-review--sublink .fc-sublink__kicker{color:#ffce4b}.tone-analysis--item .tone-review--sublink .fc-sublink__kicker{color:#7d7569}.tone-comment--item .tone-review--sublink .fc-sublink__kicker{color:#7d7569}.tone-dead--item .tone-review--sublink .fc-sublink__kicker{color:#7d7569}.tone-letters--item .tone-review--sublink .fc-sublink__kicker{color:#7d7569}.tone-news--item .tone-review--sublink .fc-sublink__kicker{color:#7d7569}.tone-review--most-popular .fc-item__kicker{color:#7d7569}.tone-dead--item.fc-item,.tone-dead--item.rich-link{background-color:#f1f1f1}.tone-dead--item .u-faux-block-link--hover,.tone-dead--item .fc-item__image-container{background-color:#e5e5e5}.tone-dead--item .fc-item__container:before,.tone-dead--item .rich-link__container:before{background-color:#b51800}.tone-dead--item .fc-item__kicker,.tone-dead--item .fc-item__byline{color:#cc2b12}.tone-dead--item .fc-item__kicker--dreamsnap{background-color:#d9d9d9}.tone-dead--item .rich-link__read-more-text{color:#767676}.tone-dead--item .rich-link__arrow-icon{fill:#767676}.tone-dead--sublink .fc-sublink__kicker{color:#cc2b12}.tone-editorial--item .tone-dead--sublink .fc-sublink__kicker{color:#ffffff}.tone-feature--item .tone-dead--sublink .fc-sublink__kicker{color:#ffffff}.tone-live--item .tone-dead--sublink .fc-sublink__kicker{color:#ffffff}.tone-media--item .tone-dead--sublink .fc-sublink__kicker{color:#ffffff}.tone-review--item .tone-dead--sublink .fc-sublink__kicker{color:#ffffff}.tone-dead--most-popular .fc-item__kicker{color:#cc2b12}.tone-editorial--item{background-color:#005689}.tone-editorial--item,.tone-editorial--item .rich-link__link,.tone-editorial--item .fc-sublink__title,.tone-editorial--item .rich-link__standfirst{color:#fff}.tone-editorial--item .u-faux-block-link--hover,.tone-editorial--item .fc-item__image-container{background-color:#004670}.tone-editorial--item .fc-item__link:visited,.tone-editorial--item .fc-sublink__link:visited{color:#ccdde7}.tone-editorial--item .inline-quote,.tone-editorial--item .fc-item__meta .inline-icon{fill:#aad8f1}.tone-editorial--item .fc-item__container:before,.tone-editorial--item .rich-link__container:before{background-color:#aad8f1}.tone-editorial--item .fc-item__kicker,.tone-editorial--item .fc-item__byline,.tone-editorial--item .fc-item__standfirst,.tone-editorial--item .rich-link__read-more-text{color:#aad8f1}.tone-editorial--item .fc-item__kicker--dreamsnap{background-color:#004d7b}.tone-editorial--item .rich-link__arrow-icon{fill:#aad8f1}.tone-editorial--item .fc-item__meta{color:#aad8f1}.tone-editorial--item .fc-sublink__title:before{border-color:#3378a1}.tone-editorial--sublink .fc-sublink__kicker{color:#005689}.tone-editorial--item .tone-editorial--sublink .fc-sublink__kicker{color:#aad8f1}.tone-feature--item .tone-editorial--sublink .fc-sublink__kicker{color:#aad8f1}.tone-live--item .tone-editorial--sublink .fc-sublink__kicker{color:#aad8f1}.tone-media--item .tone-editorial--sublink .fc-sublink__kicker{color:#aad8f1}.tone-review--item .tone-editorial--sublink .fc-sublink__kicker{color:#aad8f1}.tone-editorial--most-popular .fc-item__kicker{color:#005689}.tone-external--item{background-color:#eaeaea}.tone-external--item .fc-item__kicker,.tone-external--item .fc-item__byline{color:#1c6326}.tone-external--item .fc-item__kicker--dreamsnap{background-color:#d3d3d3}.tone-external--item .u-faux-block-link--hover,.tone-external--item .fc-item__image-container{background-color:#e2e2e2}.tone-external--item .fc-item__container:before,.tone-external--item .rich-link__container:before{background-color:#a9af2b}.tone-special-report--item.fc-item,.tone-special-report--item.rich-link{background-color:#63717a}.tone-special-report--item .u-faux-block-link--hover,.tone-special-report--item .fc-item__image-container{background-color:#58646c}.tone-special-report--item .inline-quote{fill:#dcdcdc}.tone-special-report--item .rich-link__container:before,.tone-special-report--item .fc-item__container:before{background-color:#4bc6df}.tone-special-report--item,.tone-special-report--item .fc-sublink__title,.tone-special-report--item .fc-sublink__kicker{color:#ffffff}.tone-special-report--item .fc-item__link:visited,.tone-special-report--item .fc-sublink__link:visited{color:#e0e3e4}.tone-special-report--item .fc-item__kicker,.tone-special-report--item .rich-link__kicker,.tone-special-report--item .fc-item__byline,.tone-special-report--item .rich-link__byline,.tone-special-report--item .rich-link__read-more-text{color:#4bc6df}.tone-special-report--item .fc-item__kicker--dreamsnap{background-color:#59666e}.tone-special-report--item .fc-item__kicker--breaking-news{color:#ff7c69}.tone-special-report--item .fc-item__standfirst{color:#e0e3e4}.tone-special-report--item .rich-link__arrow-icon{fill:#4bc6df}.tone-special-report--item .fc-item__kicker:after,.tone-special-report--item .rich-link__kicker:after,.tone-special-report--item .fc-sublink__kicker:after{color:#828d95}.tone-special-report--item .fc-sublink__title:before{border-color:#e0e3e4}.tone-special-report--item .fc-item__meta{color:#dcdcdc}.tone-news--sublink .fc-sublink__kicker,.tone-news--sublink .fc-sublink__byline{color:#005689}.tone-editorial--item .tone-news--sublink .fc-sublink__kicker{color:#ffffff}.tone-feature--item .tone-news--sublink .fc-sublink__kicker{color:#ffffff}.tone-live--item .tone-news--sublink .fc-sublink__kicker{color:#ffffff}.tone-media--item .tone-news--sublink .fc-sublink__kicker{color:#ffffff}.tone-news--most-popular .fc-item__kicker{color:#005689}.treats__container{list-style-type:none;margin:0.75rem 0;display:none;position:absolute;bottom:0.6875rem}.fc-container--has-show-more .treats__container{bottom:2.5625rem}.fc-container--rolled-up .treats__container{display:none}@media (min-width: 71.25em){.treats__container{display:block}}@media (min-width: 81.25em){.has-page-skin .treats__container{display:none}}.treats__treat{font-size:0.75rem;line-height:1rem;font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;height:1.5rem;padding:0 0.5rem;margin-right:0.5rem;line-height:1.375rem;-webkit-border-radius:62.5rem;border-radius:62.5rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#005689;background-color:#fff;border-color:#4bc6df;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;display:inline-block;vertical-align:top;width:auto;font-weight:700;border-width:0.0625rem;border-style:solid;text-decoration:none;max-width:18.75rem;line-height:22px}.treats__treat .i{width:1.5rem;height:1.5rem;margin:-0.0625rem -0.5rem 0}.treats__treat svg{width:1.5rem;height:1.5rem}.treats__treat .i-left{margin-left:-0.5rem;margin-right:0}.treats__treat .i-right{margin-right:-0.5rem;margin-left:0}.treats__treat:hover,.treats__treat:focus,.treats__treat:active{background-color:#fff;border-color:#a4a4a4}@media (min-width: 71.25em){.treats__treat{max-width:8.75rem}}@media (min-width: 81.25em){.treats__treat{max-width:13.75rem}}.treats__treat:hover,.treats__treat:focus,.treats__treat:active{color:#333;text-decoration:none}.treats__list-item{margin-top:0.5rem}.treats__list-item:first-child{margin-top:0}.treats__crossword{display:block;margin-top:1rem;margin-bottom:0.5rem}.treats__crossword-link:hover .treats__treat,.treats__crossword-link:focus .treats__treat,.treats__crossword-link:active .treats__treat{color:#333;border-color:#a4a4a4}.fc-cp-scott__quote{display:block;color:#767676}@media (min-width: 30em){.fc-cp-scott__quote-line{display:block}}.fc-cp-scott__citation{display:block}.fc-cp-scott__portrait{float:right;width:4.375rem}@media (max-width: 29.99em){.fc-cp-scott__portrait{position:absolute;bottom:0;right:0}}@media (min-width: 46.25em){.fc-cp-scott__portrait{margin-top:-0.375rem;margin-bottom:0.375rem;width:5rem}}@media (min-width: 71.25em){.fc-cp-scott__portrait{margin-top:0;margin-bottom:0;float:none}}@media (min-width: 81.25em){.has-page-skin .fc-cp-scott__portrait{float:right;margin-top:-0.375rem;margin-bottom:0.375rem}}.fc-cp-scott__text{font-size:0.875rem;line-height:1.125rem;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-weight:normal;clear:left;margin-right:5rem;line-height:1rem}.fc-cp-scott__text .inline-quote svg{height:0.625rem;fill:#767676}@media (min-width: 30em){.fc-cp-scott__text{clear:none;float:right;margin-right:0.625rem;margin-top:0.125rem}}@media (min-width: 46.25em){.fc-cp-scott__text{margin-top:0}}@media (min-width: 71.25em){.fc-cp-scott__text{float:none;margin-right:0}}@media (min-width: 81.25em){.has-page-skin .fc-cp-scott__text{float:right;margin-right:0.625rem}}.badge-slot{width:2.0625rem;margin-top:0.125rem}@media (max-width: 61.24em){.badge-slot{float:left;margin-right:0.3125rem}}@media (min-width: 61.25em){.badge-slot{width:3.75rem}}.badge-slot__img{width:100%}.content__head--is-badged .content__section-label,.content__head--is-badged .content__series-label{float:none}
/*# sourceMappingURL=head.facia.css.map */


</style>
<link rel="stylesheet" type="text/css" href="https://assets.guim.co.uk/stylesheets/e8793d2b0c5050b5980360493c10720a/facia.css" media="only x"/>
<noscript>
<link rel="stylesheet" type="text/css" href="https://assets.guim.co.uk/stylesheets/e8793d2b0c5050b5980360493c10720a/facia.css"/>
</noscript>
<!--<![endif]-->
<link rel="stylesheet" media="print" type="text/css" href="https://assets.guim.co.uk/stylesheets/6b958532c211045f7ce1185bd3bb443a/print.css"/>
<style class="webfont" data-cache-name="GuardianEgyptianWeb" data-cache-file-woff2="https://assets.guim.co.uk/fonts/a24c7bea5a91ee87d0868f0d587c6129/GuardianEgyptianWeb.woff2.json" data-cache-file-hinted-cleartype-woff2="https://assets.guim.co.uk/fonts/fb32696c02620a1b503e233c1359e2f8/GuardianEgyptianWebCleartypeHinted.woff2.json" data-cache-file-hinted-auto-woff2="https://assets.guim.co.uk/fonts/1513269d7c379805b57784bb334a331f/GuardianEgyptianWebAutoHinted.woff2.json" data-cache-file-woff="https://assets.guim.co.uk/fonts/a551aab8b1ccfcfd32edd37a27fc1823/GuardianEgyptianWeb.woff.json" data-cache-file-hinted-cleartype-woff="https://assets.guim.co.uk/fonts/f4ec7dfc5cc01960abe6bc0a42714ec9/GuardianEgyptianWebCleartypeHinted.woff.json" data-cache-file-hinted-auto-woff="https://assets.guim.co.uk/fonts/c9dd78499c869cc0c77c91e6a4d8d0e5/GuardianEgyptianWebAutoHinted.woff.json" data-cache-file-ttf="https://assets.guim.co.uk/fonts/a0e077ccafc42d20b07a3f234a06b576/GuardianEgyptianWeb.ttf.json" data-cache-file-hinted-cleartype-ttf="https://assets.guim.co.uk/fonts/2738675136670257aaa1a48b6921c04f/GuardianEgyptianWebCleartypeHinted.ttf.json" data-cache-file-hinted-auto-ttf="https://assets.guim.co.uk/fonts/1204ca5411e8d3fb8c0f9cb90400957c/GuardianEgyptianWebAutoHinted.ttf.json"></style>
<style class="webfont" data-cache-name="GuardianTextEgyptianWeb" data-cache-file-woff2="https://assets.guim.co.uk/fonts/97fe10912fa4379b2566da45aa949ad0/GuardianTextEgyptianWeb.woff2.json" data-cache-file-hinted-cleartype-woff2="https://assets.guim.co.uk/fonts/b58082bdb36433347e22031ab01e335f/GuardianTextEgyptianWebCleartypeHinted.woff2.json" data-cache-file-hinted-auto-woff2="https://assets.guim.co.uk/fonts/009f55005e0c252697ac298193f7eeb1/GuardianTextEgyptianWebAutoHinted.woff2.json" data-cache-file-woff="https://assets.guim.co.uk/fonts/fbe0437c39cd0f89db6acf24e36c1437/GuardianTextEgyptianWeb.woff.json" data-cache-file-hinted-cleartype-woff="https://assets.guim.co.uk/fonts/6e81caf787303d24efd7b0930b837b4d/GuardianTextEgyptianWebCleartypeHinted.woff.json" data-cache-file-hinted-auto-woff="https://assets.guim.co.uk/fonts/186a723d9113413d244e6fbcec9a32f2/GuardianTextEgyptianWebAutoHinted.woff.json" data-cache-file-ttf="https://assets.guim.co.uk/fonts/6a8730a9c57227effd13174fa12c9669/GuardianTextEgyptianWeb.ttf.json" data-cache-file-hinted-cleartype-ttf="https://assets.guim.co.uk/fonts/c4054e9bdace03f04c410ab6c3c4d251/GuardianTextEgyptianWebCleartypeHinted.ttf.json" data-cache-file-hinted-auto-ttf="https://assets.guim.co.uk/fonts/7ebc6aee620382ba44f94d663aac46be/GuardianTextEgyptianWebAutoHinted.ttf.json"></style>
<style class="webfont" data-cache-name="GuardianSansWeb" data-cache-file-woff2="https://assets.guim.co.uk/fonts/0a5b897d26a290d80ef71316a49a31e2/GuardianSansWeb.woff2.json" data-cache-file-hinted-cleartype-woff2="https://assets.guim.co.uk/fonts/f2463ec9413fa90b3349736bbaf506e5/GuardianSansWebCleartypeHinted.woff2.json" data-cache-file-hinted-auto-woff2="https://assets.guim.co.uk/fonts/c6160564c25bc9b1ef85ede4a1f32a0e/GuardianSansWebAutoHinted.woff2.json" data-cache-file-woff="https://assets.guim.co.uk/fonts/34121e4858440b40aa458d7b001e50fd/GuardianSansWeb.woff.json" data-cache-file-hinted-cleartype-woff="https://assets.guim.co.uk/fonts/7723b48f7c73c9c4d5301f6da8156e68/GuardianSansWebCleartypeHinted.woff.json" data-cache-file-hinted-auto-woff="https://assets.guim.co.uk/fonts/ea66376e7711e4cf3ac9152cfa9be1c5/GuardianSansWebAutoHinted.woff.json" data-cache-file-ttf="https://assets.guim.co.uk/fonts/6d102ed1b30b27f97de6e29d30bd3198/GuardianSansWeb.ttf.json" data-cache-file-hinted-cleartype-ttf="https://assets.guim.co.uk/fonts/24c60fb8c15f931e53eb4445e5545f76/GuardianSansWebCleartypeHinted.ttf.json" data-cache-file-hinted-auto-ttf="https://assets.guim.co.uk/fonts/24c8d16b6f339c0394ba6caab6d4ed58/GuardianSansWebAutoHinted.ttf.json"></style>
<style class="webfont" data-cache-name="GuardianTextSansWeb" data-cache-file-woff2="https://assets.guim.co.uk/fonts/e98740f460023b3b3b3137589c40db35/GuardianTextSansWeb.woff2.json" data-cache-file-hinted-cleartype-woff2="https://assets.guim.co.uk/fonts/31443178085917965e0fd5b89ecff788/GuardianTextSansWebCleartypeHinted.woff2.json" data-cache-file-hinted-auto-woff2="https://assets.guim.co.uk/fonts/1e08730fbd3200a61dfa77d9e6d645b6/GuardianTextSansWebAutoHinted.woff2.json" data-cache-file-woff="https://assets.guim.co.uk/fonts/68a6b1dc3e7af0aa14a2a0ba3839eea3/GuardianTextSansWeb.woff.json" data-cache-file-hinted-cleartype-woff="https://assets.guim.co.uk/fonts/997e56e52c9d9f28ab60a9786694af4b/GuardianTextSansWebCleartypeHinted.woff.json" data-cache-file-hinted-auto-woff="https://assets.guim.co.uk/fonts/73e92258e322d31f85cea2ffbf02cbb0/GuardianTextSansWebAutoHinted.woff.json" data-cache-file-ttf="https://assets.guim.co.uk/fonts/71a960886bc7e0d7d7c9b3483b347ab0/GuardianTextSansWeb.ttf.json" data-cache-file-hinted-cleartype-ttf="https://assets.guim.co.uk/fonts/1ec1f70d7bd618abc7ad43fd7e22d7f2/GuardianTextSansWebCleartypeHinted.ttf.json" data-cache-file-hinted-auto-ttf="https://assets.guim.co.uk/fonts/3a59896fe9b9cee9b2f5d3b7a086d481/GuardianTextSansWebAutoHinted.ttf.json"></style>
<script>window.console=window.console||undefined;</script>
<script id="gu">/*@cc_on
    @if (@_jscript_version <= 9)
(function(f){
    window.setTimeout = f(window.setTimeout);
    window.setInterval = f(window.setInterval);
})(function(f){return function(c,t){var a=[].slice.call(arguments,2);return f(function(){c.apply(this,a)},t)}});
    @end
@*/(function(window){var lastTime,vendors;if(!window.requestAnimationFrame){lastTime=0;vendors=["ms","moz","webkit","o"];for(var x=0;x<vendors.length&&!window.requestAnimationFrame;++x){window.requestAnimationFrame=window[vendors[x]+"RequestAnimationFrame"];window.cancelAnimationFrame=window[vendors[x]+"CancelAnimationFrame"]||window[vendors[x]+"CancelRequestAnimationFrame"]}window.requestAnimationFrame=function(callback,element){var currTime=(new Date).getTime();var timeToCall=Math.max(0,16-(currTime-lastTime));var id=window.setTimeout(function(){callback(currTime+timeToCall)},timeToCall);lastTime=currTime+timeToCall;return id}}if(!window.cancelAnimationFrame)window.cancelAnimationFrame=function(id){clearTimeout(id)}})(window);(function(window,document){var weShouldPolyfill=!("open"in document.createElement("details"));function toggleDetailsState(details){if(details.hasAttribute("open"))details.removeAttribute("open");else details.setAttribute("open","open")}function handleEvent(event){var targetNode=event.target;while(targetNode.nodeName.toLowerCase()!=="summary"&&targetNode!==document)targetNode=targetNode.parentNode;if(targetNode.nodeName.toLowerCase()==="summary")toggleDetailsState(targetNode.parentNode)}function bindEvents(){document.addEventListener("click",handleEvent,true);document.addEventListener("keypress",function(event){if(event.key&&(event.key===" "||event.key==="Enter"))handleEvent(event);else if(event.keyCode===32||event.keyCode===13)handleEvent(event)},true)}function appendCss(){if(document.querySelector("#details-polyfill-css")===null){var style=document.createElement("style");style.id="details-polyfill-css";style.textContent="details:not([open]) \x3e *:not(summary) {display: none;}";document.head.insertBefore(style,document.head.firstChild)}}if(weShouldPolyfill){bindEvents();appendCss()}})(window,document);(function(window){var location=window.location;var hash=location.hash;var navigator=window.navigator;var platform=navigator.platform;var isFront=true;var enhancedKey="gu.prefs.enhanced";var preferEnhanced;try{preferEnhanced=JSON.parse(localStorage.getItem(enhancedKey)).value}catch(e){preferEnhanced=null}function mustEnhance(){if(hash==="#enhanced"||hash==="#"+enhancedKey+"\x3dtrue")return true;if(preferEnhanced)return true;return false}function mustNotEnhance(){return hash==="#standard"||hash==="#"+enhancedKey+"\x3dfalse"}function couldEnhance(){return preferEnhanced!==false}function weWantToEnhance(){if(isOlderIOSDevice())return false;if(isFront)return!isIpad();return true}function isOlderIOSDevice(){return/.*(iPhone|iPad|iPod; CPU) OS ([34567])_\d+.*/.test(navigator.userAgent)}function isIpad(){return platform==="iPad"}window.shouldEnhance=mustNotEnhance()?false:mustEnhance()?true:couldEnhance()&&weWantToEnhance()})(window);var isModernBrowser="querySelector"in document&&"addEventListener"in window&&"localStorage"in window&&"sessionStorage"in window&&"bind"in Function&&(("XMLHttpRequest"in window&&"withCredentials"in new XMLHttpRequest())||"XDomainRequest"in window);window.guardian={isModernBrowser:isModernBrowser,isEnhanced:window.shouldEnhance&&isModernBrowser,css:{loaded:false},polyfilled:false,adBlockers:{active:undefined,onDetect:[]},config:{"page":{"avatarApiUrl":"https://avatar.theguardian.com","membershipUrl":"https://membership.theguardian.com","isProd":true,"discussionFrontendUrl":"","membershipAccess":"","allowUserGeneratedContent":false,"forecastsapiurl":"/weatherapi/forecast","idOAuthUrl":"https://oauth.theguardian.com","supportUrl":"https://support.theguardian.com","webTitle":"Network Front","isFront":true,"idWebAppUrl":"https://oauth.theguardian.com","googleSearchUrl":"//www.google.co.uk/cse/cse.js","googleSearchId":"007466294097402385199:m2ealvuxh1i","idUrl":"https://profile.theguardian.com","omnitureAmpAccount":"guardiangu-thirdpartyapps","dfpAdUnitRoot":"theguardian.com","host":"https://www.theguardian.com","fbAppId":"180444840287","dfpAccountId":"59666047","plistaPublicApiKey":"462925f4f131001fd974bebe","cardStyle":"","adUnit":"/59666047/theguardian.com/international/front/ng","discussionApiUrl":"https://discussion.theguardian.com/discussion-api","ophanEmbedJsUrl":"//j.ophan.co.uk/ophan.embed","edition":"INT","userAttributesApiUrl":"https://members-data-api.theguardian.com/user-attributes","discussionApiClientHeader":"nextgen","hasSuperStickyBanner":false,"section":"international","dfpHost":"pubads.g.doubleclick.net","weatherapiurl":"/weatherapi/city","sentryPublicApiKey":"344003a8d11c41d8800fbad8383fdc50","pageId":"international","sonobiHeaderBiddingJsUrl":"//api.nextgen.guardianapps.co.uk/morpheus.theguardian.12919.js","beaconUrl":"//beacon.gu-web.net","discussionD2Uid":"zHoBy6HNKsk","ophanJsUrl":"//j.ophan.co.uk/ophan.ng","keywordIds":"international/international","contentType":"Network Front","isDev":false,"facebookIaAdUnitRoot":"facebook-instant-articles","stripePublicToken":"pk_live_2O6zPMHXNs2AGea4bAmq5R7Z","omnitureAccount":"guardiangu-network","locationapiurl":"/weatherapi/locations?query=","isPaidContent":false,"externalEmbedHost":"https://embed.theguardian.com","thirdPartyAppsAccount":"guardiangu-thirdpartyapps","ajaxUrl":"https://api.nextgen.guardianapps.co.uk","keywords":"Network Front","mobileAppsAdUnitRoot":"beta-guardian-app","hasPageSkin":false,"requiresMembershipAccess":false,"revisionNumber":"ef486712273a9c8d41038974bd533887565c6af7","assetsPath":"https://assets.guim.co.uk/","avatarImagesUrl":"https://avatar.guim.co.uk","sentryHost":"app.getsentry.com/35463","buildNumber":"13737","sharedAdTargeting":{"ct":"network-front","url":"/international","edition":"int","p":"ng","k":["international"]},"onwardWebSocket":"ws://api.nextgen.guardianapps.co.uk/recently-published","shouldHideAdverts":false,"googletagJsUrl":"//www.googletagservices.com/tag/js/gpt.js","idApiUrl":"https://idapi.theguardian.com","isPreview":false},"switches":{"boostGaUserTimingFidelity":false,"thirdPartyEmbedTracking":true,"scrollDepth":true,"enableSentryReporting":true,"ophan":true,"discussionPageSize":true,"externalVideoEmbeds":true,"relatedContent":true,"autoRefresh":true,"lazyLoadContainers":true,"enableDiscussionSwitch":true,"registerWithPhone":false,"discussionAllowAnonymousRecommendsSwitch":false,"discussionAllPageSize":true,"sonobiHeaderBidding":true,"kruxVideoTracking":false,"adblock":false,"membershipEngagementBannerBlockAu":false,"membershipEngagementBannerBlockUs":false,"membershipEngagementBannerBlockUk":false,"membershipEngagementBanner":true,"simpleReach":true,"remarketing":true,"doubleclickYoutubeAdFree":true,"krux":true,"adomik":true,"imrWorldwide":true,"tourismAustralia":true,"adFreeStrictExpiryEnforcement":false,"adFreeSubscriptionTrial":true,"blockIas":true,"surveys":false,"keepVideoAdSlotsOpen":false,"commercial":true,"abOutstreamFrequencyCap":false,"abAcquisitionsEpicThankYou":true,"abAcquisitionsEpicAlwaysAskElection":false,"abAcquisitionsEpicAlwaysAskIfTagged":true,"abPaidContentVsOutbrain2":false,"abAcquisitionsElectionInteractiveSlice":true,"abAcquisitionsInteractiveEnd":true,"abAcquisitionsEpicLiveblog":true,"abContributionsEpicAskFourEarning":true,"abContributionsEpicAlwaysAskStrategy":true,"abJavascriptRenderingControl":true,"abJavascriptRenderingVariant":true,"abNewDesktopHeaderControl":false,"abNewDesktopHeaderVariant":true,"commercialClientLogging":true,"ukSupporterTrafficToNewSupportFrontend":true,"useTailorEndpoints":true,"targeting":true,"sharingComments":true,"smartAppBanner":true,"emailSignupEuRef":true,"emailSignupLabNotes":true,"emailInArticleOutbrain":true,"emailInArticleGtoday":true,"emailInArticle":true,"emailInlineInFooter":true,"crosswordSvgThumbnails":true,"historyTags":true,"weather":true,"breakingNews":true,"enhancedMediaPlayer":true,"enhanceTweets":true,"idCookieRefresh":true,"idProfileNavigation":true,"googleSearch":true,"webFonts":true,"geoMostPopular":true,"plistaForOutbrainAu":true,"outbrain":true,"exploreMainMedia":true,"serverShareCounts":true},"tests":{"abJavascriptRenderingVariant":"variant"},"modules":{},"images":{"commercial":{"ab-icon":"https:\/\/assets.guim.co.uk\/images\/commercial\/504a6bc5825d269eaf8ffdc77ad1f5b8\/ab-icon.png","abp-icon":"https:\/\/assets.guim.co.uk\/images\/commercial\/15fa8f9f99ce2a6b804097d348622727\/abp-icon.png","abp-whitelist-instruction-chrome":"https:\/\/assets.guim.co.uk\/images\/commercial\/862b03a008061af5c3b77c1f2dd52dd4\/ad-block-instructions-chrome.png"},"membership":{"adblock-coins":"https:\/\/assets.guim.co.uk\/images\/membership\/6b077732beb2d9bf9dcbb78c953a3de5\/adblock-coins.png","adblock-coins-us":"https:\/\/assets.guim.co.uk\/images\/membership\/103510d0b88a6444f383b492d556c539\/adblock-coins-us.png"},"acquisitions":{"paypal-and-credit-card":"https:\/\/assets.guim.co.uk\/images\/acquisitions\/f11636cbbeea81079eff3d092f4a9539\/paypal-and-credit-card.png","usa-flag":"https:\/\/assets.guim.co.uk\/images\/acquisitions\/1193722b05513fcafad78cf3d44cf293\/usa-flag.png"}},"stylesheets":{"fonts":{"hintingCleartype":{"kerningOn":"https:\/\/assets.guim.co.uk\/stylesheets\/9f78997fd3b37533007e55334c9e7c8b\/webfonts-hinting-cleartype-kerning-on.css"},"hintingOff":{"kerningOn":"https:\/\/assets.guim.co.uk\/stylesheets\/50441b3bda46af4af85a3f0a1b61f8bb\/webfonts-hinting-off-kerning-on.css"},"hintingAuto":{"kerningOn":"https:\/\/assets.guim.co.uk\/stylesheets\/4f3512b7ca058a60dea4f4b994ab4ebc\/webfonts-hinting-auto-kerning-on.css"}}},"googleAnalytics":{"trackers":{"editorialTest":"guardianTestPropertyTracker","editorialProd":"allEditorialPropertyTracker","editorial":"allEditorialPropertyTracker"},"timingEvents":[]},"libs":{"googletag":"\/\/www.googletagservices.com\/tag\/js\/gpt.js","sonobi":"\/\/api.nextgen.guardianapps.co.uk\/morpheus.theguardian.12919.js"}}};if(window.esi&&window.esi.viewId){window.guardian.config.ophan={pageViewId:window.esi.viewId};}else{window.guardian.config.ophan={pageViewId:new Date().getTime().toString(36)+'xxxxxxxxxxxx'.replace(/x/g,function(){return Math.floor(Math.random()*36).toString(36);})};}/*@cc_on
@if (@_jscript_version <= 9)
    guardian.config.page.ajaxUrl = guardian.config.page.ajaxUrl.replace(/^https:/, '');
@end
@*/(function(documentElement,window,navigator){var docClass=documentElement.className;var testCssSupportForPropertyAndValue=function(supportsSupports){return supportsSupports?nativeCSSSupports:shimCSSSupports()}("CSS"in window&&"supports"in window.CSS);function nativeCSSSupports(prop,value){return window.CSS.supports(prop,value)}function shimCSSSupports(){var cssToDOMRegExp=/([a-z])-([a-z])/g;var testElem=document.createElement("test");function cssToDOM(name){return name.replace(cssToDOMRegExp,cssToDOMReplacer).replace(/^-/,"")}function cssToDOMReplacer(str,m1,m2){return m1+m2.toUpperCase()}return function(prop,value){try{prop=cssToDOM(prop);var originalValue=testElem.style[prop];if(originalValue===undefined)return false;if(originalValue===value)return true;testElem.style[prop]=value;return testElem.style[prop]!==originalValue}catch(e){return false}}}function testAndAddClass(tests){docClass+=" "+tests.map(function(test){return(test.props.some(function(prop){return test.values.some(function(value){return testCssSupportForPropertyAndValue(prop,value)})})?"has-":"has-no-")+test.feature}).join(" ")}function getCookieValue(name){var val=document.cookie.match("(^|;)\\s*"+name+"\\s*\x3d\\s*([^;]+)");return val?val.pop():undefined}function isRecentContributor(){var value=getCookieValue("gu.contributions.contrib-timestamp");if(!value)return false;var now=(new Date).getTime();var lastContribution=(new Date(value)).getTime();var diffDays=Math.ceil((now-lastContribution)/(1E3*3600*24));return diffDays<=180}function isPayingMember(){return getCookieValue("gu_paying_member")==="true"}if(!!document.createElementNS&&!!document.createElementNS("http://www.w3.org/2000/svg","svg").createSVGRect)docClass+=" svg";else docClass+=" no-svg";testAndAddClass([{feature:"flex",props:["flex","-ms-flex","-webkit-flex","-moz-box-flex","-webkit-box-flex"],values:["inherit"]},{feature:"flex-wrap",props:["flex-wrap","-ms-flex-wrap","-webkit-flex-wrap"],values:["inherit"]},{feature:"fixed",props:["position"],values:["fixed"]},{feature:"sticky",props:["position"],values:["sticky","-webkit-sticky"]}]);if(window.guardian.isEnhanced)docClass=docClass.replace(/\bis-not-modern\b/g,"is-modern");if(window.location.hash!=="#no-kern")docClass+=" should-kern";var baseFontSize=null;if("getComputedStyle"in window)baseFontSize=window.getComputedStyle(documentElement).getPropertyValue("font-size");if(baseFontSize&&parseInt(baseFontSize,10)!==16)documentElement.style.fontSize=baseFontSize;if(isPayingMember())docClass+=" is-paying-member";if(isRecentContributor())docClass+=" is-recent-contributor";documentElement.className=docClass.replace(/\bjs-off\b/g,"js-on")})(document.documentElement,window,navigator);(function(window,document){var ua=navigator.userAgent;var fontHinting=function(){var windowsNT=/Windows NT (\d\.\d+)/.exec(ua);var hinting="Off";try{if(windowsNT){var version=parseFloat(windowsNT[1],10);if(version>=5.1&&version<=6.1)if(/Chrome/.exec(ua)&&version<6)hinting="Auto";else hinting="Cleartype"}}catch(e){}return hinting}();function loadFontsFromStorage(){try{if("localStorage"in window){var saveFont=function(fontName,fontHash,css){for(var i=0,totalItems=localStorage.length;i<totalItems-1;i++){var key=localStorage.key(i);if(key.indexOf(fontStorageKey(fontName))!==-1){localStorage.removeItem(key);break}}localStorage.setItem(fontStorageKey(fontName,fontHash),JSON.stringify({value:css}))};var fetchFont=function(url,el,fontName,fontHash){var xhr=new XMLHttpRequest;this["guFont"]=function(fontData){return fontData.css};xhr.open("GET",url,true);xhr.onreadystatechange=function(){if(xhr.readyState===4&&xhr.status===200){var css=eval(xhr.responseText);useFont(el,css);saveFont(fontName,fontHash,css)}};xhr.send()};var useFont=function(el,css){el.innerHTML=css};var fontStorageKey=function(fontName,fontHash){fontHash=fontHash===undefined?"":fontHash;return"gu.fonts."+fontName+"."+fontHash};var fontFormat=function(){var formatStorageKey="gu.fonts.format";var format=localStorage.getItem(formatStorageKey);function supportsWoff2(){if("FontFace"in window)try{var f=new window.FontFace("t",'url("data:application/font-woff2,") format("woff2")',{});f.load()["catch"](function(){});if(f.status==="loading")return true}catch(e){}if(!/edge\/([0-9]+)/.test(ua.toLowerCase())){var browser=/(chrome|firefox)\/([0-9]+)/.exec(ua.toLowerCase());var supportsWoff2$0={"chrome":36,"firefox":39};return!!browser&&supportsWoff2$0[browser[1]]<parseInt(browser[2],10)}return false}if(/value/.test(format)){format=JSON.parse(format).value;localStorage.setItem(formatStorageKey,format)}if(!format){format=supportsWoff2()?"woff2":ua.indexOf("android")>-1?"ttf":"woff";localStorage.setItem(formatStorageKey,format)}return format}();var fonts=document.querySelectorAll(".webfont");var hinting=fontHinting==="Off"?"":"hinted-"+fontHinting+"-";var urlAttribute="data-cache-file-"+hinting+fontFormat;for(var i=0,j=fonts.length;i<j;++i){var font=fonts[i];var fontURL=font.getAttribute(urlAttribute);var fontInfo=fontURL.match(/fonts\/([^/]*?)\/?([^/]*)\.(woff2|woff|ttf).json$/);var fontName=fontInfo[2];var fontHash=fontInfo[1];var fontData=localStorage.getItem(fontStorageKey(fontName,fontHash));if(fontData)useFont(font,JSON.parse(fontData).value);else fetchFont(fontURL,font,fontName,fontHash)}return true}}catch(e){}return false}function loadFontsAsynchronously(){try{var scripts=document.getElementsByTagName("script");var thisScript=scripts[scripts.length-1];var fonts=document.createElement("link");fonts.rel="stylesheet";fonts.className="webfonts";fonts.href=window.guardian.config.stylesheets.fonts["hinting"+fontHinting].kerningOn;window.setTimeout(function(){thisScript.parentNode.insertBefore(fonts,thisScript)})}catch(e){}}function fontSmoothingEnabled(){try{var saveFontSmoothing=function(state){state=state?"on":"off";document.cookie="GU_fonts_smoothing\x3d "+state+"; domain\x3d"+location.hostname+"; path\x3d/; max-age\x3d"+60*60*24*30};if(document.cookie.indexOf("GU_fonts_smoothing")!==-1&&window.location.hash!=="#check-smoothing")return document.cookie.indexOf("GU_fonts_smoothing\x3don")!==-1;if(/Windows NT (\d\.\d+)/.exec(ua)&&!/MSIE|Trident/.exec(ua)){try{var canvasNode=document.createElement("canvas");canvasNode.width="35";canvasNode.height="35";canvasNode.style.display="none";document.documentElement.appendChild(canvasNode);var ctx=canvasNode.getContext("2d");ctx.textBaseline="top";ctx.font="32px Arial";ctx.fillStyle="black";ctx.strokeStyle="black";ctx.fillText("@",0,0);for(var x=0;x<=16;x++)for(var y=0;y<=16;y++){var alpha=ctx.getImageData(x,y,1,1).data[3];if(alpha>0&&alpha<255){saveFontSmoothing(true);return true}}}catch(e){}saveFontSmoothing(false);return false}else return true}catch(e$1){}}var fontCookie="GU_fonts\x3doff; domain\x3d"+location.hostname+"; path\x3d/";function disableFonts(){document.cookie=fontCookie+"; max-age\x3d"+60*60*24*365}function enableFonts(){document.cookie=fontCookie+"; expires\x3dThu, 01 Jan 1970 00:00:00 GMT"}function checkUserFontDisabling(){if(window.location.hash==="#fonts-off")disableFonts();else if(window.location.hash==="#fonts-on"||window.location.hash==="#check-smoothing")enableFonts()}var fontsEnabled=document.cookie.indexOf("GU_fonts\x3doff")===-1;function loadFonts(){checkUserFontDisabling();if(fontsEnabled)if(fontSmoothingEnabled())loadFontsFromStorage()||loadFontsAsynchronously();else disableFonts()}loadFonts()})(window,document);(function(styleSheetLinks,documentStyleSheets){function setMedia(styleSheet){for(var i=0,totalSheets=documentStyleSheets.length;i<totalSheets;i++){var sheet=documentStyleSheets[i];if(sheet.href&&sheet.href.indexOf(styleSheet.href)>-1){styleSheet.media="screen";window.guardian.css.loaded=true;try{window.guardian.css.onLoad()}catch(e){}return true}}setTimeout(function(){setMedia(styleSheet)})}function useCss(){for(var i=0,totalStyleSheetLinks=styleSheetLinks.length;i<totalStyleSheetLinks;i++)if(styleSheetLinks[i].getAttribute("media")==="only x")setMedia(styleSheetLinks[i])}useCss()})(document.getElementsByTagName("link"),window.document.styleSheets);function guardianPolyfilled(){try{window.guardian.polyfilled=true}catch(e){}}(function(document,window){var src;var script;var pendingScripts=[];var firstScript=document.scripts[0];var scripts=["https://assets.guim.co.uk/polyfill.io/v2/polyfill.min.js?rum\x3d0\x26features\x3des6,es7,es2017,default-3.6,HTMLPictureElement\x26flags\x3dgated\x26callback\x3dguardianPolyfilled","https://assets.guim.co.uk/javascripts/f8d727c25df3bd9dcfeb/graun.standard.js"];function stateChange(){var pendingScript;while(pendingScripts[0]&&pendingScripts[0].readyState=="loaded"){pendingScript=pendingScripts.shift();pendingScript.onreadystatechange=null;firstScript.parentNode.insertBefore(pendingScript,firstScript)}}while(src=scripts.shift())if("async"in firstScript){script=document.createElement("script");script.async=false;script.src=src;document.head.appendChild(script)}else if(firstScript.readyState){script=document.createElement("script");pendingScripts.push(script);script.onreadystatechange=stateChange;script.src=src}else document.write('\x3cscript src\x3d"'+src+'" defer\x3e\x3c/'+"script\x3e")})(document,window);</script>
</head>
<body id="top" class="" itemscope itemtype="http://schema.org/WebPage">
<div class="site-message js-site-message is-hidden" data-link-name="release message" role="dialog" aria-label="welcome" aria-describedby="site-message__message">
<div class="gs-container">
<div class="site-message__inner js-site-message-inner">
<div class="site-message__media">
<span class="inline-marque-36 inline-icon u-vertical-align-middle-icon">
<svg width="36" height="36" viewbox="0 0 36 36" class="u-vertical-align-middle-icon__svg inline-marque-36__svg inline-icon__svg">
<path d="M21.3 8.8c0-4.9-1.5-5.7-3.3-5.7-1.8 0-3.2.7-3.2 5.7s1.5 5.5 3.2 5.5c1.8-.1 3.3-.6 3.3-5.5m-6.5 18.8c-2.3 0-2.9 1.7-2.9 2.9 0 1.8 1.6 3.4 6.3 3.4 5.3 0 6.8-1.5 6.8-3.4 0-1.7-1.3-2.9-3.4-2.9h-6.8zM10.5 2.4C4.3 5.2 0 11.4 0 18.7c0 4.9 2 9.4 5.2 12.6V31c0-3.2 3.1-4.4 5.9-5-2.6-.6-3.9-2.5-3.9-4.4 0-2.6 2.9-4.8 4.3-5.8l-.2-.1c-2.5-1.4-4.1-3.8-4.1-7 0-2.7 1.2-4.9 3.3-6.3M36 18.8C36 11.4 31.5 5 25.1 2.3c2.1 1.4 3.4 3.5 3.5 6.3l.1.6c0 5.4-4.4 8.2-10.7 8.2-1.6 0-2.7-.1-4.1-.5-.6.4-1.1 1.1-1.1 1.8 0 .9.8 1.6 1.8 1.6h8.8c5.5 0 8.2 2.2 8.2 7.1 0 1.6-.3 3.1-1 4.3 3.3-3.4 5.4-7.9 5.4-12.9"/>
</svg>
</span>
</div>
<div class="site-message__copy js-site-message-copy u-cf">
</div>
<div class="site-message__close">
<button class="site-message__close-btn js-site-message-close" data-link-name="hide release message">
<span class="u-h">Close</span>
<span class="inline-close inline-icon inline-close--small">
<svg width="18" height="18" viewbox="0 0 18 18" class="inline-close--small__svg inline-close__svg inline-icon__svg">
<path d="M7.5 9L1 2l1-1 7 6.5L16 1l1 1-6.5 7 6.5 7-1 1-7-6.5L2 17l-1-1 6.5-7z"/>
</svg>
</span>
</button>
</div>
</div>
</div>
</div>
<a class="u-h skip" href="#maincontent" data-link-name="skip : main content">Skip to main content</a>
<div id="bannerandheader">
<div class="top-banner-ad-container js-top-banner">
<div id="dfp-ad--top-above-nav" class="js-ad-slot ad-slot ad-slot--top-above-nav ad-slot--top-banner-ad ad-slot--top-banner-ad-desktop " data-link-name="ad slot top-above-nav" data-name="top-above-nav" data-tablet="1,1|2,2|728,90|88,71|fluid" data-desktop="1,1|2,2|728,90|940,230|900,250|970,250|88,71|fluid"> </div>
</div>
<header class="new-header" role="banner">
<nav class="new-header__inner gs-container" data-component="nav2" aria-label="Guardian sections">
<a href="https://www.theguardian.com/international" class="new-header__logo" data-link-name="nav2 : logo">
<span class="u-h">The Guardian - Back to home</span>
<span class="inline-guardian-logo-160 inline-logo new-header__logo">
<svg width="160" height="30" viewbox="0 0 320 60" class="new-header__logo__svg inline-guardian-logo-160__svg inline-logo__svg">
<path fill="#fff" d="M284 45h16v-3l-3-1.5v-20c1.2-.9 2.8-1.1 4.3-1.1 2.8 0 3.8.9 3.8 4.1v17l-3 1.5v3h16v-3l-3-1.5v-19c0-5.7-2.2-8.3-7.2-8.3-4.1 0-8.1 1.5-10.8 4V13h-1l-12.4 2.2v2.7l3.4 1.6v21l-3 1.5-.1 3zM245.3.4c-3 0-5.4 2.4-5.4 5.5 0 3 2.4 5.4 5.4 5.4 2.9 0 5.4-2.4 5.4-5.4-.1-3.1-2.5-5.5-5.4-5.5zM237 15.1v2.8l3 1.6v20.9l-3 1.5v3h16v-3l-3-1.5V13.1h-1l-12 2zM222.9 39c-.7.6-1.6 1.1-3.1 1.1-4 0-5.9-3.3-5.9-10.9 0-8.7 2.4-11.7 5.6-11.7 1.8 0 2.7.6 3.4 1.4V39zm0-24.5c-1.2-.9-3.2-1.4-4.9-1.4-7.4 0-14.5 4.3-14.5 16.8 0 11.9 7.1 15.7 11.8 15.7 3.8 0 6.4-1.7 7.6-3.4h.3v3.3h.9l11.9-1.4v-2.3l-3.2-1.8V.6h-.8l-12.6 2v2.8l3.4 1.6v7.5h.1zM181 18l3 1.5v20.9l-3 1.5v3h17v-3l-3.9-1.5V24.1c1.8-1.4 4-1.9 6.7-1.9.9 0 1.6.2 2.2.3v-9c-.3-.1-.7-.2-1.2-.2-3.3 0-5.9 2.1-7.7 6.2V13H193l-12 2v3zm-19.3-.8c3.9 0 5 2 5 5.9v3.5l-5.8 1.1c-5.9 1.1-10.4 3-10.4 9.3 0 5.1 3.5 8.7 8.3 8.7 3.8 0 7.4-1.7 8.7-4.4h.3c.5 3.3 3.3 4.4 6.4 4.4 2.4 0 4.8-.6 5.7-1.6v-2l-3-1.5v-18c0-6.9-5-9.4-13.1-9.4-5.3 0-8.8 1.4-11.6 2.7v7.8h4.7l2-6c.9-.5 2.4-.5 2.8-.5zm2.3 22.9c-1.9 0-4-1.1-4-4.6 0-2.4 2.4-4.6 4.8-5l2.2-.5v8.5s-1.9 1.6-3 1.6zm100.8-22.9c3.9 0 5 2 5 5.9v3.5l-5.8 1.1c-5.9 1.1-10.4 3-10.4 9.3 0 5.1 3.5 8.7 8.3 8.7 3.8 0 7.4-1.7 8.7-4.4h.3c.5 3.3 3.3 4.4 6.4 4.4 2.4 0 4.8-.6 5.7-1.6v-2l-3-1.5v-18c0-6.9-5-9.4-13.1-9.4-5.3 0-8.8 1.4-11.6 2.7v7.8h4.7l2-6c.8-.5 2.3-.5 2.8-.5zm2.2 22.9c-1.9 0-4-1.1-4-4.6 0-2.4 2.4-4.6 4.8-5l2.2-.5v8.5s-1.9 1.6-3 1.6zm-138.7 5.6c.4 0 .9 0 1.3-.1 3.5-.3 6.7-2 8.4-4.2v4.1l12-1.5v-2l-3-2V13h-1l-11.9 2.3v2.8l3.9 1.6V38c-1.1.8-2.4 1.3-4.2 1.3-2.5 0-4.8-.8-4.8-4.3V13h-1l-12 2.5v2.6l4 1.6V36c0 5.4 2.2 9.7 8.3 9.7zM96 38c-1.2 0-2.5-.8-2.5-1.9 0-.8.6-1.7 1.3-2.3 1.6.5 3 .6 5 .6 7.8 0 13.2-3.7 13.2-10.4 0-3-1.3-4.6-3.2-6.4L115 19v-6l-8.2 1.6c-1.9-.7-4.5-1.6-7-1.6-7.8 0-13.2 4.1-13.2 10.8 0 4.1 2 7.1 5 8.8l.3.2c-1.7 1.2-5.3 4-5.3 7.2 0 2.4 1.5 4.8 4.8 5.5C88 46.3 84 48 84 52c0 4.1 5.9 8 15.5 8 11.8 0 16.5-5.7 16.5-13 0-6.1-2.8-9-9.5-9H96zm7.5-14c0 5.7-1.3 6.5-3.5 6.5s-4-.8-4-6.5c0-5.8 1.8-7.5 4-7.5s3.5 2 3.5 7.5zM92 50.9c.1-1.5 1.1-3.4 3.7-3.6h8.6c2.5 0 3.7 2 3.7 3.6 0 3.2-2 4.4-8.3 4.4-5.5 0-7.8-2.2-7.7-4.4z"/>
<path fill="#AADCE6" d="M83 30c0-13-5.1-16.9-13-16.9-9 0-15 6.2-15 16.4 0 10.5 5.5 16.2 15.8 16.2 5.6 0 9.8-2.7 11.2-4.7v-3c-2.1.7-3.9 1.2-7.8 1.2-5.4 0-9.2-3.2-9.2-9.2h18zM69.9 16.6c2.5 0 3.8 1.9 3.8 9.6l-8.4.5c.2-7.9 1.8-10.1 4.6-10.1zM37 45v-3l-3-1.5V21c1.2-.9 3.3-1.7 4.8-1.7 2.8 0 4.3 1.5 4.2 4.2v17L40 42v3h16v-3l-3-1.5v-19c0-5.7-3.3-8.3-7.7-8.3-4.1 0-8.6 1.3-11.3 3.8V0h-1L21 2v3l4 1.5v34L22 42v3h15zM4 36.4c0 5.7 2.8 9.3 8.9 9.3 3.1 0 6.5-.8 8.4-2.3v-3.8c-.8.3-2.2.5-3.3.5-2.9 0-4-1.6-4-4.6V19h7v-5h-7V6.5L4 8v6l-4 1v4h4v17.4z"/>
</svg>
</span>
</a>
<div class="new-header__cta-container hide-until-mobile">
<a class="header-cta-item header-cta-item--primary" data-link-name="nav2 : supporter-cta" data-edition="int" href="https://membership.theguardian.com/supporter?INTCMP=mem_int_web_newheader&amp;acquisitionData=%7B&quot;source&quot;:&quot;GUARDIAN_WEB&quot;,&quot;componentType&quot;:&quot;ACQUISITIONS_HEADER&quot;,&quot;componentId&quot;:&quot;mem_int_web_newheader&quot;,&quot;campaignCode&quot;:&quot;mem_int_web_newheader&quot;%7D">
<span class="header-cta-item__label">
become a <span class="header-cta-item__new-line">supporter</span>
</span>
</a>
<a class="header-cta-item hide-until-tablet header-cta-item--secondary js-change-subscribe-link" data-link-name="nav2 : subscribe-cta" data-edition="int" href="https://subscribe.theguardian.com?INTCMP=subs_int_web_newheader&amp;acquisitionData=%7B&quot;source&quot;:&quot;GUARDIAN_WEB&quot;,&quot;componentType&quot;:&quot;ACQUISITIONS_HEADER&quot;,&quot;componentId&quot;:&quot;subs_int_web_newheader&quot;,&quot;campaignCode&quot;:&quot;subs_int_web_newheader&quot;%7D">
<span class="header-cta-item__label">
subscribe
</span>
</a>
<a class="header-cta-item hide-until-tablet header-cta-item--secondary" data-link-name="nav2 : job-cta" data-edition="int" href="https://jobs.theguardian.com?INTCMP=jobs_int_web_newheader">
<span class="header-cta-item__label">
<span class="hide-until-tablet">find a job</span>
<span class="hide-from-tablet">jobs</span>
</span>
</a>
</div>
<input type="checkbox" id="main-menu-toggle" class="veggie-burger-fallback js-enhance-checkbox u-h" aria-controls="main-menu">
<ul class="pillars">
<li class="pillars__item">
<a class="pillar-link pillar-link--current-section" href="https://www.theguardian.com/international" data-link-name="nav2 : primary : news">
news
</a>
</li>
<li class="pillars__item">
<a class="pillar-link" href="https://www.theguardian.com/uk/commentisfree" data-link-name="nav2 : primary : opinion">
opinion
</a>
</li>
<li class="pillars__item">
<a class="pillar-link" href="https://www.theguardian.com/uk/sport" data-link-name="nav2 : primary : sport">
sport
</a>
</li>
<li class="pillars__item">
<a class="pillar-link" href="https://www.theguardian.com/uk/culture" data-link-name="nav2 : primary : arts">
arts
</a>
</li>
<li class="pillars__item">
<a class="pillar-link" href="https://www.theguardian.com/uk/lifeandstyle" data-link-name="nav2 : primary : life">
life
</a>
</li>
</ul>
<label for="main-menu-toggle" class="veggie-burger js-change-link" tabindex="0" data-link-name="nav2 : veggie-burger : show">
<span class="veggie-burger__icon"></span>
<span class="veggie-burger__label">All sections</span>
</label>
<label for="main-menu-toggle" class="menu__overlay" aria-hidden="true" data-link-name="nav2 : overlay"></label>
<div class="menu js-main-menu" id="main-menu" aria-hidden="true">
<div class="menu__inner gs-container">
<ul class="menu-group menu-group--primary" role="menubar">
<li class="menu-item js-navigation-item" data-section-name="news" role="menuitem">
<button class="menu-item__title hide-on-desktop js-navigation-toggle" data-link-name="nav2 : secondary : news" aria-haspopup="true" aria-expanded="true">
<i class="menu-item__toggle"></i>
news
</button>
<ul class="menu-group menu-group--secondary" data-edition="int" aria-label="Submenu news" role="menu">
<li class="menu-item menu-item--home" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/international" data-link-name="nav2 : secondary : headlines">
<span class="inline-home inline-icon menu-item__icon">
<svg width="15" height="18" viewbox="0 0 15 18" class="menu-item__icon__svg inline-home__svg inline-icon__svg">
<path d="M7.9 0h-1L0 7v10.1l.9.9h4.2v-6.6h4.7V18h4.3l.9-1V7z"/>
</svg>
</span>
headlines
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/world" data-link-name="nav2 : secondary : world news">
world news
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/uk-news" data-link-name="nav2 : secondary : UK news">
UK news
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/science" data-link-name="nav2 : secondary : science">
science
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/cities" data-link-name="nav2 : secondary : cities">
cities
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/global-development" data-link-name="nav2 : secondary : global development">
global development
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/uk/technology" data-link-name="nav2 : secondary : tech">
tech
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/uk/business" data-link-name="nav2 : secondary : business">
business
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/uk/environment" data-link-name="nav2 : secondary : environment">
environment
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/tone/obituaries" data-link-name="nav2 : secondary : obituaries">
obituaries
</a>
</li>
</ul>
</li>
<li class="menu-item js-navigation-item" data-section-name="opinion" role="menuitem">
<button class="menu-item__title hide-on-desktop js-navigation-toggle" data-link-name="nav2 : secondary : opinion" aria-haspopup="true" aria-expanded="true">
<i class="menu-item__toggle"></i>
opinion
</button>
<ul class="menu-group menu-group--secondary" data-edition="int" aria-label="Submenu opinion" role="menu">
<li class="menu-item menu-item--home" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/uk/commentisfree" data-link-name="nav2 : secondary : opinion home">
<span class="inline-home inline-icon menu-item__icon">
<svg width="15" height="18" viewbox="0 0 15 18" class="menu-item__icon__svg inline-home__svg inline-icon__svg">
<path d="M7.9 0h-1L0 7v10.1l.9.9h4.2v-6.6h4.7V18h4.3l.9-1V7z"/>
</svg>
</span>
opinion home
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/profile/editorial" data-link-name="nav2 : secondary : the guardian view">
the guardian view
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/index/contributors" data-link-name="nav2 : secondary : columnists">
columnists
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/cartoons/archive" data-link-name="nav2 : secondary : cartoons">
cartoons
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/commentisfree/series/comment-is-free-weekly" data-link-name="nav2 : secondary : opinion videos">
opinion videos
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/tone/letters" data-link-name="nav2 : secondary : letters">
letters
</a>
</li>
</ul>
</li>
<li class="menu-item js-navigation-item" data-section-name="sport" role="menuitem">
<button class="menu-item__title hide-on-desktop js-navigation-toggle" data-link-name="nav2 : secondary : sport" aria-haspopup="true" aria-expanded="true">
<i class="menu-item__toggle"></i>
sport
</button>
<ul class="menu-group menu-group--secondary" data-edition="int" aria-label="Submenu sport" role="menu">
<li class="menu-item menu-item--home" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/uk/sport" data-link-name="nav2 : secondary : sport home">
<span class="inline-home inline-icon menu-item__icon">
<svg width="15" height="18" viewbox="0 0 15 18" class="menu-item__icon__svg inline-home__svg inline-icon__svg">
<path d="M7.9 0h-1L0 7v10.1l.9.9h4.2v-6.6h4.7V18h4.3l.9-1V7z"/>
</svg>
</span>
sport home
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/football" data-link-name="nav2 : secondary : football">
football
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/sport/rugby-union" data-link-name="nav2 : secondary : rugby union">
rugby union
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/sport/cricket" data-link-name="nav2 : secondary : cricket">
cricket
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/sport/tennis" data-link-name="nav2 : secondary : tennis">
tennis
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/sport/cycling" data-link-name="nav2 : secondary : cycling">
cycling
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/sport/formulaone" data-link-name="nav2 : secondary : F1">
F1
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/sport/golf" data-link-name="nav2 : secondary : golf">
golf
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/sport/us-sport" data-link-name="nav2 : secondary : US sports">
US sports
</a>
</li>
</ul>
</li>
<li class="menu-item js-navigation-item" data-section-name="arts" role="menuitem">
<button class="menu-item__title hide-on-desktop js-navigation-toggle" data-link-name="nav2 : secondary : arts" aria-haspopup="true" aria-expanded="true">
<i class="menu-item__toggle"></i>
arts
</button>
<ul class="menu-group menu-group--secondary" data-edition="int" aria-label="Submenu arts" role="menu">
<li class="menu-item menu-item--home" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/uk/culture" data-link-name="nav2 : secondary : culture home">
<span class="inline-home inline-icon menu-item__icon">
<svg width="15" height="18" viewbox="0 0 15 18" class="menu-item__icon__svg inline-home__svg inline-icon__svg">
<path d="M7.9 0h-1L0 7v10.1l.9.9h4.2v-6.6h4.7V18h4.3l.9-1V7z"/>
</svg>
</span>
culture home
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/books" data-link-name="nav2 : secondary : books">
books
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/music" data-link-name="nav2 : secondary : music">
music
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/uk/tv-and-radio" data-link-name="nav2 : secondary : tv &amp; radio">
tv &amp; radio
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/artanddesign" data-link-name="nav2 : secondary : art &amp; design">
art &amp; design
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/uk/film" data-link-name="nav2 : secondary : film">
film
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/technology/games" data-link-name="nav2 : secondary : games">
games
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/music/classicalmusicandopera" data-link-name="nav2 : secondary : classical">
classical
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/stage" data-link-name="nav2 : secondary : stage">
stage
</a>
</li>
</ul>
</li>
<li class="menu-item js-navigation-item" data-section-name="life" role="menuitem">
<button class="menu-item__title hide-on-desktop js-navigation-toggle" data-link-name="nav2 : secondary : life" aria-haspopup="true" aria-expanded="true">
<i class="menu-item__toggle"></i>
life
</button>
<ul class="menu-group menu-group--secondary" data-edition="int" aria-label="Submenu life" role="menu">
<li class="menu-item menu-item--home" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/uk/lifeandstyle" data-link-name="nav2 : secondary : lifestyle home">
<span class="inline-home inline-icon menu-item__icon">
<svg width="15" height="18" viewbox="0 0 15 18" class="menu-item__icon__svg inline-home__svg inline-icon__svg">
<path d="M7.9 0h-1L0 7v10.1l.9.9h4.2v-6.6h4.7V18h4.3l.9-1V7z"/>
</svg>
</span>
lifestyle home
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/fashion" data-link-name="nav2 : secondary : fashion">
fashion
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/lifeandstyle/food-and-drink" data-link-name="nav2 : secondary : food">
food
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/tone/recipes" data-link-name="nav2 : secondary : recipes">
recipes
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/lifeandstyle/love-and-sex" data-link-name="nav2 : secondary : love &amp; sex">
love &amp; sex
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/lifeandstyle/health-and-wellbeing" data-link-name="nav2 : secondary : health &amp; fitness">
health &amp; fitness
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/lifeandstyle/home-and-garden" data-link-name="nav2 : secondary : home &amp; garden">
home &amp; garden
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/lifeandstyle/women" data-link-name="nav2 : secondary : women">
women
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/lifeandstyle/family" data-link-name="nav2 : secondary : family">
family
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/uk/travel" data-link-name="nav2 : secondary : travel">
travel
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/uk/money" data-link-name="nav2 : secondary : money">
money
</a>
</li>
</ul>
</li>
</ul>
<div class="menu-group menu-group--search">
<form class="menu-search js-menu-search" action="https://www.google.co.uk/search">
<input type="text" name="q" class="menu-search__search-box js-menu-search-term" id="google-search" placeholder="search" data-link-name="nav2 : search">
<label class="menu-search__glass" for="google-search">
<span class="inline-search-36 inline-icon main-menu__icon main-menu__icon--search">
<svg width="18" height="18" viewbox="0 0 18 18" class="main-menu__icon__svg main-menu__icon--search__svg inline-search-36__svg inline-icon__svg">
<path d="M6.5 1.6c2.7 0 4.9 2.2 4.9 4.9s-2.2 4.9-4.9 4.9-4.9-2.2-4.9-4.9 2.2-4.9 4.9-4.9m0-1.6C2.9 0 0 2.9 0 6.5S2.9 13 6.5 13 13 10.1 13 6.5 10.1 0 6.5 0zm6.6 11.5l4.9 4.9-1.6 1.6-4.9-4.9v-.8l.8-.8h.8z"/>
</svg>
</span>
<span class="u-h">What term do you want to search?</span>
</label>
<button class="menu-search__submit" data-link-name="nav2 : search : submit" for="submit-google-search" type="submit">
<i class="right-arrow__icon"></i>
<span class="u-h">Search with google</span>
</button>
<input type="hidden" name="as_sitesearch" value="www.theguardian.com">
</form>
</div>
<ul class="menu-group menu-group--membership" role="menubar">
<li class="menu-item hide-on-desktop" data-edition="int" role="menuitem">
<a class="menu-item__title js-change-membership-item" href="https://membership.theguardian.com/supporter?INTCMP=mem_int_web_newheader&amp;acquisitionData=%7B&quot;source&quot;:&quot;GUARDIAN_WEB&quot;,&quot;componentType&quot;:&quot;ACQUISITIONS_HEADER&quot;,&quot;componentId&quot;:&quot;mem_int_web_newheader&quot;,&quot;campaignCode&quot;:&quot;mem_int_web_newheader&quot;%7D" data-link-name="nav2 : become a supporter">
become a supporter
</a>
</li>
<li class="menu-item hide-on-desktop" data-edition="int" role="menuitem">
<a class="menu-item__title js-change-membership-item" href="https://subscribe.theguardian.com?INTCMP=NGW_NEWHEADER_int_GU_SUBSCRIBE&amp;acquisitionData=%7B&quot;source&quot;:&quot;GUARDIAN_WEB&quot;,&quot;componentType&quot;:&quot;ACQUISITIONS_HEADER&quot;,&quot;componentId&quot;:&quot;NGW_NEWHEADER_int_GU_SUBSCRIBE&quot;,&quot;campaignCode&quot;:&quot;NGW_NEWHEADER_int_GU_SUBSCRIBE&quot;%7D" data-link-name="nav2 : subscribe">
subscribe
</a>
</li>
<li class="menu-item js-navigation-sign-in">
<a href="https://profile.theguardian.com/signin?INTCMP=DOTCOM_NEWHEADER_SIGNIN" data-link-name="nav2 : sign in" class="menu-item__title">
Sign in/up
</a>
</li>
<li class="menu-item menu-item--user-detail u-h hide-until-desktop js-navigation-account-details">
<div class="menu-user">
<span class="inline-profile inline-icon menu-user__avatar-fallback js-navigation-account-avatar-fallback">
<svg width="14" height="14" viewbox="0 0 14 14" class="menu-user__avatar-fallback__svg js-navigation-account-avatar-fallback__svg inline-profile__svg inline-icon__svg">
<path d="M2.1 12.3l.8-3.6.6-.6c1.2-.4 2.2-.6 3.5-.6 1.3 0 2.3.2 3.5.6l.6.6.8 3.6c1.3-1.3 2.1-3 2.1-5 0-3.9-3.1-7-7-7s-7 3.1-7 7c0 1.9.8 3.7 2.1 5zM7 1.4c1.5 0 2.3.8 2.3 2.3C9.3 5.2 8 6.4 7 6.4c-1-.1-2.3-1.3-2.3-2.7 0-1.5.8-2.3 2.3-2.3z"/>
</svg>
</span>
<img src="" class="menu-user__avatar u-h js-navigation-account-avatar" alt="user avatar"/>
<p class="menu-user__name js-navigation-account-username"></p>
</div>
</li>
<li class="menu-item menu-item--membership u-h js-navigation-account-actions">
<button class="menu-item__title hide-on-desktop js-navigation-toggle" data-link-name="nav2 : my account" aria-haspopup="true" aria-expanded="true">
<i class="menu-item__toggle"></i>
my account
</button>
<ul class="menu-group menu-group--membership-actions">
<li class="menu-item u-h js-show-comment-activity">
<a data-link-name="nav2 : comment activity" class="menu-item__title js-add-comment-activity-link">
Comment activity
</a>
</li>
<li class="menu-item">
<a href="https://profile.theguardian.com/public/edit" data-link-name="nav2 : edit profile" class="menu-item__title">
Edit profile
</a>
</li>
<li class="menu-item">
<a href="https://profile.theguardian.com/email-prefs" data-link-name="nav2 : email preferences" class="menu-item__title">
Email preferences
</a>
</li>
<li class="menu-item">
<a href="https://profile.theguardian.com/password/change" data-link-name="nav2 : change password" class="menu-item__title">
Change password
</a>
</li>
<li class="menu-item">
<a href="https://profile.theguardian.com/signout" data-link-name="nav2 : sign out" class="menu-item__title">
Sign out
</a>
</li>
</ul>
</li>
</ul>
<ul class="menu-group menu-group--editions">
<li class="menu-item js-navigation-item">
<button class="menu-item__title hide-on-desktop js-navigation-toggle" data-link-name="nav2 : edition picker" aria-haspopup="true" aria-expanded="true">
<i class="menu-item__toggle"></i>
<span class="hide-on-desktop">International edition</span>
<span class="hide-until-desktop">INT</span>
</button>
<span class="menu-item__editions-label hide-until-desktop">
edition:
</span>
<ul class="menu-group">
<li class="menu-item">
<a data-link-name="nav2 : edition-picker: UK" href="https://www.theguardian.com/preference/edition/uk" class="menu-item__title">
<span class="u-h">switch to the </span>
<span class="hide-on-desktop">UK edition</span>
<span class="hide-until-desktop">UK</span>
</a>
</li>
<li class="menu-item">
<a data-link-name="nav2 : edition-picker: US" href="https://www.theguardian.com/preference/edition/us" class="menu-item__title">
<span class="u-h">switch to the </span>
<span class="hide-on-desktop">US edition</span>
<span class="hide-until-desktop">US</span>
</a>
</li>
<li class="menu-item">
<a data-link-name="nav2 : edition-picker: AU" href="https://www.theguardian.com/preference/edition/au" class="menu-item__title">
<span class="u-h">switch to the </span>
<span class="hide-on-desktop">Australia edition</span>
<span class="hide-until-desktop">AU</span>
</a>
</li>
<li class="menu-item menu-item--edition-active hide-until-desktop">
<a data-link-name="nav2 : edition-picker: INT" href="https://www.theguardian.com/preference/edition/int" class="menu-item__title">
<span class="u-h">switch to the </span>
<span class="hide-until-desktop">INT</span>
</a>
</li>
</ul>
</li>
</ul>
<ul class="menu-group menu-group--footer" data-edition="int" role="menubar">
<li class="menu-item hide-on-desktop" role="menuitem">
<a class="menu-item__title" href="https://jobs.theguardian.com?INTCMP=jobs_int_web_newheader" data-link-name="nav2 : jobs">
jobs
</a>
</li>
<li class="menu-item hide-on-desktop" role="menuitem">
<a class="menu-item__title" href="https://soulmates.theguardian.com?INTCMP=soulmates_int_web_newheader" data-link-name="nav2 : dating">
dating
</a>
</li>
<li class="menu-item hide-on-desktop" role="menuitem">
<a class="menu-item__title" href="https://holidays.theguardian.com?INTCMP=holidays_int_web_newheader" data-link-name="nav2 : holidays">
holidays
</a>
</li>
<li class="hide-on-desktop menu-item" role="menuitem">
<a class="menu-item__title" href="https://app.adjust.com/f8qm1x_8q69t7?campaign=NewHeader&amp;amp;adgroup=Mobile&amp;amp;creative=generic?INTCMP=apps_int_web_newheader" data-link-name="nav2 : the guardian app">
the guardian app
</a>
</li>
<li class="menu-item menu-item--no-border" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/video" data-link-name="nav2 : video">
video
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/podcasts" data-link-name="nav2 : podcasts">
podcasts
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/inpictures" data-link-name="nav2 : pictures">
pictures
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/email-newsletters" data-link-name="nav2 : newsletters">
newsletters
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/theguardian" data-link-name="nav2 : today&#x27;s paper">
today&#x27;s paper
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/observer" data-link-name="nav2 : the observer">
the observer
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://theguardian.newspapers.com" data-link-name="nav2 : digital archive">
digital archive
</a>
</li>
<li class="menu-item" role="menuitem">
<a class="menu-item__title" href="https://www.theguardian.com/crosswords" data-link-name="nav2 : crosswords">
crosswords
</a>
</li>
<li class="menu-item hide-on-desktop" role="menuitem">
<a class="menu-item__title" href="https://www.facebook.com/theguardian" data-link-name="nav2 : facebook">
<span class="inline-share-facebook inline-icon menu-item__icon">
<svg width="32" height="32" viewbox="-2 -2 32 32" class="menu-item__icon__svg inline-share-facebook__svg inline-icon__svg">
<path d="M17.9 14h-3v8H12v-8h-2v-2.9h2V8.7C12 6.8 13.1 5 16 5c1.2 0 2 .1 2 .1v3h-1.8c-1 0-1.2.5-1.2 1.3v1.8h3l-.1 2.8z"/>
</svg>
</span>
Facebook
</a>
</li>
<li class="menu-item hide-on-desktop" role="menuitem">
<a class="menu-item__title" href="https://twitter.com/guardian" data-link-name="nav2 : twitter">
<span class="inline-share-twitter inline-icon menu-item__icon">
<svg width="32" height="32" viewbox="-2 -2 32 32" class="menu-item__icon__svg inline-share-twitter__svg inline-icon__svg">
<path d="M21.3 10.5v.5c0 4.7-3.5 10.1-9.9 10.1-2 0-3.8-.6-5.3-1.6.3 0 .6.1.8.1 1.6 0 3.1-.6 4.3-1.5-1.5 0-2.8-1-3.3-2.4.2 0 .4.1.7.1l.9-.1c-1.6-.3-2.8-1.8-2.8-3.5.5.3 1 .4 1.6.4-.9-.6-1.6-1.7-1.6-2.9 0-.6.2-1.3.5-1.8 1.7 2.1 4.3 3.6 7.2 3.7-.1-.3-.1-.5-.1-.8 0-2 1.6-3.5 3.5-3.5 1 0 1.9.4 2.5 1.1.8-.1 1.5-.4 2.2-.8-.3.8-.8 1.5-1.5 1.9.7-.1 1.4-.3 2-.5-.4.4-1 1-1.7 1.5z"/>
</svg>
</span>
Twitter
</a>
</li>
</ul>
</div>
<div class="menu-brand-extensions hide-until-desktop">
<div class="menu-brand-extensions__inner gs-container">
<span class="inline-guardian-logo-160 inline-logo menu-brand-extensions__logo">
<svg width="160" height="30" viewbox="0 0 320 60" class="menu-brand-extensions__logo__svg inline-guardian-logo-160__svg inline-logo__svg">
<path fill="#fff" d="M284 45h16v-3l-3-1.5v-20c1.2-.9 2.8-1.1 4.3-1.1 2.8 0 3.8.9 3.8 4.1v17l-3 1.5v3h16v-3l-3-1.5v-19c0-5.7-2.2-8.3-7.2-8.3-4.1 0-8.1 1.5-10.8 4V13h-1l-12.4 2.2v2.7l3.4 1.6v21l-3 1.5-.1 3zM245.3.4c-3 0-5.4 2.4-5.4 5.5 0 3 2.4 5.4 5.4 5.4 2.9 0 5.4-2.4 5.4-5.4-.1-3.1-2.5-5.5-5.4-5.5zM237 15.1v2.8l3 1.6v20.9l-3 1.5v3h16v-3l-3-1.5V13.1h-1l-12 2zM222.9 39c-.7.6-1.6 1.1-3.1 1.1-4 0-5.9-3.3-5.9-10.9 0-8.7 2.4-11.7 5.6-11.7 1.8 0 2.7.6 3.4 1.4V39zm0-24.5c-1.2-.9-3.2-1.4-4.9-1.4-7.4 0-14.5 4.3-14.5 16.8 0 11.9 7.1 15.7 11.8 15.7 3.8 0 6.4-1.7 7.6-3.4h.3v3.3h.9l11.9-1.4v-2.3l-3.2-1.8V.6h-.8l-12.6 2v2.8l3.4 1.6v7.5h.1zM181 18l3 1.5v20.9l-3 1.5v3h17v-3l-3.9-1.5V24.1c1.8-1.4 4-1.9 6.7-1.9.9 0 1.6.2 2.2.3v-9c-.3-.1-.7-.2-1.2-.2-3.3 0-5.9 2.1-7.7 6.2V13H193l-12 2v3zm-19.3-.8c3.9 0 5 2 5 5.9v3.5l-5.8 1.1c-5.9 1.1-10.4 3-10.4 9.3 0 5.1 3.5 8.7 8.3 8.7 3.8 0 7.4-1.7 8.7-4.4h.3c.5 3.3 3.3 4.4 6.4 4.4 2.4 0 4.8-.6 5.7-1.6v-2l-3-1.5v-18c0-6.9-5-9.4-13.1-9.4-5.3 0-8.8 1.4-11.6 2.7v7.8h4.7l2-6c.9-.5 2.4-.5 2.8-.5zm2.3 22.9c-1.9 0-4-1.1-4-4.6 0-2.4 2.4-4.6 4.8-5l2.2-.5v8.5s-1.9 1.6-3 1.6zm100.8-22.9c3.9 0 5 2 5 5.9v3.5l-5.8 1.1c-5.9 1.1-10.4 3-10.4 9.3 0 5.1 3.5 8.7 8.3 8.7 3.8 0 7.4-1.7 8.7-4.4h.3c.5 3.3 3.3 4.4 6.4 4.4 2.4 0 4.8-.6 5.7-1.6v-2l-3-1.5v-18c0-6.9-5-9.4-13.1-9.4-5.3 0-8.8 1.4-11.6 2.7v7.8h4.7l2-6c.8-.5 2.3-.5 2.8-.5zm2.2 22.9c-1.9 0-4-1.1-4-4.6 0-2.4 2.4-4.6 4.8-5l2.2-.5v8.5s-1.9 1.6-3 1.6zm-138.7 5.6c.4 0 .9 0 1.3-.1 3.5-.3 6.7-2 8.4-4.2v4.1l12-1.5v-2l-3-2V13h-1l-11.9 2.3v2.8l3.9 1.6V38c-1.1.8-2.4 1.3-4.2 1.3-2.5 0-4.8-.8-4.8-4.3V13h-1l-12 2.5v2.6l4 1.6V36c0 5.4 2.2 9.7 8.3 9.7zM96 38c-1.2 0-2.5-.8-2.5-1.9 0-.8.6-1.7 1.3-2.3 1.6.5 3 .6 5 .6 7.8 0 13.2-3.7 13.2-10.4 0-3-1.3-4.6-3.2-6.4L115 19v-6l-8.2 1.6c-1.9-.7-4.5-1.6-7-1.6-7.8 0-13.2 4.1-13.2 10.8 0 4.1 2 7.1 5 8.8l.3.2c-1.7 1.2-5.3 4-5.3 7.2 0 2.4 1.5 4.8 4.8 5.5C88 46.3 84 48 84 52c0 4.1 5.9 8 15.5 8 11.8 0 16.5-5.7 16.5-13 0-6.1-2.8-9-9.5-9H96zm7.5-14c0 5.7-1.3 6.5-3.5 6.5s-4-.8-4-6.5c0-5.8 1.8-7.5 4-7.5s3.5 2 3.5 7.5zM92 50.9c.1-1.5 1.1-3.4 3.7-3.6h8.6c2.5 0 3.7 2 3.7 3.6 0 3.2-2 4.4-8.3 4.4-5.5 0-7.8-2.2-7.7-4.4z"/>
<path fill="#AADCE6" d="M83 30c0-13-5.1-16.9-13-16.9-9 0-15 6.2-15 16.4 0 10.5 5.5 16.2 15.8 16.2 5.6 0 9.8-2.7 11.2-4.7v-3c-2.1.7-3.9 1.2-7.8 1.2-5.4 0-9.2-3.2-9.2-9.2h18zM69.9 16.6c2.5 0 3.8 1.9 3.8 9.6l-8.4.5c.2-7.9 1.8-10.1 4.6-10.1zM37 45v-3l-3-1.5V21c1.2-.9 3.3-1.7 4.8-1.7 2.8 0 4.3 1.5 4.2 4.2v17L40 42v3h16v-3l-3-1.5v-19c0-5.7-3.3-8.3-7.7-8.3-4.1 0-8.6 1.3-11.3 3.8V0h-1L21 2v3l4 1.5v34L22 42v3h15zM4 36.4c0 5.7 2.8 9.3 8.9 9.3 3.1 0 6.5-.8 8.4-2.3v-3.8c-.8.3-2.2.5-3.3.5-2.9 0-4-1.6-4-4.6V19h7v-5h-7V6.5L4 8v6l-4 1v4h4v17.4z"/>
</svg>
</span>
<ul class="menu-brand-extensions__list">
<li class="menu-brand-extensions__list-item">
<a href="https://jobs.theguardian.com?INTCMP=jobs_int_web_newheader" class="menu-brand-extensions-item" data-link-name="nav2 : brand extension : jobs">
jobs
</a>
</li>
<li class="menu-brand-extensions__list-item">
<a href="https://soulmates.theguardian.com?INTCMP=soulmates_int_web_newheader" class="menu-brand-extensions-item" data-link-name="nav2 : brand extension : dating">
dating
</a>
</li>
<li class="menu-brand-extensions__list-item">
<a href="https://holidays.theguardian.com?INTCMP=holidays_int_web_newheader" class="menu-brand-extensions-item" data-link-name="nav2 : brand extension : holidays">
holidays
</a>
</li>
</ul>
</div>
</div>
</div>
</nav>
<div class="subnav">
<div class="gs-container">
<ul class="subnav__list" data-pillar-title="news">
<li class="subnav__item">
<a class="subnav-link" href="https://www.theguardian.com/world" data-link-name="nav2 : subnav : world news">
world
</a>
</li>
<li class="subnav__item">
<a class="subnav-link" href="https://www.theguardian.com/uk-news" data-link-name="nav2 : subnav : UK news">
UK
</a>
</li>
<li class="subnav__item">
<a class="subnav-link" href="https://www.theguardian.com/uk/business" data-link-name="nav2 : subnav : business">
business
</a>
</li>
<li class="subnav__item">
<a class="subnav-link" href="https://www.theguardian.com/science" data-link-name="nav2 : subnav : science">
science
</a>
</li>
<li class="subnav__item">
<a class="subnav-link" href="https://www.theguardian.com/global-development" data-link-name="nav2 : subnav : global development">
global development
</a>
</li>
<li class="subnav__item">
<a class="subnav-link" href="https://www.theguardian.com/football" data-link-name="nav2 : subnav : football">
football
</a>
</li>
</ul>
</div>
</div>
</header>
<header id="header" class="l-header u-cf js-header" role="banner" data-link-name="global navigation: header">
<div class="js-navigation-header navigation-container navigation-container--collapsed">
<div class="gs-container l-header__inner">
<div class="l-header-pre u-cf">
<div class="brand-bar">
<div class="brand-bar__item brand-bar__item--profile popup-container
                                    has-popup js-profile-nav" data-component="identity-profile">
<a href="https://profile.theguardian.com/signin?INTCMP=DOTCOM_HEADER_SIGNIN" data-link-name="User profile" data-toggle="popup--profile" data-toggle-signed-in="true" class="brand-bar__item--action popup__toggle" data-test-id="sign-in-link" aria-haspopup="true">
<span class="inline-profile-36 inline-icon rounded-icon control__icon-wrapper">
<svg width="18" height="18" viewbox="0 0 18 18" class="rounded-icon__svg control__icon-wrapper__svg inline-profile-36__svg inline-icon__svg">
<path d="M9 7.3c1.6 0 3.4-1.8 3.4-3.9S11.1 0 9 0 5.6 1.3 5.6 3.4s2 3.9 3.4 3.9zm5.9 3.4l-.9-.8c-1.7-.6-3.1-.9-5-.9s-3.3.3-5 .9l-.9.9L1 17.2l.9.8h14.3l.9-.9-2.2-6.4z"/>
</svg>
</span>
<span class="js-profile-info control__info" data-test-id="sign-in-name">sign in</span>
</a>
<div class="js-profile-popup">
<ul class="popup popup--default popup__group popup--profile is-off" data-link-name="Sub Sections" data-test-id="popup-profile">
<li class="popup__item">
<a class="brand-bar__item--action js-comment-activity u-h" data-link-name="Comment activity">
Comment activity</a>
</li>
<li class="popup__item">
<a href="https://profile.theguardian.com/public/edit" class="brand-bar__item--action" data-link-name="Edit profile">
Edit profile</a>
</li>
<li class="popup__item">
<a href="https://profile.theguardian.com/email-prefs" class="brand-bar__item--action" data-link-name="Email preferences">
Email preferences</a>
</li>
<li class="popup__item">
<a href="https://profile.theguardian.com/password/change" class="brand-bar__item--action" data-link-name="Change password">
Change password</a></li>
<li class="popup__item">
<a href="https://profile.theguardian.com/signout" class="brand-bar__item--action" data-link-name="Sign out">
Sign out</a>
</li>
</ul>
</div>
</div>
<div class="brand-bar__item
                                    has-popup
                                    brand-bar__item--has-control
                                    popup-container
                                    brand-bar__item--subscribe
                                    hide-on-slim-header hide-on-tablet" data-component="subscribe">
<span class="inline-marque-36 inline-icon rounded-icon control__icon-wrapper">
<svg width="36" height="36" viewbox="0 0 36 36" class="rounded-icon__svg control__icon-wrapper__svg inline-marque-36__svg inline-icon__svg">
<path d="M21.3 8.8c0-4.9-1.5-5.7-3.3-5.7-1.8 0-3.2.7-3.2 5.7s1.5 5.5 3.2 5.5c1.8-.1 3.3-.6 3.3-5.5m-6.5 18.8c-2.3 0-2.9 1.7-2.9 2.9 0 1.8 1.6 3.4 6.3 3.4 5.3 0 6.8-1.5 6.8-3.4 0-1.7-1.3-2.9-3.4-2.9h-6.8zM10.5 2.4C4.3 5.2 0 11.4 0 18.7c0 4.9 2 9.4 5.2 12.6V31c0-3.2 3.1-4.4 5.9-5-2.6-.6-3.9-2.5-3.9-4.4 0-2.6 2.9-4.8 4.3-5.8l-.2-.1c-2.5-1.4-4.1-3.8-4.1-7 0-2.7 1.2-4.9 3.3-6.3M36 18.8C36 11.4 31.5 5 25.1 2.3c2.1 1.4 3.4 3.5 3.5 6.3l.1.6c0 5.4-4.4 8.2-10.7 8.2-1.6 0-2.7-.1-4.1-.5-.6.4-1.1 1.1-1.1 1.8 0 .9.8 1.6 1.8 1.6h8.8c5.5 0 8.2 2.2 8.2 7.1 0 1.6-.3 3.1-1 4.3 3.3-3.4 5.4-7.9 5.4-12.9"/>
</svg>
</span>
<a href="https://membership.theguardian.com/supporter?INTCMP=DOTCOM_HEADER_BECOMEMEMBER_INT&amp;acquisitionData=%7B&quot;source&quot;:&quot;GUARDIAN_WEB&quot;,&quot;componentType&quot;:&quot;ACQUISITIONS_HEADER&quot;,&quot;componentId&quot;:&quot;DOTCOM_HEADER_BECOMEMEMBER_INT&quot;,&quot;campaignCode&quot;:&quot;DOTCOM_HEADER_BECOMEMEMBER_INT&quot;%7D" data-link-name="Register link" class="brand-bar__item--action brand-bar__item--split--first js-become-member">
<span class="control__info js-control-info control__info--supporting">
become a supporter
</span>
</a>
<a href="https://subscribe.theguardian.com?INTCMP=NGW_HEADER_INT_GU_SUBSCRIBE&amp;acquisitionData=%7B&quot;source&quot;:&quot;GUARDIAN_WEB&quot;,&quot;componentType&quot;:&quot;ACQUISITIONS_HEADER&quot;,&quot;componentId&quot;:&quot;NGW_HEADER_INT_GU_SUBSCRIBE&quot;,&quot;campaignCode&quot;:&quot;NGW_HEADER_INT_GU_SUBSCRIBE&quot;%7D" class="brand-bar__item--action brand-bar__item--split--last js-subscribe js-change-subscribe-link" data-link-name="int : topNav : subscribe">
<span class="control__info js-control-info">subscribe</span>
</a>
</div>
<div class="brand-bar__item has-popup popup-container brand-bar__item--search" data-component="search">
<a href="https://www.google.co.uk/advanced_search?q=site:www.theguardian.com" data-is-ajax data-link-name="Search icon" class="brand-bar__item--action popup__toggle js-search-toggle" data-toggle="popup--search" aria-haspopup="true">
<span class="inline-search-36 inline-icon rounded-icon control__icon-wrapper">
<svg width="18" height="18" viewbox="0 0 18 18" class="rounded-icon__svg control__icon-wrapper__svg inline-search-36__svg inline-icon__svg">
<path d="M6.5 1.6c2.7 0 4.9 2.2 4.9 4.9s-2.2 4.9-4.9 4.9-4.9-2.2-4.9-4.9 2.2-4.9 4.9-4.9m0-1.6C2.9 0 0 2.9 0 6.5S2.9 13 6.5 13 13 10.1 13 6.5 10.1 0 6.5 0zm6.6 11.5l4.9 4.9-1.6 1.6-4.9-4.9v-.8l.8-.8h.8z"/>
</svg>
</span>
<span class="control__info">search</span>
</a>
</div>
<div class="brand-bar__item--right" data-component="guardian-services">
<div class="brand-bar__item brand-bar__item--jobs hide-until-tablet hide-on-slim-header">
<a class="brand-bar__item--action" data-link-name="uk : topNav : jobs" href="https://jobs.theguardian.com/?INTCMP=NGW_TOPNAV_INT_GU_JOBS">jobs</a>
</div>
<div class="brand-bar__item brand-bar__item--soulmates hide-until-desktop hide-on-slim-header">
<a class="brand-bar__item--action" data-link-name="int : topNav : soulmates" href="https://soulmates.theguardian.com/?INTCMP=NGW_TOPNAV_INT_GU_SOULMATES">dating</a>
</div>
<div class="brand-bar__item has-popup brand-bar__item--has-control brand-bar__item--more">
<a class="brand-bar__item--action popup__toggle" data-toggle="top-bar__popup--more" data-link-name="topNav : more" aria-haspopup="true" aria-controls="guardian-services-top-menu">
<span class="rounded-icon control__icon-wrapper">
<!--[if (gt IE 8)&(IEMobile)]><!-->
<span class="inline-ellipsis-36 inline-icon ">
<svg viewbox="0 0 24 18" width="24" height="18" fill="#fff" class="inline-ellipsis-36__svg inline-icon__svg">
<circle cx="3" cy="10" r="3"/>
<circle cx="12" cy="10" r="3"/>
<circle cx="21" cy="10" r="3"/>
</svg>
</span>
<!--<![endif]-->
</span>
<span class="control__info" data-test-id="sign-in-name">more</span>
</a>
<div class="popup popup--default is-off top-bar__popup--more" id="guardian-services-top-menu">
<h3 class="popup__group-header">from the guardian:</h3>
<ul class="popup__group">
<li class="popup__item brand-bar__popup--soulmates hide-on-desktop show-on-slim-header">
<a class="brand-bar__item--action" data-link-name="int : topNav : soulmates" href="https://soulmates.theguardian.com/?INTCMP=NGW_TOPNAV_INT_GU_SOULMATES">dating</a>
</li>
<li class="popup__item brand-bar__popup--jobs">
<a class="brand-bar__item--action" data-link-name="int: topNav : jobs" href="https://jobs.theguardian.com/?INTCMP=NGW_TOPNAV_INT_GU_JOBS">jobs</a>
</li>
</ul>
<div class="brand-bar__popup--edition mobile-only show-on-slim-header">
<h3 class="popup__group-header">change edition:</h3>
<ul class="popup__group">
<li class="popup__item">
<a class="brand-bar__item--action brand-bar__item--inline-action" data-edition="UK" data-link-name="switch to UK edition" href="https://www.theguardian.com/preference/edition/uk" title="Switch to the UK edition">
<span class="u-h">switch to the </span> UK <span class="u-h"> edition</span>
</a>
<a class="brand-bar__item--action brand-bar__item--inline-action" data-edition="US" data-link-name="switch to US edition" href="https://www.theguardian.com/preference/edition/us" title="Switch to the US edition">
<span class="u-h">switch to the </span> US <span class="u-h"> edition</span>
</a>
<a class="brand-bar__item--action brand-bar__item--inline-action" data-edition="AU" data-link-name="switch to AU edition" href="https://www.theguardian.com/preference/edition/au" title="Switch to the AU edition">
<span class="u-h">switch to the </span> AU <span class="u-h"> edition</span>
</a>
</li>
</ul>
</div>
</div>
</div>
<div class="brand-bar__item has-popup brand-bar__item--has-control brand-bar__item--edition hide-until-tablet hide-on-slim-header" data-component="edition">
<a class="brand-bar__item--action popup__toggle" data-link-name="topNav : edition" data-toggle="top-bar__popup--edition" aria-haspopup="true" aria-controls="guardian-edition-menu">
International edition
</a>
<ul class="popup popup--default popup__group is-off top-bar__popup--edition" id="guardian-edition-menu">
<li class="popup__item">
<a class="brand-bar__item--action" data-edition="UK" data-link-name="switch to UK edition" href="https://www.theguardian.com/preference/edition/uk" title="Switch to the UK edition">
<span class="u-h">switch to the </span>
<span class="brand-bar__edition-name">UK edition</span>
</a>
</li>
<li class="popup__item">
<a class="brand-bar__item--action" data-edition="US" data-link-name="switch to US edition" href="https://www.theguardian.com/preference/edition/us" title="Switch to the US edition">
<span class="u-h">switch to the </span>
<span class="brand-bar__edition-name">US edition</span>
</a>
</li>
<li class="popup__item">
<a class="brand-bar__item--action" data-edition="AU" data-link-name="switch to AU edition" href="https://www.theguardian.com/preference/edition/au" title="Switch to the AU edition">
<span class="u-h">switch to the </span>
<span class="brand-bar__edition-name">Australia edition</span>
</a>
</li>
</ul>
</div>
</div>
</div>
</div>
<div class="popup popup--default popup--search js-search-popup is-off"><div class="js-search-placeholder"></div></div>
<div class="l-header-main">
<a href="https://www.theguardian.com/international" data-link-name="site logo" id="logo" class="logo-wrapper" data-component="logo">
<span class="u-h">The Guardian - Back to home</span>
<!--[if (gt IE 8)|(IEMobile)]><!-->
<span class="inline-guardian-logo-320 inline-logo ">
<svg width="320" height="60" viewbox="0 0 320 60" class="inline-guardian-logo-320__svg inline-logo__svg">
<path fill="#fff" d="M284 45h16v-3l-3-1.5v-20c1.2-.9 2.8-1.1 4.3-1.1 2.8 0 3.7.9 3.7 4.1v17l-3 1.5v3h16v-3l-3-1.5v-19c0-5.7-2.1-8.3-7.1-8.3-4.1 0-8.1 1.5-10.8 4V13h-1l-12.4 2.2v2.7l3.3 1.6v21l-3 1.5v3zM245.3.4c-3 0-5.4 2.4-5.4 5.5 0 3 2.4 5.4 5.4 5.4 2.9 0 5.4-2.4 5.4-5.4-.1-3.1-2.5-5.5-5.4-5.5zM237 15.1v2.8l3 1.6v20.9l-3 1.5V45h16v-3.1l-3-1.5V13.1h-1l-12 2zM223 39c-.7.6-1.7 1.1-3.2 1.1-4 0-5.9-3.3-5.9-10.9 0-8.7 2.4-11.6 5.6-11.6 1.8 0 2.8.6 3.5 1.4v20zm0-24.4c-1.2-.9-3.3-1.4-5-1.4-7.4 0-14.5 4.4-14.5 16.8 0 11.9 7.1 15.7 11.8 15.7 3.8 0 6.4-1.7 7.6-3.4h.3v3.3h.9l11.9-1.4v-2.3l-3-1.8V.6h-1l-12.6 2v2.8l3.6 1.5v7.7zM181 18l3 1.5v20.9l-3 1.5V45h17v-3.1l-4-1.5V24.1c1.8-1.4 4.1-1.9 6.8-1.9.9 0 1.6.2 2.2.3v-9c-.3-.1-.7-.2-1.2-.2-3.3 0-6 2.2-7.8 6.2V13h-1l-12 2v3zm-19.3-.8c3.9 0 5.3 2 5.3 5.9v3.5l-6.1 1.1c-5.9 1.1-10.4 2.9-10.4 9.3 0 5.1 3.5 8.7 8.3 8.7 3.8 0 7.4-1.7 8.7-4.4h.3c.5 3.3 3.3 4.4 6.4 4.4 2.4 0 4.8-.6 5.7-1.6v-2l-2.9-1.5v-18c0-7-5.2-9.4-13.3-9.4-5.3 0-8.6 1.3-11.4 2.6v7.8h4.7l2-6c1.1-.4 2.3-.4 2.7-.4zm2.3 22.9c-1.9 0-4-1.1-4-4.6 0-2.4 2.4-4.7 4.8-5l2.2-.5v8.5s-1.9 1.6-3 1.6zm100.7-22.9c3.9 0 5.3 2 5.3 5.9v3.5l-6.1 1.1c-5.9 1.1-10.4 2.9-10.4 9.3 0 5.1 3.5 8.7 8.3 8.7 3.8 0 7.4-1.7 8.7-4.4h.3c.5 3.3 3.3 4.4 6.4 4.4 2.4 0 4.8-.6 5.7-1.6v-2l-2.9-1.5v-18c0-7-5.2-9.4-13.3-9.4-5.3 0-8.6 1.3-11.4 2.6v7.8h4.7l2-6c1.1-.4 2.3-.4 2.7-.4zm2.3 22.9c-1.9 0-4-1.1-4-4.6 0-2.4 2.4-4.7 4.8-5l2.2-.5v8.5s-1.9 1.6-3 1.6zm-138.7 5.6c.4 0 .9 0 1.3-.1 3.5-.3 6.7-2 8.4-4.2v4.1l12-1.5v-2l-3-2V13h-1l-12 2.3V18l4 1.7V38c-1.1.8-2.4 1.3-4.2 1.3-2.5 0-4.8-.8-4.8-4.3V13h-1l-12 2.5v2.6l4 1.6V36c0 5.4 2.2 9.7 8.3 9.7zM96 38c-1.2 0-2.5-.8-2.5-1.9 0-.8.6-1.7 1.4-2.3 1.6.5 3 .6 5 .6 7.8 0 13.2-3.7 13.2-10.4 0-3-1.3-4.6-3.2-6.4L115 19v-6l-8.2 1.6c-1.9-.7-4.5-1.6-7-1.6-7.8 0-13.2 4.1-13.2 10.8 0 4.1 2 7.1 5 8.8l.2.2c-1.7 1.2-5.3 4-5.3 7.2 0 2.4 1.5 4.8 4.8 5.5-3.4.8-7.3 2.5-7.3 6.5 0 4.1 5.9 8 15.5 8 11.8 0 16.5-5.7 16.5-13 0-6.1-2.8-9-9.5-9H96zm7.5-14c0 5.7-1.3 6.5-3.5 6.5s-4-.8-4-6.5c0-5.8 1.8-7.5 4-7.5s3.5 2 3.5 7.5zM92 50.9c.1-1.5 1.1-3.4 3.7-3.6h8.6c2.5 0 3.7 2 3.7 3.6 0 3.2-2 4.4-8.3 4.4-5.5 0-7.8-2.2-7.7-4.4z"/>
<path fill="#AADCE6" d="M83 30c0-13-5.1-16.9-13-16.9-9 0-15 6.2-15 16.4 0 10.5 5.5 16.2 15.8 16.2 5.6 0 9.7-2.7 11.2-4.7v-3c-2.1.7-3.9 1.2-7.7 1.2-5.6 0-9.3-3.2-9.3-9.2h18zM69.9 16.6c2.5 0 3.8 1.8 3.8 9.6l-8.4.7c.1-7.9 1.8-10.3 4.6-10.3zM37 45v-3l-3-1.5V21c1.2-.9 3.2-1.7 4.8-1.7 2.8 0 4.3 1.6 4.2 4.2v17L40 42v3h16v-3l-3-1.5v-19c0-5.7-3.3-8.3-7.7-8.3-4.1 0-8.6 1.3-11.3 3.8V0h-1L21 2v3l4 1.5v34L22 42v3h15zM4 36.4c0 5.7 2.8 9.3 8.9 9.3 3.1 0 6.2-.8 8.1-2.3v-3.8c-.8.3-1.9.5-2.9.5-2.9 0-4.1-1.6-4.1-4.6V19h7v-5h-7V6.5L4 8v6l-4 1v4h4v17.4z"/>
</svg>
</span>
<!--<![endif]-->
<!--[if (lt IE 9)&(!IEMobile)]>
                                <span class="inline-logo inline-guardian-logo-320"></span>
                            <![endif]-->
</a>
</div>
</div>
<div class="js-navigation navigation navigation--has-signposting">
<div class="gs-container">
<div class="navigation__inner">
<div class="navigation__scroll">
<nav class="navigation__container navigation__container--first" data-component="nav" role="navigation" aria-label="Current section">
<ul class="signposting">
<li class="signposting__item signposting__item--home">
<a class="signposting__action" href="https://www.theguardian.com/international" data-link-name="nav : signposting : home">home</a>
</li>
</ul>
</nav>
<nav class="navigation__container navigation__container--second" data-component="nav" role="navigation" aria-label="Guardian sections">
<ul class="top-navigation js-top-navigation">
<li class="top-navigation__item top-navigation__item--home">
<a href="https://www.theguardian.com/international" class="top-navigation__action top-navigation__action--has-icon" data-link-name="nav : primary : home" title="Back to homepage">
<span class="top-navigation__icon top-navigation__icon--home"></span>
<span class="u-h">home</span>
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk-news" data-link-name="nav : primary : UK">
UK
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/world" data-link-name="nav : primary : world">
world
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/sport" data-link-name="nav : primary : sport">
sport
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/football" data-link-name="nav : primary : football">
football
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/commentisfree" data-link-name="nav : primary : opinion">
opinion
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/culture" data-link-name="nav : primary : culture">
culture
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/business" data-link-name="nav : primary : business">
business
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/lifeandstyle" data-link-name="nav : primary : lifestyle">
lifestyle
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/fashion" data-link-name="nav : primary : fashion">
fashion
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/environment" data-link-name="nav : primary : environment">
environment
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/technology" data-link-name="nav : primary : tech">
tech
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/travel" data-link-name="nav : primary : travel">
travel
</a>
</li>
</ul>
</nav>
</div>
<a class="navigation-toggle js-navigation-toggle" href="#footer-nav" data-link-name="nav : allSections" data-target-nav="js-navigation-header">
<i class="burger-icon"></i><span class="navigation-toggle-label navigation-toggle-label--open" aria-haspopup="true" aria-controls="all-sections-popup" aria-label="browse all sections"><span class="navigation-toggle-label__extra navigation-toggle-label__extra--browse">browse </span>all<span class="navigation-toggle-label__extra"> sections</span></span>
<span class="navigation-toggle-label navigation-toggle-label--close" aria-label="close all sections">close</span>
</a>
</div>
<div id="all-sections-popup" class="navigation__expandable js-mega-nav-placeholder" data-component="all-nav"></div>
</div>
</div>
</div>
</header>
</div>
<div class="js-breaking-news-placeholder breaking-news breaking-news--hidden breaking-news--fade-in" data-link-name="breaking news" data-component="breaking-news">
</div>
<div class="l-side-margins">
<div class="facia-page" data-link-name="Front | /international" role="main">
<section id="headlines" class="fc-container fc-container--first js-container--first " data-link-name="container-1 | headlines" data-id="10f21d96-18f6-426f-821b-19df55dfb831" data-component="headlines" aria-expanded="true">
<div class="fc-container__inner">
<div class="fc-container__header
                js-container__header
                ">
<div class="fc-container__header__title">
<span tabindex="0">headlines</span>
</div>
</div>
<div class="fc-container--rolled-up-hide fc-container__body" data-title="headlines" data-id="10f21d96-18f6-426f-821b-19df55dfb831">
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-4 fc-slice fc-slice--qqq-q">
<li class="fc-slice__item l-row__item l-row__item--span-3 u-faux-block-link">
<div class="fc-item fc-item--force-image-upgrade fc-item--has-image fc-item--has-sublinks-3 js-fc-item tone-news--item fc-item--standard-mobile fc-item--three-quarters-tablet js-snappable" data-link-name="news | group-2+ | card-1" data-item-visibility="all" data-test-id="facia-card" data-id="film/2017/oct/12/harvey-weinstein-nypd-and-london-police-investigating-allegations" data-loyalty-short-url="/p/7cfab">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio inlined-image">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="460px" srcset="https://i.guim.co.uk/img/media/e69cff43cbdc2b2c90dd52d4c5a812b8385371ab/0_65_4234_2541/master/4234.jpg?w=460&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=6806b10fc15beeb782b903050ccdd1cd 920w">
<source media="(min-width: 980px)" sizes="460px" srcset="https://i.guim.co.uk/img/media/e69cff43cbdc2b2c90dd52d4c5a812b8385371ab/0_65_4234_2541/master/4234.jpg?w=460&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=71b355b8ca790d50ba248dfc5c9ca108 460w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="340px" srcset="https://i.guim.co.uk/img/media/e69cff43cbdc2b2c90dd52d4c5a812b8385371ab/0_65_4234_2541/master/4234.jpg?w=340&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=a93d34bd9a899d6677ec1daea40c00f4 680w">
<source media="(min-width: 740px)" sizes="340px" srcset="https://i.guim.co.uk/img/media/e69cff43cbdc2b2c90dd52d4c5a812b8385371ab/0_65_4234_2541/master/4234.jpg?w=340&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=30a763e0bead5fcc3fba13a4867c0d6f 340w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="95vw" srcset="https://i.guim.co.uk/img/media/e69cff43cbdc2b2c90dd52d4c5a812b8385371ab/0_65_4234_2541/master/4234.jpg?w=460&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=6806b10fc15beeb782b903050ccdd1cd 920w, https://i.guim.co.uk/img/media/e69cff43cbdc2b2c90dd52d4c5a812b8385371ab/0_65_4234_2541/master/4234.jpg?w=340&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=a93d34bd9a899d6677ec1daea40c00f4 680w, https://i.guim.co.uk/img/media/e69cff43cbdc2b2c90dd52d4c5a812b8385371ab/0_65_4234_2541/master/4234.jpg?w=445&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=c29ed5455c13153d1352f6232067c9a0 890w, https://i.guim.co.uk/img/media/e69cff43cbdc2b2c90dd52d4c5a812b8385371ab/0_65_4234_2541/master/4234.jpg?w=605&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=b48839a2948d3701cd9f0242fce2e955 1210w">
<source media="(min-width: 0px)" sizes="95vw" srcset="https://i.guim.co.uk/img/media/e69cff43cbdc2b2c90dd52d4c5a812b8385371ab/0_65_4234_2541/master/4234.jpg?w=460&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=71b355b8ca790d50ba248dfc5c9ca108 460w, https://i.guim.co.uk/img/media/e69cff43cbdc2b2c90dd52d4c5a812b8385371ab/0_65_4234_2541/master/4234.jpg?w=340&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=30a763e0bead5fcc3fba13a4867c0d6f 340w, https://i.guim.co.uk/img/media/e69cff43cbdc2b2c90dd52d4c5a812b8385371ab/0_65_4234_2541/master/4234.jpg?w=445&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=255cb8105eab5446777a066a06e0b2e7 445w, https://i.guim.co.uk/img/media/e69cff43cbdc2b2c90dd52d4c5a812b8385371ab/0_65_4234_2541/master/4234.jpg?w=605&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=7afd96385bb9a95ac2db7411d70f8519 605w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="" src="https://i.guim.co.uk/img/media/e69cff43cbdc2b2c90dd52d4c5a812b8385371ab/0_65_4234_2541/master/4234.jpg?w=300&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=2a956727428773b7cd6a04cc5643bbc3">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h1 class="fc-item__title"><a href="https://www.theguardian.com/film/2017/oct/12/harvey-weinstein-nypd-and-london-police-investigating-allegations" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Harvey Weinstein</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">NYPD and London police investigating allegations</span></span> </a></h1>
</div>
<div class="fc-item__standfirst">
London’s Metropolitan police have opened an inquiry into the Hollywood producer’s alleged actions and the NYPD is reviewing for ‘additional complaints’
</div>
<div class="fc-item__footer--vertical" aria-hidden="true">
<ul class="fc-sublinks u-unstyled u-faux-block-link__promote">
<li class="fc-sublink tone-news--sublink" data-link-name="sublinks | 1"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/film/2017/oct/12/oscars-discuss-response-harvey-weinstein-allegations" class="fc-sublink__link" data-link-name="article"><span class="fc-sublink__kicker">Oscars</span> Academy body to discuss response to allegations</a> </h3> </li>
<li class="fc-sublink tone-news--sublink" data-link-name="sublinks | 2"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/film/2017/oct/12/james-van-der-beek-says-that-he-was-sexually-harassed-by-older-powerful-men" class="fc-sublink__link" data-link-name="article"><span class="fc-sublink__kicker">James Van Der Beek</span> Actor harassed by 'older, powerful men'</a> </h3> </li>
<li class="fc-sublink tone-news--sublink" data-link-name="sublinks | 3"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/technology/2017/oct/12/rose-mcgowan-twitter-suspended-ben-affleck-harvey-weinstein" class="fc-sublink__link" data-link-name="article"><span class="fc-sublink__kicker">Rose McGowan</span> Twitter account suspended after Ben Affleck tweets</a> </h3> </li>
</ul>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<footer class="fc-item__footer--horizontal">
<ul class="fc-sublinks u-unstyled u-faux-block-link__promote">
<li class="fc-sublink tone-news--sublink" data-link-name="sublinks | 1"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/film/2017/oct/12/oscars-discuss-response-harvey-weinstein-allegations" class="fc-sublink__link" data-link-name="article"><span class="fc-sublink__kicker">Oscars</span> Academy body to discuss response to allegations</a> </h3> </li>
<li class="fc-sublink tone-news--sublink" data-link-name="sublinks | 2"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/film/2017/oct/12/james-van-der-beek-says-that-he-was-sexually-harassed-by-older-powerful-men" class="fc-sublink__link" data-link-name="article"><span class="fc-sublink__kicker">James Van Der Beek</span> Actor harassed by 'older, powerful men'</a> </h3> </li>
<li class="fc-sublink tone-news--sublink" data-link-name="sublinks | 3"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/technology/2017/oct/12/rose-mcgowan-twitter-suspended-ben-affleck-harvey-weinstein" class="fc-sublink__link" data-link-name="article"><span class="fc-sublink__kicker">Rose McGowan</span> Twitter account suspended after Ben Affleck tweets</a> </h3> </li>
</ul>
</footer>
<a href="https://www.theguardian.com/film/2017/oct/12/harvey-weinstein-nypd-and-london-police-investigating-allegations" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">NYPD and London police investigating allegations</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--force-image-upgrade fc-item--has-image js-fc-item tone-news--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="news | group-2 | card-2" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/us-withdraw-unesco-december-united-nations" data-loyalty-short-url="/p/7cf38">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio inlined-image">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/68735d01c046e4e0304ccead2ea7a660734b1e14/0_322_4662_2797/master/4662.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=25443aaa09ba305da854fc4480c80753 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/68735d01c046e4e0304ccead2ea7a660734b1e14/0_322_4662_2797/master/4662.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=8d944dd7d33a7c0bf731429473c503c6 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/68735d01c046e4e0304ccead2ea7a660734b1e14/0_322_4662_2797/master/4662.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=8e685a6bfb95caf6547f5f9deab1f936 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/68735d01c046e4e0304ccead2ea7a660734b1e14/0_322_4662_2797/master/4662.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=08f74890b74e0d6e069ef98791593d6d 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/68735d01c046e4e0304ccead2ea7a660734b1e14/0_322_4662_2797/master/4662.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=2d9979f01b42c9df1d6b446ddec6fc3b 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/68735d01c046e4e0304ccead2ea7a660734b1e14/0_322_4662_2797/master/4662.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=89af9265359a13006592a3f299f60c06 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="" src="https://i.guim.co.uk/img/media/68735d01c046e4e0304ccead2ea7a660734b1e14/0_322_4662_2797/master/4662.jpg?w=300&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=f59e1dd053f17c376e82889a9385caa4">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/us-withdraw-unesco-december-united-nations" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Unesco</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">US quits UN heritage agency over 'anti-Israel bias'</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
Trump administration has been preparing for a withdrawal from world heritage body for months, which Israeli PM praises as ‘brave and moral decision’
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/us-withdraw-unesco-december-united-nations" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">US quits UN heritage agency over 'anti-Israel bias'</a>
</div>
</div> </li>
</ul>
</div>
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-4 fc-slice fc-slice--h-q_ql2-ql4">
<li class="fc-slice__item l-row__item l-row__item--span-2 u-faux-block-link">
<div class="fc-item fc-item--force-image-upgrade fc-item--has-image fc-item--has-sublinks-2 js-fc-item tone-news--item fc-item--list-media-mobile fc-item--half-tablet js-snappable" data-link-name="news | group-1+ | card-3" data-item-visibility="all" data-test-id="facia-card" data-id="politics/2017/oct/12/brexit-talks-at-disturbing-deadlock-over-divorce-bill-says-eu-negotiator" data-loyalty-short-url="/p/7cecj">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio inlined-image">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="460px" srcset="https://i.guim.co.uk/img/media/7c8310cf85978de1e3009cde029ecce231eb281e/204_368_4161_2497/master/4161.jpg?w=460&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=751d8d6a80fbb252be9c3a8edd365e8a 920w">
<source media="(min-width: 980px)" sizes="460px" srcset="https://i.guim.co.uk/img/media/7c8310cf85978de1e3009cde029ecce231eb281e/204_368_4161_2497/master/4161.jpg?w=460&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=b458a15976be9dfaefd3c84ace16a1ae 460w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="340px" srcset="https://i.guim.co.uk/img/media/7c8310cf85978de1e3009cde029ecce231eb281e/204_368_4161_2497/master/4161.jpg?w=340&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=6140fab2199bb85119fab1714ba6ce35 680w">
<source media="(min-width: 740px)" sizes="340px" srcset="https://i.guim.co.uk/img/media/7c8310cf85978de1e3009cde029ecce231eb281e/204_368_4161_2497/master/4161.jpg?w=340&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=a1398b9895f99624fe23492e7b718d9f 340w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/7c8310cf85978de1e3009cde029ecce231eb281e/204_368_4161_2497/master/4161.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=14eb6fcfe3dc79e83221112e6c118177 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/7c8310cf85978de1e3009cde029ecce231eb281e/204_368_4161_2497/master/4161.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=ad83cef6cc9a16aeeebbf19ad9f42637 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="" src="https://i.guim.co.uk/img/media/7c8310cf85978de1e3009cde029ecce231eb281e/204_368_4161_2497/master/4161.jpg?w=300&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=cae4b2ab9400dda3d7e92415334708bb">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/politics/2017/oct/12/brexit-talks-at-disturbing-deadlock-over-divorce-bill-says-eu-negotiator" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Brexit</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Talks at 'disturbing deadlock' over divorce bill, says EU negotiator</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
Michel Barnier tells joint press conference with Brexit secretary David Davis that he cannot recommend moving on to trade talks
</div>
<div class="fc-item__footer--vertical" aria-hidden="true">
<ul class="fc-sublinks u-unstyled u-faux-block-link__promote">
<li class="fc-sublink tone-news--sublink" data-link-name="sublinks | 1"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/politics/2017/oct/12/eu-refuses-to-engage-on-rights-of-britons-living-in-europe-after-brexit" class="fc-sublink__link" data-link-name="article"><span class="fc-sublink__kicker">Britons in Europe</span> EU 'refusing to engage on rights'</a> </h3> </li>
<li class="fc-sublink tone-news--sublink" data-link-name="sublinks | 2"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/world/2017/oct/12/christine-lagarde-imf-britain-eu-no-deal-brexit-talks" class="fc-sublink__link" data-link-name="article"><span class="fc-sublink__kicker">IMF chief</span> Unimaginable for UK to leave EU without a deal</a> </h3> </li>
</ul>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<footer class="fc-item__footer--horizontal">
<ul class="fc-sublinks u-unstyled u-faux-block-link__promote">
<li class="fc-sublink tone-news--sublink" data-link-name="sublinks | 1"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/politics/2017/oct/12/eu-refuses-to-engage-on-rights-of-britons-living-in-europe-after-brexit" class="fc-sublink__link" data-link-name="article"><span class="fc-sublink__kicker">Britons in Europe</span> EU 'refusing to engage on rights'</a> </h3> </li>
<li class="fc-sublink tone-news--sublink" data-link-name="sublinks | 2"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/world/2017/oct/12/christine-lagarde-imf-britain-eu-no-deal-brexit-talks" class="fc-sublink__link" data-link-name="article"><span class="fc-sublink__kicker">IMF chief</span> Unimaginable for UK to leave EU without a deal</a> </h3> </li>
</ul>
</footer>
<a href="https://www.theguardian.com/politics/2017/oct/12/brexit-talks-at-disturbing-deadlock-over-divorce-bill-says-eu-negotiator" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Talks at 'disturbing deadlock' over divorce bill, says EU negotiator</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1">
<ul class="u-unstyled l-list l-list--columns-1 l-list--rows-3">
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--force-image-upgrade fc-item--has-image js-fc-item tone-news--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="news | group-1 | card-4" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/cuba-mass-hysteria-sonic-attacks-neurologists" data-loyalty-short-url="/p/7cfkv">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio inlined-image">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/ec9e541074430d656d83a5d6de0f6991fa2b887d/0_0_3500_2101/master/3500.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=c29b867e9b0780405e53971c7bb666bc 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/ec9e541074430d656d83a5d6de0f6991fa2b887d/0_0_3500_2101/master/3500.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=6802d3a74eefd5a36272f749f15e1fe8 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/ec9e541074430d656d83a5d6de0f6991fa2b887d/0_0_3500_2101/master/3500.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=596b930278d1503d5d57e4222a2bd267 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/ec9e541074430d656d83a5d6de0f6991fa2b887d/0_0_3500_2101/master/3500.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=5627d6bd21e065167c26f241248057c3 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/ec9e541074430d656d83a5d6de0f6991fa2b887d/0_0_3500_2101/master/3500.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=bf7701786f6d075efa2cb3b41edd5612 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/ec9e541074430d656d83a5d6de0f6991fa2b887d/0_0_3500_2101/master/3500.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e64b36ded8cd79604add4eeeb4f3318e 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="" src="https://i.guim.co.uk/img/media/ec9e541074430d656d83a5d6de0f6991fa2b887d/0_0_3500_2101/master/3500.jpg?w=300&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e47db10b97e9ba357d4b55174ca1ab3a">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/cuba-mass-hysteria-sonic-attacks-neurologists" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Cuba</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Mass hysteria may explain 'sonic attacks', say top neurologists</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
Despite 22 Americans reporting symptoms, no evidence of a weapon has been found and experts suspect psychosomatic disorder linked to high stress
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/cuba-mass-hysteria-sonic-attacks-neurologists" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Mass hysteria may explain 'sonic attacks', say top neurologists</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--force-image-upgrade fc-item--has-image js-fc-item tone-news--item fc-item--list-mobile fc-item--list-tablet js-snappable" data-link-name="news | group-0 | card-5" data-item-visibility="all" data-test-id="facia-card" data-id="us-news/2017/oct/12/trump-sabotage-obamacare-executive-order" data-loyalty-short-url="/p/7cft2">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/us-news/2017/oct/12/trump-sabotage-obamacare-executive-order" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">US healthcare</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Trump accused of sabotage after signing executive order to weaken Obamacare</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/us-news/2017/oct/12/trump-sabotage-obamacare-executive-order" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Trump accused of sabotage after signing executive order to weaken Obamacare</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--force-image-upgrade fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-news--item fc-item--list-mobile fc-item--list-tablet js-snappable" data-discussion-id="/p/7ce87" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/science/2017/oct/12/astronomers-find-half-of-the-missing-matter-in-the-universe#comments" data-link-name="news | group-0 | card-6" data-item-visibility="all" data-test-id="facia-card" data-id="science/2017/oct/12/astronomers-find-half-of-the-missing-matter-in-the-universe" data-loyalty-short-url="/p/7ce87">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/science/2017/oct/12/astronomers-find-half-of-the-missing-matter-in-the-universe" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Astronomy</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Scientists find half of the missing matter in the universe</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/science/2017/oct/12/astronomers-find-half-of-the-missing-matter-in-the-universe" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Scientists find half of the missing matter in the universe</a>
</div>
</div> </li>
</ul> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1">
<ul class="u-unstyled l-list l-list--columns-1 l-list--rows-5">
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--force-image-upgrade fc-item--has-image js-fc-item tone-news--item fc-item--list-mobile fc-item--list-tablet js-snappable" data-link-name="news | group-0 | card-7" data-item-visibility="all" data-test-id="facia-card" data-id="us-news/2017/oct/12/trump-criticises-puerto-rico-hurricane-aid-cannot-go-on-forever" data-loyalty-short-url="/p/7cen4">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/us-news/2017/oct/12/trump-criticises-puerto-rico-hurricane-aid-cannot-go-on-forever" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Donald Trump</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">President hints at ending aid as Puerto Ricans forced to drink polluted water</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/us-news/2017/oct/12/trump-criticises-puerto-rico-hurricane-aid-cannot-go-on-forever" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">President hints at ending aid as Puerto Ricans forced to drink polluted water</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--force-image-upgrade fc-item--has-image js-fc-item tone-news--item fc-item--list-mobile fc-item--list-tablet js-snappable" data-link-name="news | group-0 | card-8" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/pakistan-rescues-canadian-american-family-hostages-haqqani" data-loyalty-short-url="/p/7cenz">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/pakistan-rescues-canadian-american-family-hostages-haqqani" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Taliban</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Pakistan rescues Canadian-American family held for five years</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/pakistan-rescues-canadian-american-family-hostages-haqqani" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Pakistan rescues Canadian-American family held for five years</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--force-image-upgrade fc-item--has-image js-fc-item tone-news--item fc-item--list-mobile fc-item--list-tablet js-snappable" data-link-name="news | group-0 | card-9" data-item-visibility="all" data-test-id="facia-card" data-id="global-development/2017/oct/12/yemen-cholera-outbreak-worst-in-history-1-million-cases-by-end-of-year" data-loyalty-short-url="/p/7cbc5">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/global-development/2017/oct/12/yemen-cholera-outbreak-worst-in-history-1-million-cases-by-end-of-year" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Yemen</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Cholera outbreak now the worst in history as millionth case looms</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/global-development/2017/oct/12/yemen-cholera-outbreak-worst-in-history-1-million-cases-by-end-of-year" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Cholera outbreak now the worst in history as millionth case looms</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--force-image-upgrade fc-item--has-image js-fc-item tone-news--item fc-item--list-mobile fc-item--list-tablet js-snappable" data-link-name="news | group-0 | card-10" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/catalan-president-accuses-mariano-rajoy-of-ignoring-call-for-talks-carles-puigdemont" data-loyalty-short-url="/p/7ce9a">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/catalan-president-accuses-mariano-rajoy-of-ignoring-call-for-talks-carles-puigdemont" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Spain crisis</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Catalan president accuses Rajoy of ignoring call for talks</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/catalan-president-accuses-mariano-rajoy-of-ignoring-call-for-talks-carles-puigdemont" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Catalan president accuses Rajoy of ignoring call for talks</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--force-image-upgrade fc-item--has-image js-fc-item tone-news--item fc-item--list-mobile fc-item--list-tablet js-snappable" data-link-name="news | group-0 | card-11" data-item-visibility="all" data-test-id="facia-card" data-id="uk-news/2017/oct/12/paramedics-save-man-after-whole-fish-jumps-down-throat" data-loyalty-short-url="/p/7cf43">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/uk-news/2017/oct/12/paramedics-save-man-after-whole-fish-jumps-down-throat" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Sole survivor</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Paramedics save man after he swallows whole live dover sole</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/uk-news/2017/oct/12/paramedics-save-man-after-whole-fish-jumps-down-throat" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Paramedics save man after he swallows whole live dover sole</a>
</div>
</div> </li>
</ul> </li>
</ul>
</div>
</div>
</div>
</section>
<section class="fc-container__mpu--mobile">
<div id="dfp-ad--top-above-nav--mobile" class="js-ad-slot ad-slot ad-slot--top-above-nav ad-slot--container-inline ad-slot--mobile mobile-only" data-link-name="ad slot top-above-nav" data-name="top-above-nav" data-mobile="1,1|2,2|88,70|88,71|300,250|fluid">
</div>
</section>
<section id="spotlight" class="fc-container fc-container--will-have-toggle js-container--toggle " data-link-name="container-2 | spotlight" data-id="4384b368-3392-4795-b6b1-d1fa44fe909b" data-component="spotlight" aria-expanded="true">
<div class="fc-container__inner">
<div class="fc-container__header
                js-container__header
                ">
<div class="fc-container__header__title">
<span tabindex="0">spotlight</span>
</div>
</div>
<div class="fc-container--rolled-up-hide fc-container__body" data-title="spotlight" data-id="4384b368-3392-4795-b6b1-d1fa44fe909b">
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-4 fc-slice fc-slice--qqq-q">
<li class="fc-slice__item l-row__item l-row__item--span-3 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-feature--item fc-item--standard-mobile fc-item--three-quarters-tablet js-snappable" data-link-name="feature | group-2+ | card-1" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/its-become-a-monster-is-irans-revolutionary-guard-a-terror-group" data-loyalty-short-url="/p/7c9ja">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="460px" srcset="https://i.guim.co.uk/img/media/80385f381d67c696b9120efe939d979d0c1f17ca/0_103_3000_1800/master/3000.jpg?w=460&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=3f67f368eae7085129d99fe18cfebb43 920w">
<source media="(min-width: 980px)" sizes="460px" srcset="https://i.guim.co.uk/img/media/80385f381d67c696b9120efe939d979d0c1f17ca/0_103_3000_1800/master/3000.jpg?w=460&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e233379424c73fc7fefd6f1d4deca275 460w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="340px" srcset="https://i.guim.co.uk/img/media/80385f381d67c696b9120efe939d979d0c1f17ca/0_103_3000_1800/master/3000.jpg?w=340&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=684d98f2dba8c2787ca5a1475225f6f8 680w">
<source media="(min-width: 740px)" sizes="340px" srcset="https://i.guim.co.uk/img/media/80385f381d67c696b9120efe939d979d0c1f17ca/0_103_3000_1800/master/3000.jpg?w=340&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=816f9187e53d070fbf6b109ce7187a72 340w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="95vw" srcset="https://i.guim.co.uk/img/media/80385f381d67c696b9120efe939d979d0c1f17ca/0_103_3000_1800/master/3000.jpg?w=460&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=3f67f368eae7085129d99fe18cfebb43 920w, https://i.guim.co.uk/img/media/80385f381d67c696b9120efe939d979d0c1f17ca/0_103_3000_1800/master/3000.jpg?w=340&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=684d98f2dba8c2787ca5a1475225f6f8 680w, https://i.guim.co.uk/img/media/80385f381d67c696b9120efe939d979d0c1f17ca/0_103_3000_1800/master/3000.jpg?w=445&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=0e67956785172403588728c0f2b7c069 890w, https://i.guim.co.uk/img/media/80385f381d67c696b9120efe939d979d0c1f17ca/0_103_3000_1800/master/3000.jpg?w=605&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=ba24dce7e353a70e2417f609f79663e5 1210w">
<source media="(min-width: 0px)" sizes="95vw" srcset="https://i.guim.co.uk/img/media/80385f381d67c696b9120efe939d979d0c1f17ca/0_103_3000_1800/master/3000.jpg?w=460&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e233379424c73fc7fefd6f1d4deca275 460w, https://i.guim.co.uk/img/media/80385f381d67c696b9120efe939d979d0c1f17ca/0_103_3000_1800/master/3000.jpg?w=340&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=816f9187e53d070fbf6b109ce7187a72 340w, https://i.guim.co.uk/img/media/80385f381d67c696b9120efe939d979d0c1f17ca/0_103_3000_1800/master/3000.jpg?w=445&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=64df2ecc0184afb3ed2cc0961561e7ea 445w, https://i.guim.co.uk/img/media/80385f381d67c696b9120efe939d979d0c1f17ca/0_103_3000_1800/master/3000.jpg?w=605&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=7c8a05a949e7023b9ca32b4ef4d3f298 605w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/its-become-a-monster-is-irans-revolutionary-guard-a-terror-group" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">'It's become a monster'</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Is Iran's revolutionary guard a terror group?</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
Tehran has promised ‘crushing’ retaliation if the US decides to add the powerful force to list of terrorist groups
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/its-become-a-monster-is-irans-revolutionary-guard-a-terror-group" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Is Iran's revolutionary guard a terror group?</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-comment--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="comment | group-2 | card-2" data-item-visibility="all" data-test-id="facia-card" data-id="commentisfree/2017/oct/12/banning-rose-mcgowan-shows-nothings-changed-twitter-weinstein" data-loyalty-short-url="/p/7cedh">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/06e313c4f93f1dd1f613b475a922bac37df480d5/600_222_2562_1537/master/2562.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=1995a1d7f38eea552de20f7e70cc1049 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/06e313c4f93f1dd1f613b475a922bac37df480d5/600_222_2562_1537/master/2562.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=d42224cb96a4b66607197916b2e8530d 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/06e313c4f93f1dd1f613b475a922bac37df480d5/600_222_2562_1537/master/2562.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=a9455f6d4562250979a5562f29e0e88d 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/06e313c4f93f1dd1f613b475a922bac37df480d5/600_222_2562_1537/master/2562.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e8f6c0f8a61fc1ed552fbe355c852151 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/06e313c4f93f1dd1f613b475a922bac37df480d5/600_222_2562_1537/master/2562.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=0d458e454059dce27098c68d34be3cff 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/06e313c4f93f1dd1f613b475a922bac37df480d5/600_222_2562_1537/master/2562.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=33ddee6cd3b0d21631fe10087307ef3f 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/commentisfree/2017/oct/12/banning-rose-mcgowan-shows-nothings-changed-twitter-weinstein" class="fc-item__link" data-link-name="article"> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">The banning of Rose McGowan shows that nothing's changed at Twitter</span></span> </a></h2>
<div class="fc-item__byline">
Hannah Jane Parkinson
</div>
</div>
<div class="fc-item__standfirst">
The platform ‘sucks’ at dealing with abuse, its ex-CEO said. So you’d think they’d have learned not to silence an actor calling out Weinstein’s alleged sexual abuse, says Guardian columnist Hannah Jane Parkinson
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/commentisfree/2017/oct/12/banning-rose-mcgowan-shows-nothings-changed-twitter-weinstein" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">The banning of Rose McGowan shows that nothing's changed at Twitter</a>
</div>
</div> </li>
</ul>
</div>
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-4 fc-slice fc-slice--h14-q-q">
<li class="fc-slice__item l-row__item l-row__item--span-2">
<ul class="u-unstyled l-list l-list--columns-2 l-list--rows-1">
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-sublinks-1 js-fc-item tone-news--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="news | group-1 | card-3" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/sally-jones-the-uk-punk-singer-who-became-isiss-white-widow" data-loyalty-short-url="/p/7cetb">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/a84e6f943f04892446a063de465d305ffa9198e8/0_0_1261_757/master/1261.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=a5338adbbcb63cdfbd8ea99fd0ef6449 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/a84e6f943f04892446a063de465d305ffa9198e8/0_0_1261_757/master/1261.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=f50e14effe511f6e4ced8fe68d135233 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/a84e6f943f04892446a063de465d305ffa9198e8/0_0_1261_757/master/1261.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=c65b027e38aa1b42bf0a257973d3d939 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/a84e6f943f04892446a063de465d305ffa9198e8/0_0_1261_757/master/1261.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=b7a6d6e21881afa104ea9f9ece19c60e 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/a84e6f943f04892446a063de465d305ffa9198e8/0_0_1261_757/master/1261.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=47d7e839733fd876b21eb52293d45743 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/a84e6f943f04892446a063de465d305ffa9198e8/0_0_1261_757/master/1261.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=1ba20e46f28e3ddd12ca9453adaf8759 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/sally-jones-the-uk-punk-singer-who-became-isiss-white-widow" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Sally Jones</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">The UK punk singer who became Isis's 'white widow'</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
Woman reportedly killed in US airstrike convinced hundreds of women to join her fighting for Islamic State
</div>
<div class="fc-item__footer--vertical" aria-hidden="true">
<ul class="fc-sublinks u-unstyled u-faux-block-link__promote">
<li class="fc-sublink tone-analysis--sublink" data-link-name="sublinks | 1"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/world/2017/oct/12/is-targeting-of-isis-member-sally-jones-legally-justified" class="fc-sublink__link" data-link-name="article"><span class="fc-sublink__kicker">Analysis</span> Is the targeting of Sally Jones legally justified?</a> </h3> </li>
</ul>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<footer class="fc-item__footer--horizontal">
<ul class="fc-sublinks u-unstyled u-faux-block-link__promote">
<li class="fc-sublink tone-analysis--sublink" data-link-name="sublinks | 1"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/world/2017/oct/12/is-targeting-of-isis-member-sally-jones-legally-justified" class="fc-sublink__link" data-link-name="article"><span class="fc-sublink__kicker">Analysis</span> Is the targeting of Sally Jones legally justified?</a> </h3> </li>
</ul>
</footer>
<a href="https://www.theguardian.com/world/2017/oct/12/sally-jones-the-uk-punk-singer-who-became-isiss-white-widow" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">The UK punk singer who became Isis's 'white widow'</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-feature--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="feature | group-1+ | card-4" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/kyrgyzstan-set-for-freest-and-fairest-election-in-central-asian-history" data-loyalty-short-url="/p/7bj4f">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/d9c6b044f97354988589e0f9f7b9e7c41c93d4a7/0_237_3000_1800/master/3000.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=55b26af896cecaf6fe0f70db1e82765b 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/d9c6b044f97354988589e0f9f7b9e7c41c93d4a7/0_237_3000_1800/master/3000.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=7a12f31fcda65c8c1275f2b22c83bab7 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/d9c6b044f97354988589e0f9f7b9e7c41c93d4a7/0_237_3000_1800/master/3000.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=60354ee5a3128a2953953a285c6d856b 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/d9c6b044f97354988589e0f9f7b9e7c41c93d4a7/0_237_3000_1800/master/3000.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=59d7c433a37cf52ab5a408bba1652828 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/d9c6b044f97354988589e0f9f7b9e7c41c93d4a7/0_237_3000_1800/master/3000.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=90fb0be0f29678908842a805d2e7c78e 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/d9c6b044f97354988589e0f9f7b9e7c41c93d4a7/0_237_3000_1800/master/3000.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=1739d4244201eee82663ac6c23f78b35 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/kyrgyzstan-set-for-freest-and-fairest-election-in-central-asian-history" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Democratic anomaly</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Kyrgyzstan bucks the central Asian trend for rigged elections</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
The former Soviet republic is a democratic regional anomaly, where the president will not win 105% of the vote on Sunday.
<strong>Shaun Walker </strong>reports from Bishkek
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/kyrgyzstan-set-for-freest-and-fairest-election-in-central-asian-history" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Kyrgyzstan bucks the central Asian trend for rigged elections</a>
</div>
</div> </li>
</ul> </li>
<li class="fc-slice__item l-row__item l-row__item--span-2">
<ul class="u-unstyled l-list l-list--columns-1 l-list--rows-4">
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-feature--item fc-item--list-mobile fc-item--list-media-tablet js-snappable" data-link-name="feature | group-0 | card-5" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/spanish-ex-monk-mission-build-own-cathedral-justo-gallego" data-loyalty-short-url="/p/6jghn">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/e3f9820f6470e891c370f3d6e43be73dc06a79c1/0_134_1024_614/master/1024.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=b268ec7d07ac038dfc37edabaaebe6de 280w">
<source media="(min-width: 980px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/e3f9820f6470e891c370f3d6e43be73dc06a79c1/0_134_1024_614/master/1024.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=8c19622bae5940c782cb85370c023a1c 140w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/e3f9820f6470e891c370f3d6e43be73dc06a79c1/0_134_1024_614/master/1024.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=b268ec7d07ac038dfc37edabaaebe6de 280w">
<source media="(min-width: 740px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/e3f9820f6470e891c370f3d6e43be73dc06a79c1/0_134_1024_614/master/1024.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=8c19622bae5940c782cb85370c023a1c 140w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/spanish-ex-monk-mission-build-own-cathedral-justo-gallego" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Keeping the faith</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">The Spanish ex-monk on a 56-year mission to build his own cathedral</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/spanish-ex-monk-mission-build-own-cathedral-justo-gallego" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">The Spanish ex-monk on a 56-year mission to build his own cathedral</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-feature--item fc-item--list-mobile fc-item--list-media-tablet js-snappable" data-discussion-id="/p/7bg6c" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/tv-and-radio/2017/oct/12/mindhunter-jonathan-groff-david-fincher-serial-killer-gay-hollywood-frozen-hamilton#comments" data-link-name="feature | group-0 | card-6" data-item-visibility="all" data-test-id="facia-card" data-id="tv-and-radio/2017/oct/12/mindhunter-jonathan-groff-david-fincher-serial-killer-gay-hollywood-frozen-hamilton" data-loyalty-short-url="/p/7bg6c">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/f2330771cec2e7d6a369c958ad9c98b4b88fc6b9/0_157_8280_4969/master/8280.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=da224fbafb41a5fff7bfe0121f9db280 280w">
<source media="(min-width: 980px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/f2330771cec2e7d6a369c958ad9c98b4b88fc6b9/0_157_8280_4969/master/8280.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=236d6916cc3388fc7b1c69aceccdf86c 140w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/f2330771cec2e7d6a369c958ad9c98b4b88fc6b9/0_157_8280_4969/master/8280.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=da224fbafb41a5fff7bfe0121f9db280 280w">
<source media="(min-width: 740px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/f2330771cec2e7d6a369c958ad9c98b4b88fc6b9/0_157_8280_4969/master/8280.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=236d6916cc3388fc7b1c69aceccdf86c 140w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/tv-and-radio/2017/oct/12/mindhunter-jonathan-groff-david-fincher-serial-killer-gay-hollywood-frozen-hamilton" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Jonathan Groff on Mindhunter</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">I walked into makeup and saw a scalped woman's head</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/tv-and-radio/2017/oct/12/mindhunter-jonathan-groff-david-fincher-serial-killer-gay-hollywood-frozen-hamilton" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">I walked into makeup and saw a scalped woman's head</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-review--item fc-item--list-mobile fc-item--list-media-tablet js-snappable" data-discussion-id="/p/7c9nv" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/film/2017/oct/12/the-snowman-review-michael-fassbender-tomas-alfredson-jo-nesbo#comments" data-link-name="review | group-0 | card-7" data-item-visibility="all" data-test-id="facia-card" data-id="film/2017/oct/12/the-snowman-review-michael-fassbender-tomas-alfredson-jo-nesbo" data-loyalty-short-url="/p/7c9nv">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/3ba9328378d96fa171c8c3d94b1060916ab8cf99/333_500_3368_2021/master/3368.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=acaf017e789d3376909fb682430238cf 280w">
<source media="(min-width: 980px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/3ba9328378d96fa171c8c3d94b1060916ab8cf99/333_500_3368_2021/master/3368.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e420f5527dd5b24b1033b552a9823652 140w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/3ba9328378d96fa171c8c3d94b1060916ab8cf99/333_500_3368_2021/master/3368.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=acaf017e789d3376909fb682430238cf 280w">
<source media="(min-width: 740px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/3ba9328378d96fa171c8c3d94b1060916ab8cf99/333_500_3368_2021/master/3368.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e420f5527dd5b24b1033b552a9823652 140w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/film/2017/oct/12/the-snowman-review-michael-fassbender-tomas-alfredson-jo-nesbo" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">The Snowman</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Michael Fassbender plays it cool in watchable Jo Nesbø thriller</span></span> </a></h2>
<div class="stars" role="presentation">
<span class="inline-star inline-icon star__item star__item--golden">
<svg width="14" height="13" viewbox="0 0 14 13" class="star__item__svg star__item--golden__svg inline-star__svg inline-icon__svg">
<path d="M0 5.2L3.7 8l-1.4 4.6.5.4 3.7-2.8 3.7 2.8.5-.4L9.3 8 13 5.2l-.2-.6H8.2L6.8 0h-.6L4.8 4.6H.2l-.2.6z"/>
</svg> </span>
<span class="inline-star inline-icon star__item star__item--golden">
<svg width="14" height="13" viewbox="0 0 14 13" class="star__item__svg star__item--golden__svg inline-star__svg inline-icon__svg">
<path d="M0 5.2L3.7 8l-1.4 4.6.5.4 3.7-2.8 3.7 2.8.5-.4L9.3 8 13 5.2l-.2-.6H8.2L6.8 0h-.6L4.8 4.6H.2l-.2.6z"/>
</svg> </span>
<span class="inline-star inline-icon star__item star__item--golden">
<svg width="14" height="13" viewbox="0 0 14 13" class="star__item__svg star__item--golden__svg inline-star__svg inline-icon__svg">
<path d="M0 5.2L3.7 8l-1.4 4.6.5.4 3.7-2.8 3.7 2.8.5-.4L9.3 8 13 5.2l-.2-.6H8.2L6.8 0h-.6L4.8 4.6H.2l-.2.6z"/>
</svg> </span>
<span class="inline-star inline-icon star__item star__item--grey">
<svg width="14" height="13" viewbox="0 0 14 13" class="star__item__svg star__item--grey__svg inline-star__svg inline-icon__svg">
<path d="M0 5.2L3.7 8l-1.4 4.6.5.4 3.7-2.8 3.7 2.8.5-.4L9.3 8 13 5.2l-.2-.6H8.2L6.8 0h-.6L4.8 4.6H.2l-.2.6z"/>
</svg> </span>
<span class="inline-star inline-icon star__item star__item--grey">
<svg width="14" height="13" viewbox="0 0 14 13" class="star__item__svg star__item--grey__svg inline-star__svg inline-icon__svg">
<path d="M0 5.2L3.7 8l-1.4 4.6.5.4 3.7-2.8 3.7 2.8.5-.4L9.3 8 13 5.2l-.2-.6H8.2L6.8 0h-.6L4.8 4.6H.2l-.2.6z"/>
</svg> </span>
</div>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/film/2017/oct/12/the-snowman-review-michael-fassbender-tomas-alfredson-jo-nesbo" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Michael Fassbender plays it cool in watchable Jo Nesbø thriller</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--list-mobile fc-item--list-media-tablet js-snappable" data-link-name="news | group-0 | card-8" data-item-visibility="all" data-test-id="facia-card" data-id="technology/2017/oct/12/apple-id-iphone-password-demands-security-flaw-phishing-attack-fake-sign-in-request" data-loyalty-short-url="/p/7ceeb">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/6cbca124a4b96d42f371e5eee66ad20b208f795d/558_335_3401_2041/master/3401.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=72a781a823a4d231e75258fe67ab0e72 280w">
<source media="(min-width: 980px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/6cbca124a4b96d42f371e5eee66ad20b208f795d/558_335_3401_2041/master/3401.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=1d9b62000cf99b427a8f736c28fdfc1b 140w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/6cbca124a4b96d42f371e5eee66ad20b208f795d/558_335_3401_2041/master/3401.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=72a781a823a4d231e75258fe67ab0e72 280w">
<source media="(min-width: 740px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/6cbca124a4b96d42f371e5eee66ad20b208f795d/558_335_3401_2041/master/3401.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=1d9b62000cf99b427a8f736c28fdfc1b 140w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/technology/2017/oct/12/apple-id-iphone-password-demands-security-flaw-phishing-attack-fake-sign-in-request" class="fc-item__link" data-link-name="article"> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">Your iPhone's password demands aren't just annoying. They're a security flaw</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/technology/2017/oct/12/apple-id-iphone-password-demands-security-flaw-phishing-attack-fake-sign-in-request" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Your iPhone's password demands aren't just annoying. They're a security flaw</a>
</div>
</div> </li>
</ul> </li>
</ul>
</div>
</div>
</div>
</section>
<section id="sport" class="fc-container fc-container--dynamic-slow-mpu fc-container--has-show-more fc-container--will-have-toggle js-container--toggle " data-link-name="container-3 | sport" data-id="da673281-d002-4406-9c75-d0bbdecc124f" data-component="sport" aria-expanded="true">
<div class="fc-container__inner">
<div class="fc-container__header
                js-container__header
                ">
<div class="fc-container__header__title">
<a data-link-name="section heading" href="https://www.theguardian.com/uk/sport"> <span class="fc-container__title__text">sport</span> </a>
</div>
</div>
<ul class="treats__container">
<li class="treats__list-item"> <a href="/sport/2017/may/15/the-recap-sign-up-for-the-best-of-the-guardians-sport-coverage" data-link-name="treat | 1 | The Recap sports email - sign up" class="treats__treat">The Recap sports email - sign up</a> </li>
</ul>
<div class="fc-container--rolled-up-hide fc-container__body fc-show-more--hidden js-container--fc-show-more" data-title="sport" data-id="da673281-d002-4406-9c75-d0bbdecc124f">
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-4 fc-slice fc-slice--h-q-q">
<li class="fc-slice__item l-row__item l-row__item--span-2 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--standard-mobile fc-item--half-tablet js-snappable" data-link-name="news | group-1 | card-1" data-item-visibility="all" data-test-id="facia-card" data-id="football/2017/oct/12/psg-chairman-nasser-al-khelaifi-accused-world-cup-bribery" data-loyalty-short-url="/p/7cf3z">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="460px" srcset="https://i.guim.co.uk/img/media/153f5f301ff69b4a010775f9885354b0e96f3bc9/0_253_5184_3110/master/5184.jpg?w=460&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=2c21a6ce69bc7e043d456201ebcd2449 920w">
<source media="(min-width: 980px)" sizes="460px" srcset="https://i.guim.co.uk/img/media/153f5f301ff69b4a010775f9885354b0e96f3bc9/0_253_5184_3110/master/5184.jpg?w=460&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e54a579b9e772f0f55ddd00f88a1abe5 460w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="340px" srcset="https://i.guim.co.uk/img/media/153f5f301ff69b4a010775f9885354b0e96f3bc9/0_253_5184_3110/master/5184.jpg?w=340&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=0afecd34abcd36ae88004be05c92feaf 680w">
<source media="(min-width: 740px)" sizes="340px" srcset="https://i.guim.co.uk/img/media/153f5f301ff69b4a010775f9885354b0e96f3bc9/0_253_5184_3110/master/5184.jpg?w=340&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=d6c4bea5caaef41b5f61c8e84e49952e 340w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="95vw" srcset="https://i.guim.co.uk/img/media/153f5f301ff69b4a010775f9885354b0e96f3bc9/0_253_5184_3110/master/5184.jpg?w=460&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=2c21a6ce69bc7e043d456201ebcd2449 920w, https://i.guim.co.uk/img/media/153f5f301ff69b4a010775f9885354b0e96f3bc9/0_253_5184_3110/master/5184.jpg?w=340&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=0afecd34abcd36ae88004be05c92feaf 680w, https://i.guim.co.uk/img/media/153f5f301ff69b4a010775f9885354b0e96f3bc9/0_253_5184_3110/master/5184.jpg?w=445&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=6b297395ee803d8efd263e2509461b3a 890w, https://i.guim.co.uk/img/media/153f5f301ff69b4a010775f9885354b0e96f3bc9/0_253_5184_3110/master/5184.jpg?w=605&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=a04aca9e8796f81caa6c973285cf4091 1210w">
<source media="(min-width: 0px)" sizes="95vw" srcset="https://i.guim.co.uk/img/media/153f5f301ff69b4a010775f9885354b0e96f3bc9/0_253_5184_3110/master/5184.jpg?w=460&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e54a579b9e772f0f55ddd00f88a1abe5 460w, https://i.guim.co.uk/img/media/153f5f301ff69b4a010775f9885354b0e96f3bc9/0_253_5184_3110/master/5184.jpg?w=340&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=d6c4bea5caaef41b5f61c8e84e49952e 340w, https://i.guim.co.uk/img/media/153f5f301ff69b4a010775f9885354b0e96f3bc9/0_253_5184_3110/master/5184.jpg?w=445&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e254568bedbaf2e3b6367be8af0e8656 445w, https://i.guim.co.uk/img/media/153f5f301ff69b4a010775f9885354b0e96f3bc9/0_253_5184_3110/master/5184.jpg?w=605&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=039ccb00dccac2fcde720e447e7971f6 605w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/football/2017/oct/12/psg-chairman-nasser-al-khelaifi-accused-world-cup-bribery" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">News</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">PSG chairman Al-Khelaifi accused of World Cup bribery by Swiss prosecutor</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
The office of the Swiss attorney general has opened criminal proceedings against the PSG’s Nasser al-Khelaifi and the former Fifa secretary general Jérôme Valcke in relation to World Cup media rights
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/football/2017/oct/12/psg-chairman-nasser-al-khelaifi-accused-world-cup-bribery" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">PSG chairman Al-Khelaifi accused of World Cup bribery by Swiss prosecutor</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-feature--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-discussion-id="/p/7cf4b" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/sport/blog/2017/oct/12/aaron-judge-mlb-new-york-yankees-cleveland-indians#comments" data-link-name="feature | group-1 | card-2" data-item-visibility="all" data-test-id="facia-card" data-id="sport/blog/2017/oct/12/aaron-judge-mlb-new-york-yankees-cleveland-indians" data-loyalty-short-url="/p/7cf4b">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/3d1c875a2ecc29e52a45d752516021db434860f2/211_89_2466_1480/master/2466.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=e645a782fcfc60ca7c18c7d2817b69ed 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/3d1c875a2ecc29e52a45d752516021db434860f2/211_89_2466_1480/master/2466.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=1651020cf9c29b509403e52342e9f7c2 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/3d1c875a2ecc29e52a45d752516021db434860f2/211_89_2466_1480/master/2466.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=06c01e3b92d1b217190d149bf95cdc03 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/3d1c875a2ecc29e52a45d752516021db434860f2/211_89_2466_1480/master/2466.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=8261ba4ae450e7632ac7fe270a48d24b 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/3d1c875a2ecc29e52a45d752516021db434860f2/211_89_2466_1480/master/2466.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=45cce5823e576cd57f84cc45f13fd699 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/3d1c875a2ecc29e52a45d752516021db434860f2/211_89_2466_1480/master/2466.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=6a2285d2680e74af0b9ee3bdfd198385 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/sport/blog/2017/oct/12/aaron-judge-mlb-new-york-yankees-cleveland-indians" class="fc-item__link" data-link-name="article"> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">Judge catches fans’ hearts in an MLB season for the ages</span></span> </a></h2>
<div class="fc-item__byline">
Matthew Engel
</div>
</div>
<div class="fc-item__standfirst">
From pre-season fringe player to MLB star, the rookie has taken the US by storm this summer in the Yankees’ march to unlikely post-season success
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/sport/blog/2017/oct/12/aaron-judge-mlb-new-york-yankees-cleveland-indians" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Judge catches fans’ hearts in an MLB season for the ages</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-feature--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-discussion-id="/p/7cfae" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/sport/2017/oct/12/european-rugby-champions-cup-2017-18-pool-by-pool-guide#comments" data-link-name="feature | group-1 | card-3" data-item-visibility="all" data-test-id="facia-card" data-id="sport/2017/oct/12/european-rugby-champions-cup-2017-18-pool-by-pool-guide" data-loyalty-short-url="/p/7cfae">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/ed8310016cd83f07c895ad04a85b4fb11cc04510/0_0_2560_1536/master/2560.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=7a9333d830c64e0310ba56f5576c403c 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/ed8310016cd83f07c895ad04a85b4fb11cc04510/0_0_2560_1536/master/2560.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=526585ddd53112e671b33ed058ce84a4 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/ed8310016cd83f07c895ad04a85b4fb11cc04510/0_0_2560_1536/master/2560.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=c949ce518f64d47d4457583476c0ad8d 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/ed8310016cd83f07c895ad04a85b4fb11cc04510/0_0_2560_1536/master/2560.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=039df21f179dad3e69ad1ba7384b86d1 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/ed8310016cd83f07c895ad04a85b4fb11cc04510/0_0_2560_1536/master/2560.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=8a0fbd3cd71c7e26e4427aa2cbae777a 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/ed8310016cd83f07c895ad04a85b4fb11cc04510/0_0_2560_1536/master/2560.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=4f67ba9c39b2c942d875c78ad2c600ff 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/sport/2017/oct/12/european-rugby-champions-cup-2017-18-pool-by-pool-guide" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">European Rugby Champions Cup</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Pool-by-pool guide to this season's tournament</span></span> </a></h2>
<div class="fc-item__byline">
Gerard Meagher
</div>
</div>
<div class="fc-item__standfirst">
Can Saracens complete a hat-trick of titles? Will La Rochelle make waves on their debut? And are Scarlets the pick of the Pro14 sides? We assess the contenders
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/sport/2017/oct/12/european-rugby-champions-cup-2017-18-pool-by-pool-guide" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Pool-by-pool guide to this season's tournament</a>
</div>
</div> </li>
</ul>
</div>
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-2 fc-slice fc-slice--hl3-mpu">
<li class="fc-slice__item l-row__item l-row__item--span-1">
<ul class="u-unstyled l-list l-list--columns-1 l-list--rows-3">
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-comment--item fc-item--list-media-mobile fc-item--list-media-tablet js-snappable" data-discussion-id="/p/7cfm8" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/football/blog/2017/oct/12/jurgen-klopp-liverpool-how-much-progress-manchester-united#comments" data-link-name="comment | group-0 | card-4" data-item-visibility="all" data-test-id="facia-card" data-id="football/blog/2017/oct/12/jurgen-klopp-liverpool-how-much-progress-manchester-united" data-loyalty-short-url="/p/7cfm8">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/720e07aaa95f6106a2f7b2ae49b358b64e8cc548/53_187_2029_1217/master/2029.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=18728d0cf9d1921c6273dd946c0aba19 280w">
<source media="(min-width: 980px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/720e07aaa95f6106a2f7b2ae49b358b64e8cc548/53_187_2029_1217/master/2029.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=a427d8593c6ae7140287b4be32e625f9 140w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/720e07aaa95f6106a2f7b2ae49b358b64e8cc548/53_187_2029_1217/master/2029.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=18728d0cf9d1921c6273dd946c0aba19 280w">
<source media="(min-width: 740px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/720e07aaa95f6106a2f7b2ae49b358b64e8cc548/53_187_2029_1217/master/2029.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=a427d8593c6ae7140287b4be32e625f9 140w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/720e07aaa95f6106a2f7b2ae49b358b64e8cc548/53_187_2029_1217/master/2029.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=20866b8924597b92e407949897ecdae9 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/720e07aaa95f6106a2f7b2ae49b358b64e8cc548/53_187_2029_1217/master/2029.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=d2c911f666ad2ad0aba73976ce5cd387 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/football/blog/2017/oct/12/jurgen-klopp-liverpool-how-much-progress-manchester-united" class="fc-item__link" data-link-name="article"> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">Klopp two years on – how much progress has been made?</span></span> </a></h2>
<div class="fc-item__byline">
Barney Ronay
</div>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/football/blog/2017/oct/12/jurgen-klopp-liverpool-how-much-progress-manchester-united" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Klopp two years on – how much progress has been made?</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--audio fc-item--has-image fc-item--has-metadata fc-item--is-commentable fc-item--is-media-link js-fc-item tone-media--item fc-item--list-media-mobile fc-item--list-media-tablet js-snappable" data-discussion-id="/p/7cf7z" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/football/audio/2017/oct/12/viking-claps-for-iceland-golf-claps-for-the-us-football-weekly-extra#comments" data-link-name="media | group-0 | card-5" data-item-visibility="all" data-test-id="facia-card" data-id="football/audio/2017/oct/12/viking-claps-for-iceland-golf-claps-for-the-us-football-weekly-extra" data-loyalty-short-url="/p/7cf7z">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/38efe60907c5908acf72390cf187d326494da349/387_770_4611_2766/master/4611.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=4b1bffa00d54e6563b30607d223b07d6 280w">
<source media="(min-width: 980px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/38efe60907c5908acf72390cf187d326494da349/387_770_4611_2766/master/4611.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=4ddd2f1b3897936f2c247cbed72987c9 140w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/38efe60907c5908acf72390cf187d326494da349/387_770_4611_2766/master/4611.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=4b1bffa00d54e6563b30607d223b07d6 280w">
<source media="(min-width: 740px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/38efe60907c5908acf72390cf187d326494da349/387_770_4611_2766/master/4611.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=4ddd2f1b3897936f2c247cbed72987c9 140w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/38efe60907c5908acf72390cf187d326494da349/387_770_4611_2766/master/4611.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=e386d0305bfaec738a912dcc8b0fbc6a 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/38efe60907c5908acf72390cf187d326494da349/387_770_4611_2766/master/4611.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=6aec1dff8112be57d4c186aa8893e592 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/football/audio/2017/oct/12/viking-claps-for-iceland-golf-claps-for-the-us-football-weekly-extra" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Football Weekly Extra</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-volume-high inline-icon ">
<svg width="16" height="13" viewbox="0 0 16 13" class="inline-volume-high__svg inline-icon__svg">
<path d="M3 4H1L0 5v3l1 1h2l4 4h1V0H7L3 4zm11.7 2.5c0 2-.7 3.8-1.8 5.2l.4.4c1.6-1.3 2.6-3.3 2.6-5.6s-1-4.3-2.6-5.6l-.4.4c1.2 1.5 1.8 3.3 1.8 5.2m-3.7 0c0 1.1-.3 2.2-.9 3.1l.5.5c.8-1 1.4-2.2 1.4-3.6s-.6-2.6-1.5-3.5l-.5.5c.6.8 1 1.9 1 3"/>
</svg> </span> <span class="js-headline-text">Viking claps for Iceland, golf claps for the US</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/football/audio/2017/oct/12/viking-claps-for-iceland-golf-claps-for-the-us-football-weekly-extra" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Viking claps for Iceland, golf claps for the US</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-feature--item fc-item--list-media-mobile fc-item--list-media-tablet js-snappable" data-discussion-id="/p/7ccce" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/sport/2017/oct/13/pat-cummins-interview-australia-ashes#comments" data-link-name="feature | group-0 | card-6" data-item-visibility="all" data-test-id="facia-card" data-id="sport/2017/oct/13/pat-cummins-interview-australia-ashes" data-loyalty-short-url="/p/7ccce">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/fc85c3af487b38d0c757d210bd2ae57be60c6427/9_472_4752_2851/master/4752.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=d924c94c89888f3762a5d358a7955d08 280w">
<source media="(min-width: 980px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/fc85c3af487b38d0c757d210bd2ae57be60c6427/9_472_4752_2851/master/4752.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=24dc34af5f0c48862a273e427106717e 140w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/fc85c3af487b38d0c757d210bd2ae57be60c6427/9_472_4752_2851/master/4752.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=d924c94c89888f3762a5d358a7955d08 280w">
<source media="(min-width: 740px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/fc85c3af487b38d0c757d210bd2ae57be60c6427/9_472_4752_2851/master/4752.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=24dc34af5f0c48862a273e427106717e 140w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/fc85c3af487b38d0c757d210bd2ae57be60c6427/9_472_4752_2851/master/4752.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=7dd6a775ffd33fe4e02f9df954f1bbe8 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/fc85c3af487b38d0c757d210bd2ae57be60c6427/9_472_4752_2851/master/4752.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=73c7a39be31b2d0145abbffe95150285 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/sport/2017/oct/13/pat-cummins-interview-australia-ashes" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Australia's Cummins</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">Being intimidating is about using body language</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/sport/2017/oct/13/pat-cummins-interview-australia-ashes" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Being intimidating is about using body language</a>
</div>
</div> </li>
</ul> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 fc-slice__item--mpu-candidate">
<div id="dfp-ad--inline1" class="js-ad-slot ad-slot ad-slot--inline1 ad-slot--container-inline hide-until-tablet" data-link-name="ad slot inline1" data-name="inline1" data-mobile="1,1|2,2|300,250|fluid">
</div> </li>
</ul>
</div>
<div class="js-show-more-placeholder"></div>
<button class="button button--medium button--primary button--show-more collection__show-more js-show-more-button modern-visible" data-test-id="show-more" data-link-name="more"> <span class="inline-plus inline-icon ">
<svg width="18" height="18" viewbox="0 0 18 18" class="inline-plus__svg inline-icon__svg">
<path d="M8.2 0h1.6l.4 7.8 7.8.4v1.6l-7.8.4-.4 7.8H8.2l-.4-7.8L0 9.8V8.2l7.8-.4.4-7.8z"/>
</svg> </span> <span class="inline-minus inline-icon ">
<svg width="32" height="32" viewbox="0 0 32 32" class="inline-minus__svg inline-icon__svg">
<path d="M5 15h22v3H5z"/>
</svg> </span> <span class="js-button-text">More sport</span> </button>
</div>
</div>
</section>
<section class="fc-container__mpu--mobile">
<div id="dfp-ad--inline1--mobile" class="js-ad-slot ad-slot ad-slot--inline1 ad-slot--container-inline ad-slot--mobile mobile-only" data-link-name="ad slot inline1" data-name="inline1" data-mobile="1,1|2,2|300,250|fluid">
</div>
</section>
<section id="documentaries" class="fc-container fc-container--thrasher fc-container--will-have-toggle flashing-image js-container--toggle " data-link-name="container-4 | documentaries" data-id="ede5db12-c072-445f-8910-0d5bfae7afc4" data-component="documentaries" aria-expanded="true">
<div class="fc-container__inner">
<div class="fc-container__header
                js-container__header
                ">
<div class="fc-container__header__title">
<span tabindex="0">documentaries</span>
</div>
</div>
<div class="fc-container--rolled-up-hide fc-container__body" data-title="documentaries" data-id="ede5db12-c072-445f-8910-0d5bfae7afc4">
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-1 fc-slice fc-slice--mf">
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="facia-snap facia-snap--default facia-snap-embed fc-item fc-item--has-no-image js-fc-item js-snap tone-news--item fc-item--fluid-mobile fc-item--fluid-tablet " data-link-name="news | group-0 | card-1" data-item-visibility="all" data-test-id="facia-card" data-id="snap/1507288114165" data-snap-type="json.html" data-snap-uri="https://interactive.guim.co.uk/thrashers/docs-home-match/source.json">
<div class="docs-home-match__wrapper">
<style>section#documentaries{background-color:#FFF}.docs-home-match__wrapper{position:relative;margin:0 -10px;background-color:#101820;color:#F6F6F6;font-family:"Guardian Egyptian Web","Guardian Text Egyptian Web",Georgia,serif;font-size:26px;line-height:26px;font-weight:200;overflow:hidden}@media all and (min-width:46.25em){.docs-home-match__wrapper{width:100%;margin:0}}.docs-home-match__wrapper .background{position:relative;z-index:10;height:216px}@media all and (min-width:41.25em){.docs-home-match__wrapper .background{height:280px}}@media all and (min-width:61.25em){.docs-home-match__wrapper{font-size:32px;line-height:32px}.docs-home-match__wrapper .background{height:320px}}.docs-home-match__wrapper .background .image{height:100%}.docs-home-match__wrapper .background .image:before{content:'';position:absolute;top:0;left:0;right:0;height:100px;z-index:11}@media all and (min-width:41.25em){.docs-home-match__wrapper .background .image:before{height:100%;width:480px}}@media all and (min-width:61.25em){.docs-home-match__wrapper .background .image:before{width:620px}}@media all and (min-width:71.25em){.docs-home-match__wrapper .background .image:before{opacity:.6;width:680px}}@media all and (min-width:81.25em){.docs-home-match__wrapper .background .image:before{width:820px}}.docs-home-match__wrapper .background .image img,.docs-home-match__wrapper .background .image video{height:100%;width:auto;position:absolute;top:0;left:0;bottom:0;-webkit-transform:translateX(0);transform:translateX(0)}@media all and (min-width:20em){.docs-home-match__wrapper .background .image img,.docs-home-match__wrapper .background .image video{-webkit-transform:translateX(-34%);transform:translateX(-34%)}.docs-home-match__wrapper .foreground .strapline br{display:none}}@media all and (min-width:25em){.docs-home-match__wrapper .background .image img,.docs-home-match__wrapper .background .image video{-webkit-transform:translateX(-22%);transform:translateX(-22%)}}@media all and (min-width:30em){.docs-home-match__wrapper .background .image img,.docs-home-match__wrapper .background .image video{-webkit-transform:translateX(-25%);transform:translateX(-25%)}}@media all and (min-width:36.25em){.docs-home-match__wrapper .background .image img,.docs-home-match__wrapper .background .image video{-webkit-transform:translateX(-27%);transform:translateX(-27%)}}@media all and (min-width:41.25em){.docs-home-match__wrapper .background .image img,.docs-home-match__wrapper .background .image video{-webkit-transform:translateX(-18%);transform:translateX(-18%)}}@media all and (min-width:61.25em){.docs-home-match__wrapper .background .image img,.docs-home-match__wrapper .background .image video{-webkit-transform:translateX(0);transform:translateX(0)}}@media all and (min-width:71.25em){.docs-home-match__wrapper .background .image img,.docs-home-match__wrapper .background .image video{-webkit-transform:translateX(0);transform:translateX(0)}}@media all and (min-width:81.25em){.docs-home-match__wrapper .background .image img,.docs-home-match__wrapper .background .image video{-webkit-transform:translateX(0);transform:translateX(0);width:100%;height:auto}}.docs-home-match__wrapper .background .image img{z-index:11}.docs-home-match__wrapper .background .image video{z-index:12}.docs-home-match__wrapper .background .docs-logo{position:absolute;top:5px;left:9px;z-index:15}.docs-home-match__wrapper .background .docs-logo svg{width:140px;height:79px}@media all and (min-width:61.25em){.docs-home-match__wrapper .background .docs-logo{-webkit-transform-origin:top left;transform-origin:top left;-webkit-transform:scale(1.15);transform:scale(1.15)}}.docs-home-match__wrapper .foreground{position:relative;z-index:10;padding:7px 10px 18px;text-shadow:0 0 30px rgba(0,0,0,.2);-webkit-transform-style:preserve-3d;transform-style:preserve-3d;-webkit-perspective:1000;perspective:1000}@media all and (min-width:46.25em){.docs-home-match__wrapper .background .docs-logo{left:19px}.docs-home-match__wrapper .foreground{padding:7px 20px 18px}}@media all and (min-width:71.25em){.docs-home-match__wrapper .foreground{padding-left:180px}}.docs-home-match__wrapper .foreground .title{color:#ecbfb0;margin-top:6px;padding-bottom:0;-webkit-animation-name:fade;animation-name:fade;-webkit-animation-duration:.3s;animation-duration:.3s;-webkit-animation-delay:.5s;animation-delay:.5s;-webkit-animation-timing-function:cubic-bezier(.71,.55,.62,1.57);animation-timing-function:cubic-bezier(.71,.55,.62,1.57);-webkit-animation-fill-mode:both;animation-fill-mode:both}.docs-home-match__wrapper .foreground .title .spanstyle{color:#d0d3d4}.docs-home-match__wrapper .foreground .strapline{-webkit-animation-name:fade;animation-name:fade;-webkit-animation-duration:1s;animation-duration:1s;-webkit-animation-delay:1s;animation-delay:1s;-webkit-animation-timing-function:cubic-bezier(.71,.55,.62,1.57);animation-timing-function:cubic-bezier(.71,.55,.62,1.57);-webkit-animation-fill-mode:both;animation-fill-mode:both;font-weight:200;max-width:80%}.docs-home-match__wrapper .foreground .play,.docs-home-match__wrapper .foreground .strapline{color:#FFF}.docs-home-match__wrapper .foreground .strapline br{display:none}@media all and (min-width:41.25em){.docs-home-match__wrapper .foreground{position:absolute;bottom:0;left:0;right:0}.docs-home-match__wrapper .foreground .strapline{margin-top:-3px;margin-bottom:-7px}.docs-home-match__wrapper .foreground .strapline br{display:block}}@media all and (min-width:61.25em){.docs-home-match__wrapper .foreground .strapline{margin-top:-3px;margin-bottom:-10px}.docs-home-match__wrapper .foreground .strapline br{display:none}}@media all and (min-width:81.25em){.docs-home-match__wrapper .foreground{padding-left:260px}.docs-home-match__wrapper .foreground .strapline br{display:block}}.docs-home-match__wrapper .foreground .play{font-family:"Guardian Text Sans Web","Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;font-size:16px;margin-top:16px;margin-left:-2px;position:relative}.docs-home-match__wrapper .foreground .play:before{content:'';width:42px;height:42px;border-radius:100%;background-color:#FB0;display:inline-block;margin-right:3px;vertical-align:middle;position:relative;bottom:2px}.docs-home-match__wrapper .foreground .play svg{position:absolute;width:23px;height:19px;top:10px;left:12px}.docs-home-match__wrapper .full-link{display:block;position:absolute;top:0;left:0;right:0;bottom:0;z-index:15!important;color:transparent}.docs-home-match__wrapper .full-link:hover~.background,.docs-home-match__wrapper .full-link:hover~.foreground div{opacity:.9}@keyframes fade{from{opacity:0}to{opacity:1}}@-webkit-keyframes fade{from{opacity:0}to{opacity:1}}</style>
<a href="https://www.theguardian.com/world/ng-interactive/2017/oct/06/home-match-a-young-ukrainian-woman-torn-between-football-and-family" data-link-name="docs : video thrasher : dearborn michigan" class="full-link">Home match<br>One crucial year in the life of a footballer and caregiver</a>
<div class="background">
<div class="image">
<img src="https://interactive.guim.co.uk/thrashers/docs-home-match/hashed/bg.c5b1aaf0.jpg" data-wants-docs-home-match="https://interactive.guim.co.uk/thrashers/docs-home-match/hashed/170822HomeGamesThrasher_23.74628f8a.mp4">
</div>
<div class="docs-logo">
<svg viewbox="11 6 141 79">
<g opacity=".9" fill="#F6F6F6" fill-rule="evenodd">
<path opacity=".8" d="M93.84 21.63l-34.3 14.1-1.27-1L58.3 6.9l1.3-.9 34.26 14.1"/>
<path d="M33.78 17.5l-1.38.97-.02 13.75c6.54 1.2 11.68 6.36 12.8 12.9l25.85-10.6v-1.68L33.78 17.5zm67.62 53.6L67.7 84.9l-1.23-.97.05-27.35 1.24-.86 33.63 13.84m-57-16.2c-2.3 6-8.1 10.3-14.9 10.3-1.2 0-2.3-.13-3.4-.36l-.1 7.8 1.1.86L56.8 59.8v-1.33l-12.4-5.12z" opacity=".8"/>
<path opacity=".8" d="M99.62 50h-2.58l-.56.37-.05 33.37 1.5 1.18 41.1-16.88V66.2M83.58 43.1c.8 0 1.3.26 1.54.87h.07c.6-.56 1.2-.88 2.1-.88.4 0 .8.1 1.1.3l34.3-14.1v-1.8L84.2 11.7l-1.42 1-.05 30.5c.25-.07.52-.1.83-.1"/>
<path d="M89.8 50h-3.54v-.62l.6-.34v-3.66c0-.7-.24-.95-.84-.95-.23 0-.5.06-.75.17v4.44l.6.34v.6h-3.43v-.6l.6-.34v-3.66c0-.7-.23-.95-.84-.95-.24 0-.5.06-.75.2v4.4l.6.35v.6h-3.58v-.6l.74-.34v-4.57l-.7-.35v-.6l2.8-.43h.2v.8h.1c.6-.6 1.2-.9 2.1-.9.8 0 1.3.2 1.6.8h.1c.6-.6 1.3-.9 2.2-.9 1.2 0 1.7.5 1.7 1.8V49l.8.35v.6zm-11.52-.16l-2.74.3h-.18v-.9h-.08c-.44.54-1.15.93-2.05.93-1.36 0-1.94-.97-1.94-2.14V44.5l-.8-.34v-.62l2.8-.44h.2v4.75c0 .77.3.9.9.9.3 0 .6-.06.8-.15v-4.1l-.8-.34v-.62l2.8-.44h.2v5.76l.7.4v.58zm-8.06-.64c-.36.43-1.3.96-2.4.96-2.3 0-3.47-1.4-3.47-3.54 0-2.2 1.44-3.53 3.67-3.53.8 0 1.76.1 2.15.2v2H69l-.4-1.3c-.1-.1-.34-.1-.64-.1-.74 0-1.3.7-1.3 2.5 0 1.6.82 2.2 1.92 2.2.62 0 1.3-.1 1.64-.2v.6zm-9.7.97c-2.04 0-3.45-1.26-3.45-3.55 0-2.28 1.4-3.53 3.46-3.53 2.05 0 3.46 1.2 3.46 3.5s-1.5 3.5-3.5 3.5zm29.2-3.56c0-2.2 1.3-3.5 3.32-3.5 2.03 0 3 .9 3 3.8h-4.02c.1 1.1.5 1.7 1.32 1.9l3.7-1.5v-2.7l-.78-.3v-.6l2.8-.4h.18v.8h.07c.6-.5 1.5-.9 2.4-.9.5 0 .8.1 1.1.3v-.7L53.6 22.5l-1.8 1.25V43.3c.38-.1.7-.16 1.1-.16.4 0 .8.1 1.1.3v-1.7l-.72-.4v-.6l2.8-.5h.2v8.5l.7.4v.58l-2.6.3h-.2v-.7H54c-.3.38-.87.75-1.7.75-.18 0-.36 0-.54-.02l-.03 13.5 1.8 1.43L91.1 49.6c-.9-.6-1.35-1.6-1.35-3.03z" opacity=".8"/>
<path d="M100.2 44.43c-.35 0-.65.08-.93.18v1.7l1.82-.7v-.1c0-.7-.3-.9-.9-.9M60.5 44c-.75 0-1.12.4-1.12 2.62 0 2.23.38 2.6 1.13 2.6.8 0 1.1-.37 1.1-2.6 0-2.22-.3-2.6-1.1-2.6m-7.3 4.94c.4 0 .6-.06.7-.12v-4.56c-.1-.13-.3-.24-.7-.24-.7 0-1.2.64-1.2 2.54 0 1.66.5 2.38 1.3 2.38M93 43.83c-.6 0-.98.4-1 2.2l1.86-.12c0-1.7-.3-2-.85-2m18.2 4.1c0 .8.4 1 .9 1 .3 0 .5-.1.6-.2v-1.9l-.5.1c-.5.1-.9.4-.9 1.1" opacity=".8"/>
<path d="M133.48 50.16c-.73 0-1.7-.14-2.35-.42v-1.78h.95l.38 1.12c.16.14.7.2 1.1.2.63 0 1.07-.13 1.07-.66 0-.5-.17-.7-.9-.85l-.8-.18c-1.25-.3-1.83-1.3-1.83-2.3 0-1.3.88-2.3 2.87-2.3.8 0 1.6.1 2.13.3V45h-.94l-.3-.92c-.14-.08-.6-.17-.97-.17-.6 0-.9.3-.9.7 0 .4.1.7.9.8l.8.2c1.3.3 1.8 1.2 1.8 2.2 0 1.4-.9 2.4-3.1 2.4zm-4.74-1.4c.86 0 1.34-.08 1.8-.22v.65c-.3.4-1.32.9-2.56.9-2.3 0-3.5-1.3-3.5-3.6 0-2.2 1.3-3.5 3.32-3.5 2.02 0 3 .9 3 3.7h-4.02c.1 1.3.73 1.9 1.96 1.9zM124.58 50h-3.7v-.63l.74-.34v-4.56l-.76-.35v-.6l2.82-.46h.18v5.97l.72.34V50zm-3.82-4.9c-.13-.03-.37-.05-.57-.05-.6 0-1.1.06-1.5.24V49l.9.34V50h-3.9v-.63l.7-.34v-4.56l-.8-.35v-.6l2.7-.46h.2v1.42h.1c.4-.9 1-1.37 1.7-1.37.1 0 .3.1.3.1v2zm-5.14 4.78c-.22.12-.73.28-1.27.28-.7 0-1.33-.23-1.43-.95h-.06c-.3.6-1.1 1-1.94 1-1.2 0-1.94-.7-1.94-1.9 0-1.3.9-1.6 2.38-1.9l1.3-.2v-.9c0-.8-.26-1.3-1.13-1.3h-.58l-.47 1.4h-1.05v-1.8c.64-.2 1.4-.5 2.58-.5 1.9 0 2.9.6 2.9 2.1v3.9l.8.4v.5zm7.08-9.58c.65 0 1.2.53 1.2 1.2 0 .64-.55 1.17-1.2 1.17-.66 0-1.2-.53-1.2-1.18 0-.7.54-1.2 1.2-1.2zm-16.94-13.08l-1.7 1.18-.03 15 .97-.14V42l2.24-.32v1.58h1.47v1.15h-1.4V48c0 .66.2 1 .9 1 .3 0 .6-.03.7-.05v.88c-.3.2-1.1.4-1.8.4-1.3 0-1.9-.6-1.9-2.02v-3.8h-.9v5l.1.1v.6h-.02l-.1 16 1.7 1.4 46.25-19v-2.1l-46.2-19z" opacity=".8"/>
<path d="M127.76 43.83c-.6 0-.98.4-1 2.2l1.86-.12c0-1.7-.3-2-.86-2M93 43.9c-.6 0-.98.4-1 2.2l1.86-.14c0-1.77-.3-2.06-.85-2.06m14.3-.9v.3h.8m3.2 4.7c0 .75.4 1 .9 1 .3 0 .5-.13.6-.27V46.9l-.5.04c-.5.06-.9.4-.9 1.05" opacity=".8"/>
<path d="M104.07 50h-3.7v-.62l.72-.34v-3.66c0-.7-.3-.95-.9-.95-.4 0-.7.08-1 .2v4.4l.7.35v.6h-3.6v-.6l.7-.34v-4.57l-.8-.35v-.6l2.8-.43h.2v.8c.6-.6 1.5-.9 2.4-.9 1.1 0 1.7.5 1.7 1.8V49l.7.35v.6zm-10.1-1.23c.87 0 1.35-.1 1.82-.23v.65c-.4.4-1.4.9-2.6.9-2.3 0-3.5-1.3-3.5-3.6 0-2.2 1.3-3.5 3.3-3.5 2 0 3 .9 3 3.7h-4c.1 1.3.7 1.9 1.9 1.9zM89.82 50h-3.54v-.62l.6-.34v-3.66c0-.7-.24-.95-.84-.95-.23 0-.5.06-.75.17v4.44l.6.34v.6h-3.5v-.6l.6-.34v-3.66c0-.7-.3-.95-.9-.95-.3 0-.5.06-.8.2v4.4l.6.35v.6h-3.5v-.6l.7-.34v-4.57l-.8-.35v-.6l2.8-.43h.1v.8h.1c.6-.6 1.2-.9 2.1-.9.8 0 1.3.2 1.5.8h.1c.6-.6 1.24-.9 2.2-.9 1.1 0 1.7.5 1.7 1.8V49l.7.35v.6zm28.9-.97l.93.34V50h-3.88v-.63l.7-.34v-2.3l-1.55-.63v2.94l.72.34v.5c-.22.12-.73.28-1.27.28-.7 0-1.33-.23-1.43-.95h-.06c-.3.6-1.1 1-1.94 1-1.2 0-1.94-.7-1.94-1.9 0-1.3.9-1.6 2.38-1.9l1.3-.2v-1l-1.85-.7-.32 1h-1V44l-.7-.3v.83h-1.4V48c0 .65.2 1 .9 1 .3 0 .6-.04.8-.06v.88c-.4.2-1.1.4-1.8.4-1.3 0-1.92-.6-1.92-2.03v-3.8H104v-1l1.03-.2V42L79.46 31.5l-1.52 1.05-.02 16.5.4.2v.58l-.4.04-.02 16.18 1.5 1.18 41.26-16.94v-1.9l-1.92-.8V49zM69 45.38l-.1-.33-1.73-.7c-.32.37-.52 1.06-.52 2.15 0 1.6.83 2.27 1.93 2.27.63 0 1.3-.1 1.64-.2v.27l.83-.35v-2.6l-1.34-.6H69zm-8.47 4.8c-2.05 0-3.46-1.27-3.46-3.56 0-2.28 1.4-3.53 3.46-3.53 2.05 0 3.46 1.2 3.46 3.5s-1.5 3.5-3.5 3.5zm-3.64-.34l-2.7.3H54v-.7h-.06c-.28.36-.86.73-1.7.73-1.23 0-2.7-.78-2.7-3.37 0-2.7 1.5-3.7 3.3-3.7.36 0 .8.1 1.08.3v-1.66l-.75-.34v-.6l2.8-.46h.18v8.52l.7.4v.58zm-16.3 9.23c.5-1.1.8-2.37.8-3.78 0-4.3-2.4-6.3-7.2-6.3h-7.7c-.9 0-1.6-.6-1.6-1.4 0-.6.4-1.2.9-1.6 1.2.3 2.2.4 3.6.4 5.6 0 9.4-2.5 9.4-7.2v-.6c-.1-2.5-1.2-4.3-3.1-5.6 5.6 2.4 9.6 8 9.6 14.5 0 4.4-1.9 8.4-4.8 11.3zm-11 2.05c-4.1 0-5.6-1.44-5.6-3 0-1.1.6-2.55 2.6-2.55h5.8c1.9 0 3 1.04 3 2.53 0 1.7-1.3 3.02-6 3.02zm-6.2-6.83c-2.5.5-5.2 1.5-5.2 4.3v.2c-2.8-2.9-4.6-6.8-4.6-11.1 0-6.4 3.8-11.9 9.2-14.4-1.9 1.3-2.9 3.2-2.9 5.6 0 2.8 1.4 4.9 3.6 6.1l.1.1c-1.3.8-3.8 2.8-3.8 5.1 0 1.7 1.1 3.3 3.4 3.8zm6-20.2c1.6 0 2.9.6 2.9 5 0 4.3-1.4 4.7-2.9 4.7-1.6 0-2.9-.4-2.9-4.8s1.3-5 2.8-5zm34.8 12.5c0-1.3.5-2.3 1.3-2.9L14 22.4 11.9 24v46.3l2.1 1.44 53-21.7c-1.8-.28-2.75-1.6-2.75-3.5z" opacity=".8"/>
<path d="M51.94 46.58c0 1.66.42 2.38 1.3 2.38.35 0 .54-.06.7-.12v-4.56c-.17-.13-.37-.24-.76-.24-.7 0-1.24.64-1.24 2.54m8.6-2.58c-.75 0-1.12.4-1.12 2.62 0 2.23.37 2.6 1.12 2.6.75 0 1.1-.37 1.1-2.6 0-2.22-.35-2.6-1.1-2.6" opacity=".8"/>
<path d="M60.54 49.23c.7 0 1.06-.35 1.1-2.3l-2.2-.92c-.02.2-.02.4-.02.7 0 2.3.37 2.6 1.12 2.6m-8.6-2.6c0 1.7.42 2.4 1.3 2.4.35 0 .54 0 .7-.1v-4.6c-.17-.1-.37-.2-.76-.2-.7 0-1.24.7-1.24 2.6" opacity=".8"/>
<path d="M67.82 50.16c-1.7 0-2.77-.77-3.23-2.03l-.8-.3c-.4 1.52-1.7 2.34-3.3 2.34-2.1 0-3.5-1.26-3.5-3.55 0-.55.1-1.05.2-1.48l-1.2-.47v4.2l.7.4v.57l-2.7.3v-.7h-.1c-.3.36-.9.73-1.7.73-1.3 0-2.7-.78-2.7-3.37 0-2.5 1.3-3.52 2.8-3.67l-6.8-2.8-1.6 1.1c.9 1.96 1.33 4.1 1.33 6.38 0 2.3-.5 4.5-1.38 6.5v22.4l1.6 1.3 43.3-17.8v-2L69 50c-.34.1-.75.2-1.18.2" opacity=".8"/>
</g>
</svg>
</div>
</div>
<div class="foreground">
<!-- <div class='title'><span class="spanstyle">Home</span> Match</div> -->
<div class="title">
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="206.358px" height="42.159px" viewbox="0 0 206.358 42.159" enable-background="new 0 0 206.358 42.159" xml:space="preserve">
<g>
<path fill="#FECE4D" d="M19.8,34h-3.48V20.68H5.68V34H2.24V6h3.44v11.88h10.64V6h3.48V34z"/>
<path fill="#FECE4D" d="M42.2,29.479L37.64,34h-9.2l-4.52-4.52v-19.16L28.24,6h9.64l4.32,4.32V29.479z M29.64,9.439l-2.28,2.28
		v16.4l2.4,2.44h6.56l2.4-2.44v-16.4l-2.28-2.28H29.64z"/>
<path fill="#FECE4D" d="M66.439,34h-3.32v-23.08l-5.84,10.6h-1.8l-5.84-10.6V34h-3.32V6h4.16l6.04,11.08L62.56,6h3.88V34z"/>
<path fill="#FECE4D" d="M87.679,9.439h-13.28v8.32h9.56v3.04h-9.56v9.76h13.36V34h-16.84V6h16.76V9.439z"/>
<path fill="#FECE4D" d="M123.559,34h-3.32v-23.08l-5.84,10.6h-1.8l-5.84-10.6V34h-3.32V6h4.16l6.04,11.08L119.679,6h3.88V34z"/>
<path fill="#FECE4D" d="M145.678,34h-3.6l-1.84-7.04h-8.72l-1.8,7.04h-3.2l7.48-28h4.4L145.678,34z M132.198,24.399h7.36
		l-3.72-14.12L132.198,24.399z"/>
<path fill="#FECE4D" d="M163.358,9.279h-7.76V34h-3.48V9.279h-7.76V6h19V9.279z"/>
<path fill="#FECE4D" d="M182.438,9.959v5.4h-3.44v-3.88l-2-2h-6.48l-2.52,2.56v15.84l2.68,2.68h6.16l2.16-2.12V24h3.44v5.84
		l-4.16,4.16h-8.84l-4.92-4.88V10.68l4.68-4.68h9.32L182.438,9.959z"/>
<path fill="#FECE4D" d="M204.118,34h-3.479V20.68h-10.641V34h-3.44V6h3.44v11.88h10.641V6h3.479V34z"/>
</g>
</svg>
</div>
<div class="strapline">
<span>One crucial year in the life of <br>a footballer and caregiver</span>
</div>
<div class="play">
<svg viewbox="13 13 26 21">
<path fill="#333" fill-rule="evenodd" d="M38.5 24.08V23L14.4 13l-.9.7v19.68l.9.62"/>
</svg> Watch now
</div>
</div>
<img style="height:0;width:0;visibility:hidden;position:absolute;z-index: 1;" height="0" width="0" src="https://interactive.guim.co.uk/thrashers/docs-home-match/hashed/empty.db892fb1.gif" onload="var script=document.createElement('script');script.src='https://interactive.guim.co.uk/thrashers/docs-home-match/hashed/wantsVideo.5a052959.js'; document.body.appendChild(script);">
</div>
</div> </li>
</ul>
</div>
</div>
</div>
</section>
<div class="fc-container fc-container--commercial">
<div id="dfp-ad--merchandising-high" class="js-ad-slot ad-slot ad-slot--merchandising-high ad-slot--commercial-component-high " data-link-name="ad slot merchandising-high" data-name="merchandising-high" data-label="false" data-refresh="false" data-mobile="1,1|2,2|88,87|fluid">
</div>
</div>
<section id="opinion" class="fc-container fc-container--will-have-toggle js-container--toggle " data-link-name="container-5 | opinion" data-id="ee3386bb-9430-4a6d-8bca-b99d65790f3b" data-component="opinion" aria-expanded="true">
<div class="fc-container__inner">
<div class="fc-container__header
                js-container__header
                ">
<div class="fc-container__header__title">
<span tabindex="0">opinion</span>
</div>
</div>
<div class="fc-container--rolled-up-hide fc-container__body" data-title="opinion" data-id="ee3386bb-9430-4a6d-8bca-b99d65790f3b">
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-4 fc-slice fc-slice--q-q-hl3">
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-cutout fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-comment--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-discussion-id="/p/7cept" data-discussion-closed="true" data-discussion-url="https://www.theguardian.com/commentisfree/2017/oct/12/britain-donald-trump-hatred-theresa-may-state-visit-protests#comments" data-link-name="comment | group-0 | card-1" data-item-visibility="all" data-test-id="facia-card" data-id="commentisfree/2017/oct/12/britain-donald-trump-hatred-theresa-may-state-visit-protests" data-loyalty-short-url="/p/7cept">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/commentisfree/2017/oct/12/britain-donald-trump-hatred-theresa-may-state-visit-protests" class="fc-item__link" data-link-name="article"> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">Britain will greet Trump with our biggest ever carnival against hatred</span></span> </a></h2>
<div class="fc-item__byline">
Owen Jones
</div>
</div>
<div class="fc-item__standfirst">
Trump’s people and Theresa May’s people clearly think that downgrading his state visit will subdue our protests. Quite the opposite, writes Guardian columnist Owen Jones
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<div class="fc-item__avatar">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="216px" srcset="https://i.guim.co.uk/img/uploads/2017/10/09/Owen-Jones,-L.png?w=216&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=1.3&amp;s=ab0a9e214ea20657aad18226514110d0 432w">
<source media="(min-width: 980px)" sizes="216px" srcset="https://i.guim.co.uk/img/uploads/2017/10/09/Owen-Jones,-L.png?w=216&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=2892bc2c30270f979899b46bfaf4a41f 216w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="216px" srcset="https://i.guim.co.uk/img/uploads/2017/10/09/Owen-Jones,-L.png?w=216&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=1.3&amp;s=ab0a9e214ea20657aad18226514110d0 432w">
<source media="(min-width: 740px)" sizes="216px" srcset="https://i.guim.co.uk/img/uploads/2017/10/09/Owen-Jones,-L.png?w=216&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=2892bc2c30270f979899b46bfaf4a41f 216w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="115px" srcset="https://i.guim.co.uk/img/uploads/2017/10/09/Owen-Jones,-L.png?w=115&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=1.3&amp;s=721afee4bbdc329cf30c599fab4de76f 230w">
<source media="(min-width: 0px)" sizes="115px" srcset="https://i.guim.co.uk/img/uploads/2017/10/09/Owen-Jones,-L.png?w=115&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=d72de21c32442e7ad718492382607e8d 115w">
<!--[if IE 9]></video><![endif]-->
<img class="fc-item__avatar__media image--landscape" alt="">
</picture>
</div>
<a href="https://www.theguardian.com/commentisfree/2017/oct/12/britain-donald-trump-hatred-theresa-may-state-visit-protests" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Britain will greet Trump with our biggest ever carnival against hatred</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-comment--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-discussion-id="/p/7cf6b" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/politics/2017/oct/12/barniers-body-language-reveals-futility-and-deadlock-at-brexit-talks#comments" data-link-name="comment | group-0 | card-2" data-item-visibility="all" data-test-id="facia-card" data-id="politics/2017/oct/12/barniers-body-language-reveals-futility-and-deadlock-at-brexit-talks" data-loyalty-short-url="/p/7cf6b">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/1bbe09d81d9af51553d7e1e702f13ff977ad572e/0_375_3840_2303/master/3840.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=803fd59bd59658d190040891bd775e4a 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/1bbe09d81d9af51553d7e1e702f13ff977ad572e/0_375_3840_2303/master/3840.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=6d8e5a2ce6fa8815c496030c6b903ec5 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/1bbe09d81d9af51553d7e1e702f13ff977ad572e/0_375_3840_2303/master/3840.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=74bbd03588dca8b46c96ca84529f3c77 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/1bbe09d81d9af51553d7e1e702f13ff977ad572e/0_375_3840_2303/master/3840.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=97e0a030089096a6851739a57f1ae6f1 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/1bbe09d81d9af51553d7e1e702f13ff977ad572e/0_375_3840_2303/master/3840.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=4593c53720da211cbe660a8745cdcddd 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/1bbe09d81d9af51553d7e1e702f13ff977ad572e/0_375_3840_2303/master/3840.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=342b18d470939faf43251ddd59adb2af 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/politics/2017/oct/12/barniers-body-language-reveals-futility-and-deadlock-at-brexit-talks" class="fc-item__link" data-link-name="article"> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">Barnier's body language reveals futility and deadlock at Brexit talks</span></span> </a></h2>
<div class="fc-item__byline">
John Crace
</div>
</div>
<div class="fc-item__standfirst">
The EU’s chief negotiator and David Davis avoided all eye contact as they reiterated the progress they had failed to make
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/politics/2017/oct/12/barniers-body-language-reveals-futility-and-deadlock-at-brexit-talks" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Barnier's body language reveals futility and deadlock at Brexit talks</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-2">
<ul class="u-unstyled l-list l-list--columns-1 l-list--rows-3">
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-comment--item fc-item--list-mobile fc-item--list-media-tablet js-snappable" data-discussion-id="/p/7c6eh" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/commentisfree/2017/oct/12/espn-jemele-hill-angry-black-woman-suspension-nfl#comments" data-link-name="comment | group-0 | card-3" data-item-visibility="all" data-test-id="facia-card" data-id="commentisfree/2017/oct/12/espn-jemele-hill-angry-black-woman-suspension-nfl" data-loyalty-short-url="/p/7c6eh">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/4a0e5f4b765d7837b052fc7d11f3d72ac0075180/127_135_1769_1061/master/1769.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=84a68e4768781df91bb48afdd6560ca7 280w">
<source media="(min-width: 980px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/4a0e5f4b765d7837b052fc7d11f3d72ac0075180/127_135_1769_1061/master/1769.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e7b9319063dcb42efbddb96d5562b03f 140w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/4a0e5f4b765d7837b052fc7d11f3d72ac0075180/127_135_1769_1061/master/1769.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=84a68e4768781df91bb48afdd6560ca7 280w">
<source media="(min-width: 740px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/4a0e5f4b765d7837b052fc7d11f3d72ac0075180/127_135_1769_1061/master/1769.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e7b9319063dcb42efbddb96d5562b03f 140w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/commentisfree/2017/oct/12/espn-jemele-hill-angry-black-woman-suspension-nfl" class="fc-item__link" data-link-name="article"> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">ESPN's Jemele Hill is being reduced to an 'angry black woman'</span></span> </a></h2>
<div class="fc-item__byline">
Ameer Hasan Loggins
</div>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/commentisfree/2017/oct/12/espn-jemele-hill-angry-black-woman-suspension-nfl" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">ESPN's Jemele Hill is being reduced to an 'angry black woman'</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-comment--item fc-item--list-mobile fc-item--list-media-tablet js-snappable" data-discussion-id="/p/7cetm" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/commentisfree/2017/oct/12/what-to-say-somebody-miscarried-loss-baby#comments" data-link-name="comment | group-0 | card-4" data-item-visibility="all" data-test-id="facia-card" data-id="commentisfree/2017/oct/12/what-to-say-somebody-miscarried-loss-baby" data-loyalty-short-url="/p/7cetm">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/2c6a690d9025165c6fb72013c32caf01b6ee5c1e/486_900_3284_1971/master/3284.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=ab84e452770086381bac3020b0e33bfb 280w">
<source media="(min-width: 980px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/2c6a690d9025165c6fb72013c32caf01b6ee5c1e/486_900_3284_1971/master/3284.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=8c394aa8d92501155749bffc65fccf48 140w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/2c6a690d9025165c6fb72013c32caf01b6ee5c1e/486_900_3284_1971/master/3284.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=ab84e452770086381bac3020b0e33bfb 280w">
<source media="(min-width: 740px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/2c6a690d9025165c6fb72013c32caf01b6ee5c1e/486_900_3284_1971/master/3284.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=8c394aa8d92501155749bffc65fccf48 140w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/commentisfree/2017/oct/12/what-to-say-somebody-miscarried-loss-baby" class="fc-item__link" data-link-name="article"> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">What you should say to somebody who has miscarried – and what you shouldn’t</span></span> </a></h2>
<div class="fc-item__byline">
Janet Murray
</div>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/commentisfree/2017/oct/12/what-to-say-somebody-miscarried-loss-baby" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">What you should say to somebody who has miscarried – and what you shouldn’t</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-comment--item fc-item--list-mobile fc-item--list-media-tablet js-snappable" data-discussion-id="/p/7cfvp" data-discussion-closed="true" data-discussion-url="https://www.theguardian.com/commentisfree/2017/oct/12/torture-survivors-uk-detention-centres-home-office-high-court-ruling#comments" data-link-name="comment | group-0 | card-5" data-item-visibility="all" data-test-id="facia-card" data-id="commentisfree/2017/oct/12/torture-survivors-uk-detention-centres-home-office-high-court-ruling" data-loyalty-short-url="/p/7cfvp">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/8a826fd6a936690b04f0e6540b44d314d364a400/0_92_3000_1800/master/3000.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=4a1cd2ba1f9a226502855c0b96693e14 280w">
<source media="(min-width: 980px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/8a826fd6a936690b04f0e6540b44d314d364a400/0_92_3000_1800/master/3000.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=fd3e6c800a02e2559b5e0f3b855dd3ee 140w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/8a826fd6a936690b04f0e6540b44d314d364a400/0_92_3000_1800/master/3000.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=4a1cd2ba1f9a226502855c0b96693e14 280w">
<source media="(min-width: 740px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/8a826fd6a936690b04f0e6540b44d314d364a400/0_92_3000_1800/master/3000.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=fd3e6c800a02e2559b5e0f3b855dd3ee 140w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/commentisfree/2017/oct/12/torture-survivors-uk-detention-centres-home-office-high-court-ruling" class="fc-item__link" data-link-name="article"> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">I sought refuge from torture in the UK. Only to be locked up again</span></span> </a></h2>
<div class="fc-item__byline">
Serge Eric
</div>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/commentisfree/2017/oct/12/torture-survivors-uk-detention-centres-home-office-high-court-ruling" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">I sought refuge from torture in the UK. Only to be locked up again</a>
</div>
</div> </li>
</ul> </li>
</ul>
</div>
</div>
</div>
</section>
<section id="around-the-world" class="fc-container fc-container--has-show-more fc-container--will-have-toggle js-container--toggle " data-link-name="container-6 | around-the-world" data-id="f6f08c9d-b14b-44f8-bba0-c82475c9ecb2" data-component="around-the-world" aria-expanded="true">
<div class="fc-container__inner">
<div class="fc-container__header
                js-container__header
                ">
<div class="fc-container__header__title">
<a data-link-name="section heading" href="https://www.theguardian.com/world"> <span class="fc-container__title__text">around the world</span> </a>
</div>
</div>
<ul class="treats__container">
<li class="treats__list-item"> <a href="/global-development" data-link-name="treat | 1 | Global development" class="treats__treat">Global development</a> </li>
<li class="treats__list-item"> <a href="/world/series/guardian-world-networks" data-link-name="treat | 2 | World networks" class="treats__treat">World networks</a> </li>
<li class="treats__list-item"> <a href="/cities" data-link-name="treat | 3 | Cities" class="treats__treat">Cities</a> </li>
</ul>
<div class="fc-container--rolled-up-hide fc-container__body fc-show-more--hidden js-container--fc-show-more" data-title="around the world" data-id="f6f08c9d-b14b-44f8-bba0-c82475c9ecb2">
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-4 fc-slice fc-slice--q-q-ql-ql">
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-news--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-discussion-id="/p/7cepa" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/world/2017/oct/12/trump-warns-its-possible-the-us-will-drop-out-of-nafta#comments" data-link-name="news | group-0 | card-1" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/trump-warns-its-possible-the-us-will-drop-out-of-nafta" data-loyalty-short-url="/p/7cepa">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/7ed60e65d151bfed856b72cdad2c7ebb6c92d40b/0_48_2200_1320/master/2200.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=5e3aee3c034f219a5e21af2d457fad84 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/7ed60e65d151bfed856b72cdad2c7ebb6c92d40b/0_48_2200_1320/master/2200.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=3a3ccaba2926e167befcff0e453400f6 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/7ed60e65d151bfed856b72cdad2c7ebb6c92d40b/0_48_2200_1320/master/2200.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=337ad7cd09899ca843714479120a7b46 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/7ed60e65d151bfed856b72cdad2c7ebb6c92d40b/0_48_2200_1320/master/2200.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=65984ffc68e7cf1f235c34d7f93ba600 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/7ed60e65d151bfed856b72cdad2c7ebb6c92d40b/0_48_2200_1320/master/2200.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=5335476ba6d4d6deb3a308b770bf7691 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/7ed60e65d151bfed856b72cdad2c7ebb6c92d40b/0_48_2200_1320/master/2200.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=199729bdf4f57257914b55d8185e3179 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/trump-warns-its-possible-the-us-will-drop-out-of-nafta" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Nafta</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Trump warns it's 'possible' the US will drop out</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
23-year-old North American Free Trade Agreement in peril as Trump meets with Justin Trudeau: ‘If we can’t make a deal, it’ll be terminated and that will be fine’
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/trump-warns-its-possible-the-us-will-drop-out-of-nafta" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Trump warns it's 'possible' the US will drop out</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="news | group-0 | card-2" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/kenya-bans-opposition-protests-as-election-crisis-deepens" data-loyalty-short-url="/p/7ceey">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/968620305301f150a63c5e3d1561a380ae4c7bd0/0_62_6000_3600/master/6000.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=63905a1d4c4ef8528e89ee9ddfa49e34 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/968620305301f150a63c5e3d1561a380ae4c7bd0/0_62_6000_3600/master/6000.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e778421e57435c845c134404bbac1433 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/968620305301f150a63c5e3d1561a380ae4c7bd0/0_62_6000_3600/master/6000.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=7f651d5b40cc1dfc83d9068fcf8032be 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/968620305301f150a63c5e3d1561a380ae4c7bd0/0_62_6000_3600/master/6000.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=0fb11b105bbadf81530ca4a1e6dad620 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/968620305301f150a63c5e3d1561a380ae4c7bd0/0_62_6000_3600/master/6000.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=f9add95aca416ec093fc0f8c0c3d1fb1 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/968620305301f150a63c5e3d1561a380ae4c7bd0/0_62_6000_3600/master/6000.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=49506431c15b438be35a1adbfd8ae6ff 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/kenya-bans-opposition-protests-as-election-crisis-deepens" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Kenya</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Opposition protests banned as election crisis deepens</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
Demonstrations banned in Nairobi, Mombasa and Kisumu centres due to lawlessness during rallies before poll rerun
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/kenya-bans-opposition-protests-as-election-crisis-deepens" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Opposition protests banned as election crisis deepens</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-2">
<ul class="u-unstyled l-list l-list--columns-2 l-list--rows-3">
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--list-mobile fc-item--list-tablet js-snappable" data-link-name="news | group-0 | card-3" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/south-africa-judge-rules-police-murdered-anti-apartheid-activist-in-1971" data-loyalty-short-url="/p/7ceex">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/south-africa-judge-rules-police-murdered-anti-apartheid-activist-in-1971" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">South Africa</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Judge rules police murdered anti-apartheid activist in 1971</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/south-africa-judge-rules-police-murdered-anti-apartheid-activist-in-1971" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Judge rules police murdered anti-apartheid activist in 1971</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--list-mobile fc-item--list-tablet js-snappable" data-link-name="news | group-0 | card-4" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/top-un-official-to-leave-myanmar-amid-criticism-rohingya-approach" data-loyalty-short-url="/p/7cec5">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/top-un-official-to-leave-myanmar-amid-criticism-rohingya-approach" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Myanmar</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Top UN official to leave amid criticism of Rohingya approach</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/top-un-official-to-leave-myanmar-amid-criticism-rohingya-approach" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Top UN official to leave amid criticism of Rohingya approach</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--list-mobile fc-item--list-tablet js-snappable" data-link-name="news | group-0 | card-5" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/hamas-claims-deal-agreed-fatah-control-gaza-strip" data-loyalty-short-url="/p/7cdqk">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/hamas-claims-deal-agreed-fatah-control-gaza-strip" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Gaza Strip</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Hamas claims deal agreed with Fatah over control of territory</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/hamas-claims-deal-agreed-fatah-control-gaza-strip" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Hamas claims deal agreed with Fatah over control of territory</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--list-mobile fc-item--list-tablet js-snappable" data-link-name="news | group-0 | card-6" data-item-visibility="all" data-test-id="facia-card" data-id="us-news/2017/oct/12/democrats-ban-proposal-ammunition-magazines-las-vegas" data-loyalty-short-url="/p/7cf6f">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/us-news/2017/oct/12/democrats-ban-proposal-ammunition-magazines-las-vegas" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">US gun control</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Democrats propose ban on high-capacity magazines in wake of Las Vegas attack</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/us-news/2017/oct/12/democrats-ban-proposal-ammunition-magazines-las-vegas" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Democrats propose ban on high-capacity magazines in wake of Las Vegas attack</a>
</div>
</div> </li>
<li class="fc-show-more--hide-on-mobile js-hide-on-mobile fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--list-mobile fc-item--list-tablet js-snappable" data-link-name="news | group-0 | card-7" data-item-visibility="desktop" data-test-id="facia-card" data-id="world/2017/oct/12/philippines-rodrigo-duterte-police-war-drugs" data-loyalty-short-url="/p/7ccc2">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/philippines-rodrigo-duterte-police-war-drugs" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Philippines</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Rodrigo Duterte pulls police out of brutal war on drugs</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/philippines-rodrigo-duterte-police-war-drugs" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Rodrigo Duterte pulls police out of brutal war on drugs</a>
</div>
</div> </li>
<li class="fc-show-more--hide-on-mobile js-hide-on-mobile fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--list-mobile fc-item--list-tablet js-snappable" data-link-name="news | group-0 | card-8" data-item-visibility="desktop" data-test-id="facia-card" data-id="global-development/2017/oct/12/myanmar-mass-graves-mystery-surrounds-deaths-of-hindu-villagers-dirty-tricks-rohingya" data-loyalty-short-url="/p/7c9q8">
<div class="fc-item__container">
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/global-development/2017/oct/12/myanmar-mass-graves-mystery-surrounds-deaths-of-hindu-villagers-dirty-tricks-rohingya" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Myanmar</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Mystery surrounds deaths of Hindu villagers in mass graves</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/global-development/2017/oct/12/myanmar-mass-graves-mystery-surrounds-deaths-of-hindu-villagers-dirty-tricks-rohingya" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Mystery surrounds deaths of Hindu villagers in mass graves</a>
</div>
</div> </li>
</ul> </li>
</ul>
</div>
<div class="js-show-more-placeholder"></div>
<button class="button button--medium button--primary button--show-more collection__show-more js-show-more-button modern-visible" data-test-id="show-more" data-link-name="more"> <span class="inline-plus inline-icon ">
<svg width="18" height="18" viewbox="0 0 18 18" class="inline-plus__svg inline-icon__svg">
<path d="M8.2 0h1.6l.4 7.8 7.8.4v1.6l-7.8.4-.4 7.8H8.2l-.4-7.8L0 9.8V8.2l7.8-.4.4-7.8z"/>
</svg> </span> <span class="inline-minus inline-icon ">
<svg width="32" height="32" viewbox="0 0 32 32" class="inline-minus__svg inline-icon__svg">
<path d="M5 15h22v3H5z"/>
</svg> </span> <span class="js-button-text">More around the world</span> </button>
</div>
</div>
</section>
<section class="fc-container__mpu--mobile">
<div id="dfp-ad--inline2--mobile" class="js-ad-slot ad-slot ad-slot--inline2 ad-slot--container-inline ad-slot--mobile mobile-only" data-link-name="ad slot inline2" data-name="inline2" data-mobile="1,1|2,2|300,250|fluid">
</div>
</section>
<section id="explore" class="fc-container fc-container--dynamic-slow-mpu fc-container--has-show-more fc-container--will-have-toggle js-container--toggle " data-link-name="container-7 | explore" data-id="22167321-f8cf-4f4a-b646-165e5b1e9a30" data-component="explore" aria-expanded="true">
<div class="fc-container__inner">
<div class="fc-container__header
                js-container__header
                ">
<div class="fc-container__header__title">
<span tabindex="0">explore</span>
</div>
</div>
<ul class="treats__container">
<li class="treats__list-item"> <a href="/news/series/the-long-read" data-link-name="treat | 1 | The long read" class="treats__treat">The long read</a> </li>
</ul>
<div class="fc-container--rolled-up-hide fc-container__body fc-show-more--hidden js-container--fc-show-more" data-title="explore" data-id="22167321-f8cf-4f4a-b646-165e5b1e9a30">
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-4 fc-slice fc-slice--qqq-q">
<li class="fc-slice__item l-row__item l-row__item--span-3 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-feature--item fc-item--standard-mobile fc-item--three-quarters-tablet js-snappable" data-link-name="feature | group-1+ | card-1" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/how-europes-far-right-fell-in-love-with-australias-immigration-policy" data-loyalty-short-url="/p/7ca43">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="460px" srcset="https://i.guim.co.uk/img/media/dd2c863dbebeb815af2dca682486917fdf62926e/0_0_4000_2399/master/4000.jpg?w=460&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=f1da53334b58529b1ef844d752d4f4ef 920w">
<source media="(min-width: 980px)" sizes="460px" srcset="https://i.guim.co.uk/img/media/dd2c863dbebeb815af2dca682486917fdf62926e/0_0_4000_2399/master/4000.jpg?w=460&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=a53ef013b14659190c73ff1118725a59 460w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="340px" srcset="https://i.guim.co.uk/img/media/dd2c863dbebeb815af2dca682486917fdf62926e/0_0_4000_2399/master/4000.jpg?w=340&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=50231e672c5472185dfc47fa6a8d1504 680w">
<source media="(min-width: 740px)" sizes="340px" srcset="https://i.guim.co.uk/img/media/dd2c863dbebeb815af2dca682486917fdf62926e/0_0_4000_2399/master/4000.jpg?w=340&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=6bfb4aaaa189299d81c7eb8ea9b011d7 340w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="95vw" srcset="https://i.guim.co.uk/img/media/dd2c863dbebeb815af2dca682486917fdf62926e/0_0_4000_2399/master/4000.jpg?w=460&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=f1da53334b58529b1ef844d752d4f4ef 920w, https://i.guim.co.uk/img/media/dd2c863dbebeb815af2dca682486917fdf62926e/0_0_4000_2399/master/4000.jpg?w=340&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=50231e672c5472185dfc47fa6a8d1504 680w, https://i.guim.co.uk/img/media/dd2c863dbebeb815af2dca682486917fdf62926e/0_0_4000_2399/master/4000.jpg?w=445&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=e384689e56c8c66f145b37bb2b8802d7 890w, https://i.guim.co.uk/img/media/dd2c863dbebeb815af2dca682486917fdf62926e/0_0_4000_2399/master/4000.jpg?w=605&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=b8485c53021f33ae4e58d4012ecfac78 1210w">
<source media="(min-width: 0px)" sizes="95vw" srcset="https://i.guim.co.uk/img/media/dd2c863dbebeb815af2dca682486917fdf62926e/0_0_4000_2399/master/4000.jpg?w=460&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=a53ef013b14659190c73ff1118725a59 460w, https://i.guim.co.uk/img/media/dd2c863dbebeb815af2dca682486917fdf62926e/0_0_4000_2399/master/4000.jpg?w=340&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=6bfb4aaaa189299d81c7eb8ea9b011d7 340w, https://i.guim.co.uk/img/media/dd2c863dbebeb815af2dca682486917fdf62926e/0_0_4000_2399/master/4000.jpg?w=445&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=3b7cc914c56ff870da454e7421acc03a 445w, https://i.guim.co.uk/img/media/dd2c863dbebeb815af2dca682486917fdf62926e/0_0_4000_2399/master/4000.jpg?w=605&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=ce72d166b1aff4e264e5d75fa2d088b6 605w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/how-europes-far-right-fell-in-love-with-australias-immigration-policy" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">The long read</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">How Europe's far right fell in love with Australia's immigration policy</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
European nativist parties have embraced Australia’s hardline tactics for managing asylum seekers and refugees – but their true agenda is to keep Muslims out
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/how-europes-far-right-fell-in-love-with-australias-immigration-policy" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">How Europe's far right fell in love with Australia's immigration policy</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-feature--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="feature | group-1 | card-2" data-item-visibility="all" data-test-id="facia-card" data-id="tv-and-radio/2017/oct/12/the-war-with-no-end-why-american-television-refuses-to-leave-the-trenches" data-loyalty-short-url="/p/7bhyz">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/a080676f40a880e85533e5f40b9eb667655453c5/8_0_3761_2258/master/3761.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=3d40ebcfd840469ecb7f502e8f4861ba 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/a080676f40a880e85533e5f40b9eb667655453c5/8_0_3761_2258/master/3761.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=398c6b4ead4d194ca2e27f46fe7e4415 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/a080676f40a880e85533e5f40b9eb667655453c5/8_0_3761_2258/master/3761.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=141e7159996834c5fc8ac1e945616910 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/a080676f40a880e85533e5f40b9eb667655453c5/8_0_3761_2258/master/3761.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=1d50f68caea8afb2819f3d5e6193b704 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/a080676f40a880e85533e5f40b9eb667655453c5/8_0_3761_2258/master/3761.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=8806b1bd8860eacdd9ac7718b0569ba5 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/a080676f40a880e85533e5f40b9eb667655453c5/8_0_3761_2258/master/3761.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=54fc5c6cf42415b32771104625cff5cb 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/tv-and-radio/2017/oct/12/the-war-with-no-end-why-american-television-refuses-to-leave-the-trenches" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">The war with no end</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Why American television refuses to leave the trenches</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
American TV has long been a barometer for the country’s feelings on its military – so what do a new crop of shows say about the opinions of a divided nation?
<br>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/tv-and-radio/2017/oct/12/the-war-with-no-end-why-american-television-refuses-to-leave-the-trenches" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Why American television refuses to leave the trenches</a>
</div>
</div> </li>
</ul>
</div>
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-2 fc-slice fc-slice--hl3-mpu">
<li class="fc-slice__item l-row__item l-row__item--span-1">
<ul class="u-unstyled l-list l-list--columns-1 l-list--rows-3">
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-feature--item fc-item--list-media-mobile fc-item--list-media-tablet js-snappable" data-discussion-id="/p/7cetn" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/music/2017/oct/12/america-stand-up-eminems-freestyle-and-the-10-best-anti-trump-protest-songs-so-far#comments" data-link-name="feature | group-0 | card-3" data-item-visibility="all" data-test-id="facia-card" data-id="music/2017/oct/12/america-stand-up-eminems-freestyle-and-the-10-best-anti-trump-protest-songs-so-far" data-loyalty-short-url="/p/7cetn">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/371415f0c4e12ebf98092c0339486c3a8ccd77e6/0_0_5000_3000/master/5000.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=70c68c32b8a49ebfb3d1e534fc9fc8f3 280w">
<source media="(min-width: 980px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/371415f0c4e12ebf98092c0339486c3a8ccd77e6/0_0_5000_3000/master/5000.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=41b67ab88a6a827cc6fcf8b04a33268b 140w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/371415f0c4e12ebf98092c0339486c3a8ccd77e6/0_0_5000_3000/master/5000.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=70c68c32b8a49ebfb3d1e534fc9fc8f3 280w">
<source media="(min-width: 740px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/371415f0c4e12ebf98092c0339486c3a8ccd77e6/0_0_5000_3000/master/5000.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=41b67ab88a6a827cc6fcf8b04a33268b 140w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/371415f0c4e12ebf98092c0339486c3a8ccd77e6/0_0_5000_3000/master/5000.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=99bc058d0481e52ec900efdfaea03905 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/371415f0c4e12ebf98092c0339486c3a8ccd77e6/0_0_5000_3000/master/5000.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=012631bc8c7a96a119dc1ebf7b955f0f 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/music/2017/oct/12/america-stand-up-eminems-freestyle-and-the-10-best-anti-trump-protest-songs-so-far" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">'America, stand up'</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Eminem's freestyle and the 10 best anti-Trump protest songs (so far)</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/music/2017/oct/12/america-stand-up-eminems-freestyle-and-the-10-best-anti-trump-protest-songs-so-far" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Eminem's freestyle and the 10 best anti-Trump protest songs (so far)</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--list-media-mobile fc-item--list-media-tablet js-snappable" data-link-name="news | group-0 | card-4" data-item-visibility="all" data-test-id="facia-card" data-id="culture/2017/oct/12/late-night-on-weinstein-the-second-giant-vortex-of-destructive-moisture-named-harvey" data-loyalty-short-url="/p/7cf9x">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/579b3bd47e695570fa26e9ec6359946a02ee6f90/71_0_1288_773/master/1288.png?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=90dc729e1e250128d0ba3b0598747a06 280w">
<source media="(min-width: 980px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/579b3bd47e695570fa26e9ec6359946a02ee6f90/71_0_1288_773/master/1288.png?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=ae95b6d59631580c3e718c023c979c44 140w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/579b3bd47e695570fa26e9ec6359946a02ee6f90/71_0_1288_773/master/1288.png?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=90dc729e1e250128d0ba3b0598747a06 280w">
<source media="(min-width: 740px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/579b3bd47e695570fa26e9ec6359946a02ee6f90/71_0_1288_773/master/1288.png?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=ae95b6d59631580c3e718c023c979c44 140w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/579b3bd47e695570fa26e9ec6359946a02ee6f90/71_0_1288_773/master/1288.png?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=efeb24303676dc314abd55b573759888 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/579b3bd47e695570fa26e9ec6359946a02ee6f90/71_0_1288_773/master/1288.png?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=d7657912a79ebc6bde2e0f916e769e25 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/culture/2017/oct/12/late-night-on-weinstein-the-second-giant-vortex-of-destructive-moisture-named-harvey" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">US late-night hosts on Weinstein</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">The second giant vortex of destructive moisture named Harvey</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/culture/2017/oct/12/late-night-on-weinstein-the-second-giant-vortex-of-destructive-moisture-named-harvey" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">The second giant vortex of destructive moisture named Harvey</a>
</div>
</div> </li>
<li class="fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-feature--item fc-item--list-media-mobile fc-item--list-media-tablet js-snappable" data-link-name="feature | group-0 | card-5" data-item-visibility="all" data-test-id="facia-card" data-id="working-in-development/2017/oct/12/traffic-accident-call-a-reporter-how-journalists-are-forcing-change-in-liberia" data-loyalty-short-url="/p/79pxe">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/022a37c1cf4b43f2bcd582bd38b9fbbde6acbde5/0_0_4957_2975/master/4957.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=48f1d5eaf7d9f389d5e5da26a49065ed 280w">
<source media="(min-width: 980px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/022a37c1cf4b43f2bcd582bd38b9fbbde6acbde5/0_0_4957_2975/master/4957.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=7e86dbc3f57896d6815e3bc35bdd807d 140w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="140px" srcset="https://i.guim.co.uk/img/media/022a37c1cf4b43f2bcd582bd38b9fbbde6acbde5/0_0_4957_2975/master/4957.jpg?w=140&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=48f1d5eaf7d9f389d5e5da26a49065ed 280w">
<source media="(min-width: 740px)" sizes="140px" srcset="https://i.guim.co.uk/img/media/022a37c1cf4b43f2bcd582bd38b9fbbde6acbde5/0_0_4957_2975/master/4957.jpg?w=140&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=7e86dbc3f57896d6815e3bc35bdd807d 140w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/022a37c1cf4b43f2bcd582bd38b9fbbde6acbde5/0_0_4957_2975/master/4957.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=8a2d3ad5c267f41dbe8c95be61822990 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/022a37c1cf4b43f2bcd582bd38b9fbbde6acbde5/0_0_4957_2975/master/4957.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=98bbf4f16bfea921c56ff71986e85dd7 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/working-in-development/2017/oct/12/traffic-accident-call-a-reporter-how-journalists-are-forcing-change-in-liberia" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Call a reporter!</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">How journalists are forcing change in Liberia</span></span> </a></h2>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/working-in-development/2017/oct/12/traffic-accident-call-a-reporter-how-journalists-are-forcing-change-in-liberia" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">How journalists are forcing change in Liberia</a>
</div>
</div> </li>
</ul> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 fc-slice__item--mpu-candidate">
<div id="dfp-ad--inline2" class="js-ad-slot ad-slot ad-slot--inline2 ad-slot--container-inline hide-until-tablet" data-link-name="ad slot inline2" data-name="inline2" data-mobile="1,1|2,2|300,250|fluid">
</div> </li>
</ul>
</div>
<div class="js-show-more-placeholder"></div>
<button class="button button--medium button--primary button--show-more collection__show-more js-show-more-button modern-visible" data-test-id="show-more" data-link-name="more"> <span class="inline-plus inline-icon ">
<svg width="18" height="18" viewbox="0 0 18 18" class="inline-plus__svg inline-icon__svg">
<path d="M8.2 0h1.6l.4 7.8 7.8.4v1.6l-7.8.4-.4 7.8H8.2l-.4-7.8L0 9.8V8.2l7.8-.4.4-7.8z"/>
</svg> </span> <span class="inline-minus inline-icon ">
<svg width="32" height="32" viewbox="0 0 32 32" class="inline-minus__svg inline-icon__svg">
<path d="M5 15h22v3H5z"/>
</svg> </span> <span class="js-button-text">More explore</span> </button>
</div>
</div>
</section>
<section id="securedrop" class="fc-container fc-container--thrasher fc-container--will-have-toggle flashing-image js-container--toggle " data-link-name="container-8 | securedrop" data-id="774cb333-ee30-45cd-9606-d17ceb02029c" data-component="securedrop" aria-expanded="true">
<div class="fc-container__inner">
<div class="fc-container__header
                js-container__header
                ">
<div class="fc-container__header__title">
<span tabindex="0">securedrop</span>
</div>
</div>
<div class="fc-container--rolled-up-hide fc-container__body" data-title="securedrop" data-id="774cb333-ee30-45cd-9606-d17ceb02029c">
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-1 fc-slice fc-slice--mf">
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="facia-snap facia-snap--default facia-snap-embed fc-item fc-item--has-no-image js-fc-item js-snap tone-news--item fc-item--fluid-mobile fc-item--fluid-tablet " data-link-name="news | group-0 | card-1" data-item-visibility="all" data-test-id="facia-card" data-id="snap/1486403500105" data-snap-type="json.html" data-snap-uri="https://interactive.guim.co.uk/thrashers/secure-drop/source.json">
<div class="secure-drop__wrapper">
<style>#secure-drop.fc-container--thrasher,#securedrop.fc-container--thrasher{background:#003559}#secure-drop.fc-container--thrasher .fc-item,#securedrop.fc-container--thrasher .fc-item{background:#00456E}.secure-drop__wrapper{position:relative}@media all and (min-width:61.25em){.secure-drop__wrapper{width:100%}}.secure-drop__wrapper .securedrop{color:#F6F6F6;max-width:620px;margin:0 auto}@media all and (min-width:30em){.secure-drop__wrapper .securedrop{padding:0 10px}.secure-drop__wrapper .securedrop__roundel svg{-webkit-transform-origin:top right;transform-origin:top right;-webkit-transform:scale(1.2);transform:scale(1.2)}}@media all and (min-width:46.25em){.secure-drop__wrapper .securedrop{padding:0 20px;max-width:none}}@media all and (min-width:71.25em){.secure-drop__wrapper .securedrop{margin-left:160px}.secure-drop__wrapper .securedrop__title{position:absolute;top:0;left:20px}}@media all and (min-width:81.25em){.secure-drop__wrapper .securedrop{margin-left:240px}}.secure-drop__wrapper .securedrop__title{display:inline-block;padding-top:2px;color:#4BC6DF;float:none;width:auto}.secure-drop__wrapper .securedrop__roundel{float:right;margin-top:5px}@media all and (min-width:71.25em){.secure-drop__wrapper .securedrop__roundel{margin-top:1px}}.secure-drop__wrapper .securedrop__main{display:block;font-size:24px;line-height:26px;font-weight:600;padding-top:1px;padding-bottom:18px;margin-top:-3px}@media all and (min-width:46.25em){.secure-drop__wrapper .securedrop__main{font-size:26px;line-height:28px}}@media all and (min-width:71.25em){.secure-drop__wrapper .securedrop__main{margin-top:3px}}.secure-drop__wrapper .securedrop__main,.secure-drop__wrapper .securedrop__main:hover{text-decoration:none}.secure-drop__wrapper .securedrop__main .eyes{display:inline-block;font-size:0;vertical-align:bottom;position:relative}.secure-drop__wrapper .securedrop__main .eyes .target{position:absolute;top:50%;left:50%;width:20px;height:18px;z-index:1;-webkit-transform:translate3d(-50%,-50%,0);transform:translate3d(-50%,-50%,0)}.secure-drop__wrapper .securedrop__main .eyes .target:hover+.eye .inside{top:50%!important;left:75%!important}.secure-drop__wrapper .securedrop__main .eyes .target:hover+.eye+.eye .inside{top:50%!important;left:25%!important}.secure-drop__wrapper .securedrop__main .eyes .eye{display:inline-block;position:relative;top:7px}.secure-drop__wrapper .securedrop__main .eyes .eye .outside,.secure-drop__wrapper .securedrop__main .eyes .eye svg{display:block}.secure-drop__wrapper .securedrop__main .eyes .eye+.eye{margin-left:4px}.secure-drop__wrapper .securedrop__main .eyes .eye .inside{-webkit-transition:all .4s ease-in;transition:all .4s ease-in;position:absolute;top:50%;left:50%;-webkit-transform:translate3d(-48%,-50%,0);transform:translate3d(-48%,-50%,0)}.secure-drop__wrapper .securedrop__main .cta{display:inline}.secure-drop__wrapper .securedrop__main .btn{display:inline-block;vertical-align:top;position:relative;top:1px;line-height:30px;width:24px;height:24px;border-radius:100%;border:1px solid #ececec}.secure-drop__wrapper .securedrop__main .btn svg{height:100%;width:100%;display:block}.secure-drop__wrapper .securedrop__main .btn svg path{fill:#ececec}.secure-drop__wrapper .securedrop__main:hover .btn{background-color:#4BC6DF;border-color:transparent}.secure-drop__wrapper .securedrop__main:hover .btn svg path{fill:#F6F6F6}</style>
<div class="securedrop">
<a href="https://www.theguardian.com/help/ng-interactive/2017/mar/17/contact-the-guardian-securely" class="securedrop__title fc-container__header__title" data-link-name="securedrop thrasher : container title">tip us off</a>
<div class="securedrop__roundel">
<svg width="27" height="23" viewbox="335 248 27 23" xmlns="http://www.w3.org/2000/svg">
<path d="M361 260.02c0 3.66-1.5 6.93-3.9 9.3.44-.9.7-1.95.7-3.1 0-3.58-1.88-5.13-5.87-5.13h-6.4c-.7 0-1.28-.6-1.28-1.2 0-.47.35-.98.82-1.3.95.3 1.78.32 2.93.32 4.58 0 7.74-2.26 7.68-6.2-.03-2.22-.97-3.8-2.54-4.75 4.58 2 7.86 6.57 7.86 12zm-18.44-11.93c-4.4 2.1-7.56 6.6-7.56 11.9 0 3.6 1.48 6.74 3.75 9.13v-.18c0-2.3 2.25-3.22 4.3-3.6-1.93-.45-2.85-1.8-2.85-3.22 0-1.87 2.07-3.5 3.07-4.2l-.1-.05c-1.7-1.16-2.94-2.74-2.94-5.1 0-2.04.9-3.65 2.33-4.7zm7.77 4.7c0 3.53-1.06 3.92-2.33 3.92s-2.33-.3-2.33-3.96c0-3.67 1.06-4.15 2.33-4.15 1.33 0 2.33.58 2.33 4.15zm.15 13.62c1.63 0 2.5.83 2.5 2.05 0 1.42-1.02 2.5-4.86 2.5-3.37 0-4.52-1.17-4.52-2.45 0-.95.4-2.1 2.07-2.1h4.8z" fill="#F6F6F6" fill-rule="evenodd"/>
</svg>
</div>
<a href="https://www.theguardian.com/help/ng-interactive/2017/mar/17/contact-the-guardian-securely" class="securedrop__main" data-link-name="securedrop thrasher : inner area">
<div class="eyes">
<div class="target" id="securedrop-eyes-target"></div>
<div class="eye">
<div class="outside">
<svg width="25" height="16" viewbox="13 5 25 16" xmlns="http://www.w3.org/2000/svg">
<path d="M25.5 5C32.05 5 38 12.33 38 12.33v1.34S32.03 21 25.5 21 13 13.67 13 13.67v-1.34S18.95 5 25.5 5z" fill="#F6F6F6" fill-rule="evenodd"/>
</svg>
</div>
<div class="inside">
<svg width="10" height="10" viewbox="21 7 10 10" xmlns="http://www.w3.org/2000/svg">
<circle fill="#00456E" fill-rule="evenodd" cx="26" cy="12" r="5"/>
</svg>
</div>
</div>
<div class="eye">
<div class="outside">
<svg width="25" height="16" viewbox="13 5 25 16" xmlns="http://www.w3.org/2000/svg">
<path d="M25.5 5C32.05 5 38 12.33 38 12.33v1.34S32.03 21 25.5 21 13 13.67 13 13.67v-1.34S18.95 5 25.5 5z" fill="#F6F6F6" fill-rule="evenodd"/>
</svg>
</div>
<div class="inside">
<svg width="10" height="10" viewbox="21 7 10 10" xmlns="http://www.w3.org/2000/svg">
<circle fill="#00456E" fill-rule="evenodd" cx="26" cy="12" r="5"/>
</svg>
</div>
</div>
</div>
<div class="cta">
Share&nbsp;stories with the&nbsp;Guardian securely and&nbsp;confidentially
</div>
<div class="btn">
<svg width="24" height="24" viewbox="240 334 24 24" xmlns="http://www.w3.org/2000/svg">
<g fill="none" fill-rule="evenodd" transform="translate(240 334)">
<path fill="#F6F6F6" d="M4 12.68h13.3l-5.22 6.15.68.67L20 12.34v-.68L12.76 4.5l-.68.67 5.2 6.15H4"/>
</g>
</svg>
</div> </a>
</div>
<img style="height:0;width:0;visibility:hidden;position:absolute;z-index: 1;" height="0" width="0" src="https://interactive.guim.co.uk/thrashers/secure-drop/hashed/empty.db892fb1.gif" onload="var script=document.createElement('script');script.src='https://interactive.guim.co.uk/thrashers/secure-drop/hashed/main.99839311.js'; document.body.appendChild(script);">
</div>
</div> </li>
</ul>
</div>
</div>
</div>
</section>
<section class="fc-container__mpu--mobile">
<div id="dfp-ad--inline3--mobile" class="js-ad-slot ad-slot ad-slot--inline3 ad-slot--container-inline ad-slot--mobile mobile-only" data-link-name="ad slot inline3" data-name="inline3" data-mobile="1,1|2,2|300,250|fluid">
</div>
</section>
<section id="the-defenders" class="fc-container fc-container--has-show-more fc-container--will-have-toggle js-container--toggle " data-link-name="container-9 | the-defenders" data-id="a4510b73-b032-40c6-86cc-cf3ecdbf888a" data-component="the-defenders" aria-expanded="true">
<div class="fc-container__inner">
<div class="fc-container__header js-container__header">
<div class="fc-container__header
                
                ">
<div class="fc-container__header__title">
<a data-link-name="section heading" href="https://www.theguardian.com/environment/series/the-defenders"> <span class="fc-container__title__text">the defenders</span> </a>
</div>
</div>
<div class="fc-container__header__description">
This year, in collaboration with Global Witness, the Guardian will attempt to record all of the deaths of people who are killed while defending their land, forests, rivers or wildlife
</div>
</div>
<div class="fc-container--rolled-up-hide fc-container__body fc-show-more--hidden js-container--fc-show-more" data-title="the defenders" data-id="a4510b73-b032-40c6-86cc-cf3ecdbf888a">
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-4 fc-slice fc-slice--q-q-q-q">
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="news | group-0 | card-1" data-item-visibility="all" data-test-id="facia-card" data-id="environment/2017/oct/11/2017-deadliest-on-record-for-land-defenders-mining-logging" data-loyalty-short-url="/p/7c9f5">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/c5b3f690be48b38bfcbd981668c0602ab083f36c/0_274_4608_2765/master/4608.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=68d83272289938e4d8a7466a2da7bc54 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/c5b3f690be48b38bfcbd981668c0602ab083f36c/0_274_4608_2765/master/4608.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=d26f26c46455796c58926c488a9ee51c 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/c5b3f690be48b38bfcbd981668c0602ab083f36c/0_274_4608_2765/master/4608.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=90442839b01688b8b5ff79c9b6549c39 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/c5b3f690be48b38bfcbd981668c0602ab083f36c/0_274_4608_2765/master/4608.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=19d371c0ede3c6589195a5d851616547 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/c5b3f690be48b38bfcbd981668c0602ab083f36c/0_274_4608_2765/master/4608.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=a7f744abba276b3095bd92ef61b3c868 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/c5b3f690be48b38bfcbd981668c0602ab083f36c/0_274_4608_2765/master/4608.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=8fc7446a74638ecf14f2ef638fffb95b 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/environment/2017/oct/11/2017-deadliest-on-record-for-land-defenders-mining-logging" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Environmental defenders</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">2017 on course to be deadliest on record</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
Deaths of environmental activists locked in conflict with mining, logging and agricultural companies across three continents has passed 150
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/environment/2017/oct/11/2017-deadliest-on-record-for-land-defenders-mining-logging" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">2017 on course to be deadliest on record</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-feature--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="feature | group-0 | card-2" data-item-visibility="all" data-test-id="facia-card" data-id="environment/2017/oct/04/the-day-we-witnessed-wildlife-rangers-being-gunned-down-in-congo" data-loyalty-short-url="/p/7a7dz">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/27a0aa39c736eaeef598546d77c877faca7ea065/0_915_2287_1372/master/2287.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=1e630dbe882596efb0e3f9aec41b538f 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/27a0aa39c736eaeef598546d77c877faca7ea065/0_915_2287_1372/master/2287.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=249d6955be23a2d732d769ae60c603e6 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/27a0aa39c736eaeef598546d77c877faca7ea065/0_915_2287_1372/master/2287.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=2cf64ce91af17d07d604904202f974a1 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/27a0aa39c736eaeef598546d77c877faca7ea065/0_915_2287_1372/master/2287.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=f9da0cba33b6669e0ba719072ba715c5 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/27a0aa39c736eaeef598546d77c877faca7ea065/0_915_2287_1372/master/2287.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=6216e3db3b773a3351e0fb272ff80712 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/27a0aa39c736eaeef598546d77c877faca7ea065/0_915_2287_1372/master/2287.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e47a8caf5bd89f23dfea0e070891d303 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/environment/2017/oct/04/the-day-we-witnessed-wildlife-rangers-being-gunned-down-in-congo" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Congo</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">The day we witnessed wildlife rangers being gunned down</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
When two Dutch journalists travelled to the DRC to report on illegal gold mining in the vast Okapi wildlife reserve, they ended up running for their lives
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/environment/2017/oct/04/the-day-we-witnessed-wildlife-rangers-being-gunned-down-in-congo" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">The day we witnessed wildlife rangers being gunned down</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-sublinks-1 js-fc-item tone-news--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="news | group-0 | card-3" data-item-visibility="all" data-test-id="facia-card" data-id="environment/ng-interactive/2017/jul/13/the-defenders-tracker" data-loyalty-short-url="/p/6jmx8">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/f38ab9d5076a93cbce5796ddd770bc2dae2c9fe7/0_0_800_478/master/800.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=4400408b89f96b1cf1f4a68e1038f249 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/f38ab9d5076a93cbce5796ddd770bc2dae2c9fe7/0_0_800_478/master/800.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=c4c4601f2dab69e333276213dcd187da 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/f38ab9d5076a93cbce5796ddd770bc2dae2c9fe7/0_0_800_478/master/800.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=0b08f74c32db45bf06eaafbe634babaf 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/f38ab9d5076a93cbce5796ddd770bc2dae2c9fe7/0_0_800_478/master/800.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=a5026a15966ffae2d47dbbc66b66ae05 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/f38ab9d5076a93cbce5796ddd770bc2dae2c9fe7/0_0_800_478/master/800.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=93a128d0c653499d9604f613fc6e3986 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/f38ab9d5076a93cbce5796ddd770bc2dae2c9fe7/0_0_800_478/master/800.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=52f21146dec358fc904c2285a7fdc29c 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/environment/ng-interactive/2017/jul/13/the-defenders-tracker" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Latest toll: 153</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Recording the deaths of environmental defenders worldwide</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
This year, in collaboration with Global Witness, the Guardian aims to record the deaths of all people killed while protecting land or natural resources. At the current rate, about four defenders will die this week somewhere on the planet
</div>
<div class="fc-item__footer--vertical" aria-hidden="true">
<ul class="fc-sublinks u-unstyled u-faux-block-link__promote">
<li class="fc-sublink tone-news--sublink" data-link-name="sublinks | 1"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/environment/series/the-defenders" data-link-name="kicker" class="fc-sublink__kicker">The defenders</a> <a href="https://www.theguardian.com/environment/2017/jul/13/environmental-defenders-who-are-they-and-how-do-we-decide-if-they-have-died-in-defence-of-their-environment" class="fc-sublink__link" data-link-name="article">Who are they?</a> </h3> </li>
</ul>
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<footer class="fc-item__footer--horizontal">
<ul class="fc-sublinks u-unstyled u-faux-block-link__promote">
<li class="fc-sublink tone-news--sublink" data-link-name="sublinks | 1"> <h3 class="fc-sublink__title"> <a href="https://www.theguardian.com/environment/series/the-defenders" data-link-name="kicker" class="fc-sublink__kicker">The defenders</a> <a href="https://www.theguardian.com/environment/2017/jul/13/environmental-defenders-who-are-they-and-how-do-we-decide-if-they-have-died-in-defence-of-their-environment" class="fc-sublink__link" data-link-name="article">Who are they?</a> </h3> </li>
</ul>
</footer>
<a href="https://www.theguardian.com/environment/ng-interactive/2017/jul/13/the-defenders-tracker" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Recording the deaths of environmental defenders worldwide</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="news | group-0 | card-4" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/sep/29/cameroon-palm-oil-campaigner-arrested-crackdown-activists" data-loyalty-short-url="/p/7acvv">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/14ee64521d0b381716cf3097d43db69b22c3b5b4/0_402_2439_1463/master/2439.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=f2be932f1665e200cc672b2b725baaef 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/14ee64521d0b381716cf3097d43db69b22c3b5b4/0_402_2439_1463/master/2439.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=2fa4319d3c29402df41a63e5113c7d35 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/14ee64521d0b381716cf3097d43db69b22c3b5b4/0_402_2439_1463/master/2439.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=074174d51b23546ce2695a2250efb3bd 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/14ee64521d0b381716cf3097d43db69b22c3b5b4/0_402_2439_1463/master/2439.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=32c22f998fd5d5e4e939f766b0ce0050 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/14ee64521d0b381716cf3097d43db69b22c3b5b4/0_402_2439_1463/master/2439.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=26ed12bfca37aaaf23cf5ed0c58f3200 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/14ee64521d0b381716cf3097d43db69b22c3b5b4/0_402_2439_1463/master/2439.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=56ced3beea89b031eb1825ac656483c7 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/sep/29/cameroon-palm-oil-campaigner-arrested-crackdown-activists" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Cameroon</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Palm oil campaigner arrested in crackdown on activists</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
Nasako Besingi has been jailed after opposing a US-funded palm-oil plantation and supporters say this is linked to Cameroon’s ‘anglophone crisis’
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/sep/29/cameroon-palm-oil-campaigner-arrested-crackdown-activists" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Palm oil campaigner arrested in crackdown on activists</a>
</div>
</div> </li>
</ul>
</div>
<div class="js-show-more-placeholder"></div>
<button class="button button--medium button--primary button--show-more collection__show-more js-show-more-button modern-visible" data-test-id="show-more" data-link-name="more"> <span class="inline-plus inline-icon ">
<svg width="18" height="18" viewbox="0 0 18 18" class="inline-plus__svg inline-icon__svg">
<path d="M8.2 0h1.6l.4 7.8 7.8.4v1.6l-7.8.4-.4 7.8H8.2l-.4-7.8L0 9.8V8.2l7.8-.4.4-7.8z"/>
</svg> </span> <span class="inline-minus inline-icon ">
<svg width="32" height="32" viewbox="0 0 32 32" class="inline-minus__svg inline-icon__svg">
<path d="M5 15h22v3H5z"/>
</svg> </span> <span class="js-button-text">More the defenders</span> </button>
</div>
</div>
</section>
<section id="people" class="fc-container fc-container--lazy-load fc-container--will-have-toggle js-container--lazy-load js-container--toggle " data-link-name="container-10 | people" data-id="71f36f15-5113-4ab0-82cc-9efef1baada5" data-component="people" aria-expanded="true">
<div class="fc-container__inner">
<div class="fc-container__header
                js-container__header
                ">
<div class="fc-container__header__title">
<span tabindex="0">people</span>
</div>
</div>
<div class="fc-container--rolled-up-hide fc-container__body" data-title="people" data-id="71f36f15-5113-4ab0-82cc-9efef1baada5">
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-4 fc-slice fc-slice--q-q-q-q">
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="news | group-0 | card-1" data-item-visibility="all" data-test-id="facia-card" data-id="world/2017/oct/12/white-widow-sally-jones-was-fleeing-raqqa-as-isiss-capital-fell" data-loyalty-short-url="/p/7cfkf">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/9813783ae0a133e2a72faf98e4ebe13378842cb2/6_372_1474_884/master/1474.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=e76774d04dd5af36ac06ceeb86e0edf9 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/9813783ae0a133e2a72faf98e4ebe13378842cb2/6_372_1474_884/master/1474.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=6e6e23d1a8a24e6453c506928b975df1 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/9813783ae0a133e2a72faf98e4ebe13378842cb2/6_372_1474_884/master/1474.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=a522de99e583f5d5ae7c31f639650959 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/9813783ae0a133e2a72faf98e4ebe13378842cb2/6_372_1474_884/master/1474.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=9092067c915e96200fbc2d3c18a5918b 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/9813783ae0a133e2a72faf98e4ebe13378842cb2/6_372_1474_884/master/1474.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=e54dbdf32e170f91fcfd2cbbbd30ff60 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/9813783ae0a133e2a72faf98e4ebe13378842cb2/6_372_1474_884/master/1474.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=daff4ba77b368a186b522b19641a1fe2 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/white-widow-sally-jones-was-fleeing-raqqa-as-isiss-capital-fell" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Sally Jones</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Briton was fleeing Raqqa as Isis's capital fell</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
Briton, thought to have been killed in a drone strike near the Syrian border, was part of a huge exodus of foreign fighters
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/world/2017/oct/12/white-widow-sally-jones-was-fleeing-raqqa-as-isiss-capital-fell" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Briton was fleeing Raqqa as Isis's capital fell</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-news--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="news | group-0 | card-2" data-item-visibility="all" data-test-id="facia-card" data-id="media/2017/oct/12/us-journalist-who-broke-harvey-weinstein-story-to-get-channel-4-show" data-loyalty-short-url="/p/7cfmk">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/86b522e96946b555ea8e01adb590f3a91f219c32/0_304_2000_1200/master/2000.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=fb0a4b5464af6233c03ec7c74c6cb34d 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/86b522e96946b555ea8e01adb590f3a91f219c32/0_304_2000_1200/master/2000.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=4b29d65700dec1ea9c3d88c31567aa7d 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/86b522e96946b555ea8e01adb590f3a91f219c32/0_304_2000_1200/master/2000.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=c2005e35844dc19c2d1892e34ce7e61a 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/86b522e96946b555ea8e01adb590f3a91f219c32/0_304_2000_1200/master/2000.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=48121e27d1c78d6891e1c69ca8dd1af8 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/86b522e96946b555ea8e01adb590f3a91f219c32/0_304_2000_1200/master/2000.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=c5c29aa49550e090bd5d06ab9967a8e8 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/86b522e96946b555ea8e01adb590f3a91f219c32/0_304_2000_1200/master/2000.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=647ec0c5294febe1d72c43a1105dc529 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/media/2017/oct/12/us-journalist-who-broke-harvey-weinstein-story-to-get-channel-4-show" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Ronan Farrow</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">US journalist who broke Harvey Weinstein story to get Channel 4 show</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
Ronan Farrow to present show planned as a ‘satirical take on the UK as seen through the eyes of America’
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/media/2017/oct/12/us-journalist-who-broke-harvey-weinstein-story-to-get-channel-4-show" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">US journalist who broke Harvey Weinstein story to get Channel 4 show</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-feature--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-discussion-id="/p/7cedz" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/film/2017/oct/12/andy-serkis-king-kong-was-the-epiphany-it-was-like-you-can-now-do-anything#comments" data-link-name="feature | group-0 | card-3" data-item-visibility="all" data-test-id="facia-card" data-id="film/2017/oct/12/andy-serkis-king-kong-was-the-epiphany-it-was-like-you-can-now-do-anything" data-loyalty-short-url="/p/7cedz">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/431401a97214abc92b176a46b8ad63a7ef7407b5/0_289_8660_5196/master/8660.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=cc13787a450c81cabcdaac742bef1ee3 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/431401a97214abc92b176a46b8ad63a7ef7407b5/0_289_8660_5196/master/8660.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=06bb5d092cd8c6194b91404001b594e2 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/431401a97214abc92b176a46b8ad63a7ef7407b5/0_289_8660_5196/master/8660.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=50ab738c294a5478aa2882d1b1e3015f 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/431401a97214abc92b176a46b8ad63a7ef7407b5/0_289_8660_5196/master/8660.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=e0c4b9d679bc4d32f8299c63657c11f0 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/431401a97214abc92b176a46b8ad63a7ef7407b5/0_289_8660_5196/master/8660.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=1f12a5f982a1bfff0d4f9ac453de6346 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/431401a97214abc92b176a46b8ad63a7ef7407b5/0_289_8660_5196/master/8660.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=c10496fbc4d8d0d3ecff2ea42eccc8cc 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/film/2017/oct/12/andy-serkis-king-kong-was-the-epiphany-it-was-like-you-can-now-do-anything" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Andy Serkis</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">King Kong was the epiphany. It was like: you can now do anything</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
His performances in films from The Lord of the Rings to Planet of the Apes helped transform movie acting. But his decision to direct a film, Breathe, about a disabled-rights campaigner is a very personal one, he explains
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/film/2017/oct/12/andy-serkis-king-kong-was-the-epiphany-it-was-like-you-can-now-do-anything" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">King Kong was the epiphany. It was like: you can now do anything</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-news--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-discussion-id="/p/7cf3g" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/books/2017/oct/12/writers-defend-author-accused-plagiarism-jill-bialosky-poetry-will-save-your-life#comments" data-link-name="news | group-0 | card-4" data-item-visibility="all" data-test-id="facia-card" data-id="books/2017/oct/12/writers-defend-author-accused-plagiarism-jill-bialosky-poetry-will-save-your-life" data-loyalty-short-url="/p/7cf3g">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/6862abc0b86e1c5f6e4b4fa371947cb56ed890f9/1445_7_4072_2443/master/4072.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=dea32e29972113074ba10beb89c06a12 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/6862abc0b86e1c5f6e4b4fa371947cb56ed890f9/1445_7_4072_2443/master/4072.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=02551e4f8d3f0f56bfab04862ff38343 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/6862abc0b86e1c5f6e4b4fa371947cb56ed890f9/1445_7_4072_2443/master/4072.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=5d9d69459107cf7034cfeea966dd0e83 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/6862abc0b86e1c5f6e4b4fa371947cb56ed890f9/1445_7_4072_2443/master/4072.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=2cccc3b4ba965f962fe10e3efc9a0308 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/6862abc0b86e1c5f6e4b4fa371947cb56ed890f9/1445_7_4072_2443/master/4072.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=3f5e52083301ba48ea9ef07018878cc2 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/6862abc0b86e1c5f6e4b4fa371947cb56ed890f9/1445_7_4072_2443/master/4072.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=43c77297f6eefbabe63ff1d36ce17e87 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/books/2017/oct/12/writers-defend-author-accused-plagiarism-jill-bialosky-poetry-will-save-your-life" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Jill Bialosky</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Writers step in to defend author accused of plagiarism in New York Times</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
Jill Bialosky’s memoir Poetry Will Save Your Life was charged extensive use of others’ writing, but peers say accidental repetitions ‘were not egregious theft’
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/books/2017/oct/12/writers-defend-author-accused-plagiarism-jill-bialosky-poetry-will-save-your-life" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Writers step in to defend author accused of plagiarism in New York Times</a>
</div>
</div> </li>
</ul>
</div>
</div>
</div>
</section>
<section class="fc-container__mpu--mobile">
<div id="dfp-ad--inline4--mobile" class="js-ad-slot ad-slot ad-slot--inline4 ad-slot--container-inline ad-slot--mobile mobile-only" data-link-name="ad slot inline4" data-name="inline4" data-mobile="1,1|2,2|300,250|fluid">
</div>
</section>
<section id="life" class="fc-container fc-container--lazy-load fc-container--will-have-toggle js-container--lazy-load js-container--toggle " data-link-name="container-11 | life" data-id="7b297ef5-a3f9-45e5-b915-b54951d7f6ec" data-component="life" aria-expanded="true">
<div class="fc-container__inner">
<div class="fc-container__header
                js-container__header
                ">
<div class="fc-container__header__title">
<span tabindex="0">life</span>
</div>
</div>
<div class="fc-container--rolled-up-hide fc-container__body" data-title="life" data-id="7b297ef5-a3f9-45e5-b915-b54951d7f6ec">
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-4 fc-slice fc-slice--h-q-q">
<li class="fc-slice__item l-row__item l-row__item--span-2 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-news--item fc-item--standard-mobile fc-item--half-tablet js-snappable" data-discussion-id="/p/7cf24" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/technology/2017/oct/12/shoe-colour-question-could-put-2015-dress-debate-in-the-shade#comments" data-link-name="news | group-0 | card-1" data-item-visibility="all" data-test-id="facia-card" data-id="technology/2017/oct/12/shoe-colour-question-could-put-2015-dress-debate-in-the-shade" data-loyalty-short-url="/p/7cf24">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="460px" srcset="https://i.guim.co.uk/img/media/7e5702c568d4bf828db2315243274f988b458330/31_223_567_340/master/567.png?w=460&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=4c61182b8c2a1101700f260cd1b23aa9 920w">
<source media="(min-width: 980px)" sizes="460px" srcset="https://i.guim.co.uk/img/media/7e5702c568d4bf828db2315243274f988b458330/31_223_567_340/master/567.png?w=460&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=fc6f2bb59d87e6ef1d8f61e6a036a348 460w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="340px" srcset="https://i.guim.co.uk/img/media/7e5702c568d4bf828db2315243274f988b458330/31_223_567_340/master/567.png?w=340&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=0305cab34548427ff03147e2bd95029a 680w">
<source media="(min-width: 740px)" sizes="340px" srcset="https://i.guim.co.uk/img/media/7e5702c568d4bf828db2315243274f988b458330/31_223_567_340/master/567.png?w=340&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=46bd304679e78a0c8c93b8d9fc3cb1bd 340w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="95vw" srcset="https://i.guim.co.uk/img/media/7e5702c568d4bf828db2315243274f988b458330/31_223_567_340/master/567.png?w=460&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=4c61182b8c2a1101700f260cd1b23aa9 920w, https://i.guim.co.uk/img/media/7e5702c568d4bf828db2315243274f988b458330/31_223_567_340/master/567.png?w=340&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=0305cab34548427ff03147e2bd95029a 680w, https://i.guim.co.uk/img/media/7e5702c568d4bf828db2315243274f988b458330/31_223_567_340/master/567.png?w=445&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=5552af4d69c9e563156237fcaab8e7e9 890w, https://i.guim.co.uk/img/media/7e5702c568d4bf828db2315243274f988b458330/31_223_567_340/master/567.png?w=605&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=21b78fe0c5b3bceb14181c8e320105a3 1210w">
<source media="(min-width: 0px)" sizes="95vw" srcset="https://i.guim.co.uk/img/media/7e5702c568d4bf828db2315243274f988b458330/31_223_567_340/master/567.png?w=460&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=fc6f2bb59d87e6ef1d8f61e6a036a348 460w, https://i.guim.co.uk/img/media/7e5702c568d4bf828db2315243274f988b458330/31_223_567_340/master/567.png?w=340&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=46bd304679e78a0c8c93b8d9fc3cb1bd 340w, https://i.guim.co.uk/img/media/7e5702c568d4bf828db2315243274f988b458330/31_223_567_340/master/567.png?w=445&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=4a49dd631cfe6ece470d8f3361151c99 445w, https://i.guim.co.uk/img/media/7e5702c568d4bf828db2315243274f988b458330/31_223_567_340/master/567.png?w=605&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=fc67afff1192b88c68580c3dc221ea2d 605w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/technology/2017/oct/12/shoe-colour-question-could-put-2015-dress-debate-in-the-shade" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Fashion</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">Shoe colour question could put 2015 dress debate in the shade</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
Debate kicks off on social media about whether picture shows a turquoise and grey trainer, or a pink and white one
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/technology/2017/oct/12/shoe-colour-question-could-put-2015-dress-debate-in-the-shade" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Shoe colour question could put 2015 dress debate in the shade</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image fc-item--has-metadata fc-item--is-commentable js-fc-item tone-feature--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-discussion-id="/p/7cak3" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/lifeandstyle/shortcuts/2017/oct/11/what-does-it-mean-when-we-talk-in-our-sleep#comments" data-link-name="feature | group-0 | card-2" data-item-visibility="all" data-test-id="facia-card" data-id="lifeandstyle/shortcuts/2017/oct/11/what-does-it-mean-when-we-talk-in-our-sleep" data-loyalty-short-url="/p/7cak3">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/870022c6037a1a8a3a3463c1c18e7ebfcf1dde37/0_190_5700_3420/master/5700.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=e9908c75bd60e0f014072bab216f6919 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/870022c6037a1a8a3a3463c1c18e7ebfcf1dde37/0_190_5700_3420/master/5700.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=7aae912c0ef98a94eeefdc266242f824 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/870022c6037a1a8a3a3463c1c18e7ebfcf1dde37/0_190_5700_3420/master/5700.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=d4332356139909d1984aed99b0085b3b 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/870022c6037a1a8a3a3463c1c18e7ebfcf1dde37/0_190_5700_3420/master/5700.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=3c98788d83f868dff173d5225cf94ab7 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/870022c6037a1a8a3a3463c1c18e7ebfcf1dde37/0_190_5700_3420/master/5700.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=25d3eeca2c72341ae8aeee22e5c1dc13 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/870022c6037a1a8a3a3463c1c18e7ebfcf1dde37/0_190_5700_3420/master/5700.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=313d1f431cce11495ee90a160832d054 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/lifeandstyle/shortcuts/2017/oct/11/what-does-it-mean-when-we-talk-in-our-sleep" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Health and wellbeing</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">What does it mean when we talk in our sleep?</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
It’s a compelling idea that people talking in their sleep might reveal their deepest secrets – but a new study suggests we mostly just say ‘no’ and use swear words
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/lifeandstyle/shortcuts/2017/oct/11/what-does-it-mean-when-we-talk-in-our-sleep" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">What does it mean when we talk in our sleep?</a>
</div>
</div> </li>
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--has-image js-fc-item tone-feature--item fc-item--list-media-mobile fc-item--standard-tablet js-snappable" data-link-name="feature | group-0 | card-3" data-item-visibility="all" data-test-id="facia-card" data-id="small-business-network/2017/oct/12/one-size-fits-all-the-designer-creating-clothes-that-grow-with-kids" data-loyalty-short-url="/p/7bfy9">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="220px" srcset="https://i.guim.co.uk/img/media/b839fd797026ebe93ec9bb1598db5690acd5b2e4/0_24_2802_1681/master/2802.jpg?w=220&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=ea449d5ca776b2c1a6249be8281ad4c2 440w">
<source media="(min-width: 980px)" sizes="220px" srcset="https://i.guim.co.uk/img/media/b839fd797026ebe93ec9bb1598db5690acd5b2e4/0_24_2802_1681/master/2802.jpg?w=220&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=c6116a3bd895e92df98ee9734a016725 220w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="160px" srcset="https://i.guim.co.uk/img/media/b839fd797026ebe93ec9bb1598db5690acd5b2e4/0_24_2802_1681/master/2802.jpg?w=160&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=9711990fa29e864e3bae1d2ff963443b 320w">
<source media="(min-width: 740px)" sizes="160px" srcset="https://i.guim.co.uk/img/media/b839fd797026ebe93ec9bb1598db5690acd5b2e4/0_24_2802_1681/master/2802.jpg?w=160&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=bc5e7158cf4ede271a19f3ef1fcf9306 160w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="127px" srcset="https://i.guim.co.uk/img/media/b839fd797026ebe93ec9bb1598db5690acd5b2e4/0_24_2802_1681/master/2802.jpg?w=127&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=f8080587c037521f64368a03ca4e8492 254w">
<source media="(min-width: 0px)" sizes="127px" srcset="https://i.guim.co.uk/img/media/b839fd797026ebe93ec9bb1598db5690acd5b2e4/0_24_2802_1681/master/2802.jpg?w=127&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=98363f086697d1c228fbc60970d37722 127w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/small-business-network/2017/oct/12/one-size-fits-all-the-designer-creating-clothes-that-grow-with-kids" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">One size fits all</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">The designer creating clothes that grow with kids</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
Winner of the James Dyson UK award, Ryan Yasin’s children’s garments stretch to fit kids aged three months to three years – offering parents a sustainable alternative to disposable clothing
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/small-business-network/2017/oct/12/one-size-fits-all-the-designer-creating-clothes-that-grow-with-kids" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">The designer creating clothes that grow with kids</a>
</div>
</div> </li>
</ul>
</div>
</div>
</div>
</section>
<section id="videos" class="fc-container fc-container--lazy-load fc-container--video js-container--lazy-load " data-link-name="container-12 | videos" data-id="6a001562-c027-43ee-a3bd-737ef2813614" data-component="videos" aria-expanded="true">
<div class="gs-container">
<div class="fc-container__inner">
<h2 class="video-title fc-container__header__title"> <a href="video" data-link-name="video-container-title videos">videos</a> </h2>
</div>
<div class="video-playlist video-playlist--start js-video-playlist" data-number-of-videos="5" data-component="video-playlist">
<div class="video-playlist__control video-playlist__control--prev js-video-playlist-prev" data-link-name="video-container-prev">
<span class="inline-chevron-left inline-icon video-playlist__icon">
<svg width="6" height="12" viewbox="0 0 6 12" class="video-playlist__icon__svg inline-chevron-left__svg inline-icon__svg">
<path d="M6 .5L5.5 0 0 5.8v.5L5.5 12l.5-.5L1.5 6 6 .5z"/>
</svg> </span>
</div>
<div class="video-playlist__control video-playlist__control--next js-video-playlist-next" data-link-name="video-container-next">
<span class="inline-chevron-right inline-icon video-playlist__icon">
<svg width="6" height="12" viewbox="-8 7 6 12" class="video-playlist__icon__svg inline-chevron-right__svg inline-icon__svg">
<path d="M-8 18.5l.5.5 5.5-5.8v-.5L-7.5 7l-.5.5 4.5 5.5-4.5 5.5z"/>
</svg> </span>
</div>
<ul class="u-unstyled video-playlist__inner js-video-playlist-inner">
<li class="video-playlist__item video-title video-title--leftcol fc-container__header__title"> <a class="video-title__link" href="video" data-link-name="video-container-title videos"> <span class="inline-guardian-video-logo inline-logo ">
<svg width="160" height="80" viewbox="0 0 160 80" class="inline-guardian-video-logo__svg inline-logo__svg">
<path fill="#676767" d="M90.3 18.4C90.3 7.5 87 5.7 83 5.7s-7.1 1.6-7.1 12.7 3.3 12.2 7.1 12.2c4-.2 7.3-1.3 7.3-12.2M75.9 60.2c-5.1 0-6.4 3.8-6.4 6.4 0 4 3.6 7.6 14 7.6 11.8 0 15.1-3.3 15.1-7.6 0-3.8-2.9-6.4-7.6-6.4H75.9zm-9.6-56C52.6 10.4 43 24.2 43 40.4c0 10.9 4.4 20.9 11.6 28v-.7c0-7.1 6.9-9.8 13.1-11.1-5.8-1.3-8.7-5.6-8.7-9.8 0-5.8 6.4-10.7 9.6-12.9l-.4-.2c-5.6-3.1-9.1-8.4-9.1-15.6-.1-5.9 2.6-10.8 7.2-13.9M123 40.6c0-16.4-10-30.7-24.2-36.7 4.7 3.1 7.6 7.8 7.8 14l.2 1.3c0 12-9.8 18.2-23.8 18.2-3.6 0-6-.2-9.1-1.1-1.3.9-2.4 2.4-2.4 4 0 2 1.8 3.6 4 3.6H95c12.2 0 18.2 4.9 18.2 15.8 0 3.6-.7 6.9-2.2 9.6 7.3-7.6 12-17.6 12-28.7"/>
<circle opacity=".8" fill="#FB0" cx="40" cy="40" r="40"/>
<path fill="#FFF" d="M120 1c21.5 0 39 17.5 39 39s-17.5 39-39 39-39-17.5-39-39S98.5 1 120 1m0-1C97.9 0 80 17.9 80 40s17.9 40 40 40 40-17.9 40-40-17.9-40-40-40zM27.3 30l-2.7 2.9v14.3l2.8 2.9h16.1V30H27.3m26.1.9l-7.4 7v4.3l7.4 7h2.1V30.9h-2.1"/>
<path class="inline-guardian-video-logo__title" fill="#FB0" d="M94.2 44.5l2-6.2-1.2-.6v-1h4.4v1l-1.2.6-3.4 9.6h-3.2l-3.3-9.6-1.2-.6v-1h6.5v1l-1.2.6 1.8 6.2zm10.8-8.1h.3v9.9l1.2.6v1h-6.1v-1l1.2-.6v-7.6l-1.3-.6v-1l4.7-.7zm.3-2.6c0 1.1-.9 2-2 2s-2-.9-2-2 .9-2 2-2 2 .9 2 2zm9 .4l-1.2-.6v-1l4.7-.7h.3V46l1.2.7v1l-4.4.5h-.3V47h-.1c-.5.6-1.4 1.2-2.8 1.2-2 0-4.5-1.3-4.5-5.6 0-4.5 2.5-6.1 5.5-6.1.6 0 1.3.1 1.8.5l-.2-2.8zm0 4.2c-.3-.2-.6-.4-1.3-.4-1.2 0-2.1 1.1-2.1 4.2 0 2.8.7 4 2.2 4 .6 0 .9-.1 1.1-.2v-7.6zm9.2 4.3c.2 2.2 1.2 3.2 3.3 3.2 1.4 0 2.2-.1 3-.4v1.1c-.5.7-2.2 1.6-4.3 1.6-3.8 0-5.8-2.1-5.8-5.9 0-3.7 2.2-5.8 5.5-5.8 3.4 0 5 1.5 5 6.2h-6.7zm-.1-1.4l3.1-.2c0-3-.5-3.5-1.4-3.5-1 .1-1.6.7-1.7 3.7zm19.7 1c0 3.8-2.3 5.9-5.7 5.9-3.4 0-5.7-2.1-5.7-5.9 0-3.8 2.3-5.9 5.7-5.9 3.4 0 5.7 2.1 5.7 5.9zm-3.9 0c0-3.7-.6-4.3-1.8-4.3-1.2 0-1.9.6-1.9 4.3 0 3.7.6 4.3 1.9 4.3 1.2.1 1.8-.6 1.8-4.3zm4.7 5.2v-3h1.6l.6 1.9c.3.2 1.2.4 1.8.4 1.1 0 1.8-.2 1.8-1.1 0-.8-.3-1.2-1.5-1.4l-1.4-.3c-2.1-.5-3-2.1-3-3.8 0-2.1 1.5-3.7 4.8-3.7 1.3 0 2.7.2 3.5.6v2.8h-1.6l-.5-1.5c-.3-.1-1-.3-1.6-.3-.9 0-1.5.4-1.5 1.1 0 .7.3 1.1 1.5 1.3l1.3.3c2.2.5 3 1.9 3 3.6 0 2.3-1.5 3.9-5 3.9-1.1-.1-2.7-.3-3.8-.8z"/>
</svg> </span> </a> </li>
<li class="video-playlist__item js-video-playlist-item-0 video-playlist__item--active video-playlist__item--first">
<div data-media-atom-id="64ab6f41-0f88-467d-91ae-6a995922e18e" class="u-responsive-ratio u-responsive-ratio--hd youtube-media-atom">
<iframe class="youtube-media-atom__iframe" id="youtube-Q3Vxq41OP7w" width="100%" height="100%" src="https://www.youtube.com/embed/Q3Vxq41OP7w?enablejsapi=1&amp;rel=0&amp;showinfo=0&amp;origin=https://www.theguardian.com" frameborder="0" allowfullscreen> </iframe>
<div class="video-overlay">
<div class="video-overlay__headline">
<h1 class="fc-item__title fc-item__title--quoted"><a href="https://www.theguardian.com/world/video/2017/oct/12/i-am-catalan-the-referendum-was-like-flipping-a-coin-it-didnt-make-sense-video" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">I am Catalan</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-video-icon inline-icon ">
<svg width="36" height="23" viewbox="0 0 36 23" class="inline-video-icon__svg inline-icon__svg">
<path d="M3.2 0L0 3.3v16.4L3.3 23H22V0H3.2m30.4 1L25 9v5l8.6 8H36V1h-2.4"/>
</svg> </span> <span class="inline-quote inline-icon ">
<svg width="17" height="10" viewbox="0 0 33 20" class="inline-quote__svg inline-icon__svg">
<path d="M9.002 20c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053A9.968 9.968 0 0 1 4.001 6.5C4.064 2.97 7.414.937 11.003 1l-1-1C3.98 0 .098 4.447.002 10.006c-.097 5.557 3.35 9.892 9 9.994zm17 0c3.85.068 6.932-3.104 7-6.994.068-3.892-3.15-6.937-7-7.006-2.016-.036-3.59.694-4.888 2.053a9.968 9.968 0 0 1-.113-1.553c.063-3.53 3.413-5.563 7.002-5.5l-1-1c-6.022 0-9.904 4.447-10 10.006-.097 5.557 3.35 9.892 9 9.994z"/>
</svg> </span> <span class="js-headline-text">The referendum was like flipping a coin, it didn’t make sense</span></span> </a></h1>
</div>
<span class="video-overlay__duration"> 2:39 </span>
</div>
<a href="https://www.theguardian.com/world/video/2017/oct/12/i-am-catalan-the-referendum-was-like-flipping-a-coin-it-didnt-make-sense-video" class="video-container-overlay-link"></a>
<div class="vjs-big-play-button youtube-media-atom__overlay" style="background-image: url(https://i.guim.co.uk/img/media/7b5a25b5002b47430c989a886bf4fc3ae99aabc2/0_0_1920_1080/1920.jpg?w=700&amp;h=394&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=14440c5db361eeed6f031742ff9f3a12)">
<div class="youtube-media-atom__play-button vjs-control-text">
Play Video
</div>
</div>
</div> </li>
<li class="video-playlist__item js-video-playlist-item-1 ">
<div data-media-atom-id="e793be37-c1fc-4f77-a2db-c6f570556747" class="u-responsive-ratio u-responsive-ratio--hd youtube-media-atom">
<iframe class="youtube-media-atom__iframe" id="youtube-VT-SdYpw9O8" width="100%" height="100%" src="https://www.youtube.com/embed/VT-SdYpw9O8?enablejsapi=1&amp;rel=0&amp;showinfo=0&amp;origin=https://www.theguardian.com" frameborder="0" allowfullscreen> </iframe>
<div class="video-overlay">
<div class="video-overlay__headline">
<h1 class="fc-item__title"><a href="https://www.theguardian.com/global-development/video/2017/oct/12/colombia-trans-life-transgender-they-attack-us-for-being-who-we-are" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">'They attack us just for being who we are'</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-video-icon inline-icon ">
<svg width="36" height="23" viewbox="0 0 36 23" class="inline-video-icon__svg inline-icon__svg">
<path d="M3.2 0L0 3.3v16.4L3.3 23H22V0H3.2m30.4 1L25 9v5l8.6 8H36V1h-2.4"/>
</svg> </span> <span class="js-headline-text">Trans life in Colombia</span></span> </a></h1>
</div>
<span class="video-overlay__duration"> 1:38 </span>
</div>
<a href="https://www.theguardian.com/global-development/video/2017/oct/12/colombia-trans-life-transgender-they-attack-us-for-being-who-we-are" class="video-container-overlay-link"></a>
<div class="vjs-big-play-button youtube-media-atom__overlay" style="background-image: url(https://i.guim.co.uk/img/media/fb3cc977898b92ca8ad8de556b33d29ea0b26bab/0_504_6720_3780/6720.jpg?w=700&amp;h=394&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=9ada2a4faa901da75887ff2cd3ae2224)">
<div class="youtube-media-atom__play-button vjs-control-text">
Play Video
</div>
</div>
</div> </li>
<li class="video-playlist__item js-video-playlist-item-2 ">
<div data-media-atom-id="61cedd55-18b8-43c7-9514-ac84ecd47009" class="u-responsive-ratio u-responsive-ratio--hd youtube-media-atom">
<iframe class="youtube-media-atom__iframe" id="youtube-cKN5bMTHyMM" width="100%" height="100%" src="https://www.youtube.com/embed/cKN5bMTHyMM?enablejsapi=1&amp;rel=0&amp;showinfo=0&amp;origin=https://www.theguardian.com" frameborder="0" allowfullscreen> </iframe>
<div class="video-overlay">
<div class="video-overlay__headline">
<h1 class="fc-item__title"><a href="https://www.theguardian.com/music/video/2017/oct/11/eminem-lambasts-trump-in-freestyle-rap-video" class="fc-item__link" data-link-name="article"> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-video-icon inline-icon ">
<svg width="36" height="23" viewbox="0 0 36 23" class="inline-video-icon__svg inline-icon__svg">
<path d="M3.2 0L0 3.3v16.4L3.3 23H22V0H3.2m30.4 1L25 9v5l8.6 8H36V1h-2.4"/>
</svg> </span> <span class="js-headline-text">Eminem lambasts Donald Trump in freestyle rap</span></span> </a></h1>
</div>
<span class="video-overlay__duration"> 4:29 </span>
</div>
<a href="https://www.theguardian.com/music/video/2017/oct/11/eminem-lambasts-trump-in-freestyle-rap-video" class="video-container-overlay-link"></a>
<div class="vjs-big-play-button youtube-media-atom__overlay" style="background-image: url(https://i.guim.co.uk/img/media/1d8e30c7e756e5617852c01bc98d6ac832a3590b/7_0_1890_1063/1890.png?w=700&amp;h=394&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=81a5618b9accf303568deab4ae4fea3e)">
<div class="youtube-media-atom__play-button vjs-control-text">
Play Video
</div>
</div>
</div> </li>
<li class="video-playlist__item js-video-playlist-item-3 ">
<div data-media-atom-id="0cb27db3-4a67-4c4b-8e15-b0b608325088" class="u-responsive-ratio u-responsive-ratio--hd youtube-media-atom">
<iframe class="youtube-media-atom__iframe" id="youtube-lN8-CFoXO2E" width="100%" height="100%" src="https://www.youtube.com/embed/lN8-CFoXO2E?enablejsapi=1&amp;rel=0&amp;showinfo=0&amp;origin=https://www.theguardian.com" frameborder="0" allowfullscreen> </iframe>
<div class="video-overlay">
<div class="video-overlay__headline">
<h1 class="fc-item__title"><a href="https://www.theguardian.com/world/video/2017/oct/11/i-am-catalan-its-about-building-a-new-society-for-all-video" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">I am Catalan</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-video-icon inline-icon ">
<svg width="36" height="23" viewbox="0 0 36 23" class="inline-video-icon__svg inline-icon__svg">
<path d="M3.2 0L0 3.3v16.4L3.3 23H22V0H3.2m30.4 1L25 9v5l8.6 8H36V1h-2.4"/>
</svg> </span> <span class="js-headline-text">'It's about building a new society for all'</span></span> </a></h1>
</div>
<span class="video-overlay__duration"> 2:10 </span>
</div>
<a href="https://www.theguardian.com/world/video/2017/oct/11/i-am-catalan-its-about-building-a-new-society-for-all-video" class="video-container-overlay-link"></a>
<div class="vjs-big-play-button youtube-media-atom__overlay" style="background-image: url(https://i.guim.co.uk/img/media/23d389b07d48e53e09ea9ee8c515a893eadb123c/0_0_1920_1080/1920.jpg?w=700&amp;h=394&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=bfb5cd7f74afdc3ef300484bc09f94d9)">
<div class="youtube-media-atom__play-button vjs-control-text">
Play Video
</div>
</div>
</div> </li>
<li class="video-playlist__item js-video-playlist-item-4 ">
<div data-media-atom-id="a7c29564-af8c-4f5d-bd9d-f5d1ec998610" class="u-responsive-ratio u-responsive-ratio--hd youtube-media-atom">
<iframe class="youtube-media-atom__iframe" id="youtube-rzUY4dszxqo" width="100%" height="100%" src="https://www.youtube.com/embed/rzUY4dszxqo?enablejsapi=1&amp;rel=0&amp;showinfo=0&amp;origin=https://www.theguardian.com" frameborder="0" allowfullscreen> </iframe>
<div class="video-overlay">
<div class="video-overlay__headline">
<h1 class="fc-item__title"><a href="https://www.theguardian.com/us-news/video/2017/oct/11/sheriffs-deputy-drives-through-raging-blaze-in-california-video" class="fc-item__link" data-link-name="article"> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-video-icon inline-icon ">
<svg width="36" height="23" viewbox="0 0 36 23" class="inline-video-icon__svg inline-icon__svg">
<path d="M3.2 0L0 3.3v16.4L3.3 23H22V0H3.2m30.4 1L25 9v5l8.6 8H36V1h-2.4"/>
</svg> </span> <span class="js-headline-text">Sheriff’s deputy drives through raging blaze in California</span></span> </a></h1>
</div>
<span class="video-overlay__duration"> 0:13 </span>
</div>
<a href="https://www.theguardian.com/us-news/video/2017/oct/11/sheriffs-deputy-drives-through-raging-blaze-in-california-video" class="video-container-overlay-link"></a>
<div class="vjs-big-play-button youtube-media-atom__overlay" style="background-image: url(https://i.guim.co.uk/img/media/e8233d551dc4b579afab166492fdbf02d8cfe35c/0_0_1920_1080/1920.jpg?w=700&amp;h=394&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=5ea87a01eeef83dc1beadf5ab0f2e98a)">
<div class="youtube-media-atom__play-button vjs-control-text">
Play Video
</div>
</div>
</div> </li>
<li class="video-playlist__item js-video-playlist-item-5 ">
<div data-media-atom-id="7daac35f-e259-4d48-91b7-c116e6e9ba8d" class="u-responsive-ratio u-responsive-ratio--hd youtube-media-atom">
<iframe class="youtube-media-atom__iframe" id="youtube-o5xZVLjxqco" width="100%" height="100%" src="https://www.youtube.com/embed/o5xZVLjxqco?enablejsapi=1&amp;rel=0&amp;showinfo=0&amp;origin=https://www.theguardian.com" frameborder="0" allowfullscreen> </iframe>
<div class="video-overlay">
<div class="video-overlay__headline">
<h1 class="fc-item__title"><a href="https://www.theguardian.com/politics/video/2017/oct/10/mhairi-black-snp-disappointed-in-jeremy-corbyn-video" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Mhairi Black</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-video-icon inline-icon ">
<svg width="36" height="23" viewbox="0 0 36 23" class="inline-video-icon__svg inline-icon__svg">
<path d="M3.2 0L0 3.3v16.4L3.3 23H22V0H3.2m30.4 1L25 9v5l8.6 8H36V1h-2.4"/>
</svg> </span> <span class="js-headline-text">'I am so disappointed in Jeremy Corbyn'</span></span> </a></h1>
</div>
<span class="video-overlay__duration"> 3:09 </span>
</div>
<a href="https://www.theguardian.com/politics/video/2017/oct/10/mhairi-black-snp-disappointed-in-jeremy-corbyn-video" class="video-container-overlay-link"></a>
<div class="vjs-big-play-button youtube-media-atom__overlay" style="background-image: url(https://i.guim.co.uk/img/media/ae600887bd01beb98fb20c00c1cd7a079a9a94b4/0_123_4048_2277/4048.jpg?w=700&amp;h=394&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=47df7445f0d2e866dbca1b7e1004008e)">
<div class="youtube-media-atom__play-button vjs-control-text">
Play Video
</div>
</div>
</div> </li>
</ul>
</div>
</div>
</section>
<section class="fc-container__mpu--mobile">
<div id="dfp-ad--inline5--mobile" class="js-ad-slot ad-slot ad-slot--inline5 ad-slot--container-inline ad-slot--mobile mobile-only" data-link-name="ad slot inline5" data-name="inline5" data-mobile="1,1|2,2|300,250|fluid">
</div>
</section>
<section id="the-big-picture" class="fc-container fc-container--lazy-load fc-container--will-have-toggle js-container--lazy-load js-container--toggle " data-link-name="container-13 | the-big-picture" data-id="16334b89-a4b1-4db8-8f39-7a364326bc0a" data-component="the-big-picture" aria-expanded="true">
<div class="fc-container__inner">
<div class="fc-container__header
                js-container__header
                ">
<div class="fc-container__header__title">
<span tabindex="0">the big picture</span>
</div>
</div>
<div class="fc-container--rolled-up-hide fc-container__body" data-title="the big picture" data-id="16334b89-a4b1-4db8-8f39-7a364326bc0a">
<div class="fc-slice-wrapper">
<ul class="u-unstyled l-row  l-row--cols-1 fc-slice fc-slice--f">
<li class="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link">
<div class="fc-item fc-item--gallery fc-item--has-image fc-item--has-metadata fc-item--is-commentable fc-item--is-media-link js-fc-item tone-media--item fc-item--standard-mobile fc-item--full-media-75-tablet js-snappable" data-discussion-id="/p/7cef8" data-discussion-closed="false" data-discussion-url="https://www.theguardian.com/news/gallery/2017/oct/12/elizabeth-i-and-sophia-robot-pick--thursdays-photos#comments" data-link-name="media | group-0 | card-1" data-item-visibility="all" data-test-id="facia-card" data-id="news/gallery/2017/oct/12/elizabeth-i-and-sophia-robot-pick--thursdays-photos" data-loyalty-short-url="/p/7cef8">
<div class="fc-item__container">
<div class="fc-item__media-wrapper">
<div class="fc-item__image-container u-responsive-ratio ">
<picture>
<!--[if IE 9]><video style="display: none;"><![endif]-->
<source media="(min-width: 980px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 980px) and (min-resolution: 120dpi)" sizes="700px" srcset="https://i.guim.co.uk/img/media/7e6995f218aa08e119f50e2fe4c3667cd972bd34/4_375_3333_2001/master/3333.jpg?w=700&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=20990e42ae0582dc338f718cb7876f0d 1400w">
<source media="(min-width: 980px)" sizes="700px" srcset="https://i.guim.co.uk/img/media/7e6995f218aa08e119f50e2fe4c3667cd972bd34/4_375_3333_2001/master/3333.jpg?w=700&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=bd91a94a4714df3f462fa24904936a02 700w">
<source media="(min-width: 740px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 740px) and (min-resolution: 120dpi)" sizes="520px" srcset="https://i.guim.co.uk/img/media/7e6995f218aa08e119f50e2fe4c3667cd972bd34/4_375_3333_2001/master/3333.jpg?w=520&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=bbeb7cc0e6916d7cb8441db2c059022e 1040w">
<source media="(min-width: 740px)" sizes="520px" srcset="https://i.guim.co.uk/img/media/7e6995f218aa08e119f50e2fe4c3667cd972bd34/4_375_3333_2001/master/3333.jpg?w=520&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=2331972013605b4fd180e40cc90f3a85 520w">
<source media="(min-width: 0px) and (-webkit-min-device-pixel-ratio: 1.25), (min-width: 0px) and (min-resolution: 120dpi)" sizes="95vw" srcset="https://i.guim.co.uk/img/media/7e6995f218aa08e119f50e2fe4c3667cd972bd34/4_375_3333_2001/master/3333.jpg?w=520&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=bbeb7cc0e6916d7cb8441db2c059022e 1040w, https://i.guim.co.uk/img/media/7e6995f218aa08e119f50e2fe4c3667cd972bd34/4_375_3333_2001/master/3333.jpg?w=445&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=90240e92cb09fa458c17493ca8d680a3 890w, https://i.guim.co.uk/img/media/7e6995f218aa08e119f50e2fe4c3667cd972bd34/4_375_3333_2001/master/3333.jpg?w=605&amp;q=20&amp;auto=format&amp;usm=12&amp;fit=max&amp;dpr=2&amp;s=06846fcc6f63be70cec166e57456404a 1210w">
<source media="(min-width: 0px)" sizes="95vw" srcset="https://i.guim.co.uk/img/media/7e6995f218aa08e119f50e2fe4c3667cd972bd34/4_375_3333_2001/master/3333.jpg?w=520&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=2331972013605b4fd180e40cc90f3a85 520w, https://i.guim.co.uk/img/media/7e6995f218aa08e119f50e2fe4c3667cd972bd34/4_375_3333_2001/master/3333.jpg?w=445&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=9349f6bf6ab8310e74c803ebcd589f77 445w, https://i.guim.co.uk/img/media/7e6995f218aa08e119f50e2fe4c3667cd972bd34/4_375_3333_2001/master/3333.jpg?w=605&amp;q=55&amp;auto=format&amp;usm=12&amp;fit=max&amp;s=373b736700a7bfd2538a161980ffb796 605w">
<!--[if IE 9]></video><![endif]-->
<img class="responsive-img" alt="">
</picture>
</div>
</div>
<div class="fc-item__content">
<div class="fc-item__header">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/news/gallery/2017/oct/12/elizabeth-i-and-sophia-robot-pick--thursdays-photos" class="fc-item__link" data-link-name="article"><span class="fc-item__kicker">Best photographs of the day</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="inline-camera inline-icon ">
<svg width="18" height="13" viewbox="0 0 18 13" class="inline-camera__svg inline-icon__svg">
<path d="M18 3.5v8L16.5 13h-15L0 11.5v-8L1.5 2H5l2-2h4l2 2h3.5L18 3.5zM9 11c1.9 0 3.5-1.6 3.5-3.5S10.9 4 9 4 5.5 5.6 5.5 7.5 7.1 11 9 11z"/>
</svg> </span> <span class="js-headline-text">Elizabeth I and Sophia the robot</span></span> </a></h2>
</div>
<div class="fc-item__standfirst">
The Guardian’s picture editors bring you photo highlights from around the world, including Hispanic Day, Elizabeth I and a daredevil climber
</div>
<aside class="fc-item__meta js-item__meta">
</aside>
</div>
<a href="https://www.theguardian.com/news/gallery/2017/oct/12/elizabeth-i-and-sophia-robot-pick--thursdays-photos" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">Elizabeth I and Sophia the robot</a>
</div>
</div> </li>
</ul>
</div>
</div>
</div>
</section>
<section id="most-viewed-in-world-news" class="fc-container fc-container--lazy-load fc-container--will-have-toggle js-container--lazy-load js-container--toggle " data-link-name="container-14 | most-viewed-in-world-news" data-id="558b-3b8b-3485-d9ff" data-component="most-viewed-in-world-news" aria-expanded="true">
<div class="fc-container__inner">
<div class="fc-container__header js-container__header">
<div class="fc-container__header__title">
<span tabindex="0"> most viewed </span>
</div>
</div>
<div class="fc-container__body fc-container--rolled-up-hide js-popular-trails">
<div id="popular-trails" class="fc-slice fc-slice--popular" data-link-name="most popular Test" data-test-id="popular-in">
<div class="tabs tabs--mostpop u-cf">
<ol class="tabs__container js-tabs" id="js-popular-tabs" role="tablist">
<li class="tabs__tab tabs__tab--selected tone-colour tone-accent-border" role="tab" id="tabs-popular-1-tab" aria-selected="true" aria-controls="tabs-popular-1"> <a href="#tabs-popular-1" data-link-name="tab 1 most viewed in world news"><span class="u-h">Most viewed </span>most viewed in world news</a> </li>
<li class="tabs__tab" role="tab" id="tabs-popular-2-tab" aria-controls="tabs-popular-2"> <a href="#tabs-popular-2" data-link-name="tab 2 across the guardian"><span class="u-h">Most viewed </span>across the guardian</a> </li>
</ol>
<div class="tabs__content js-tabs-content">
<div id="tabs-popular-1" class="js-tab-1  tabs__pane u-cf" role="tabpanel" aria-labelledby="tabs-popular-1-tab" data-link-name="most viewed in world news" data-link-context="most-read/most viewed">
<ul class="u-unstyled headline-list headline-list--large headline-column headline-column--tablet headline-column--desktop">
<li class="headline-list__item headline-column__item headline-column--tablet__item headline-column--desktop__item tone-news--most-popular">
<div class="headline-list__link" data-link-name="1 | text">
<p class="headline-list__count">1</p>
<div class="headline-list__text">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/pakistan-rescues-canadian-american-family-hostages-haqqani" class="fc-item__link" data-link-name="article"> <span class="headline-list__body fc-item__headline"> <span class="js-headline-text">Canadian-American family freed after five years as captives in Afghanistan</span></span> </a></h2>
</div>
</div> </li>
<li class="headline-list__item headline-column__item headline-column--tablet__item headline-column--desktop__item tone-news--most-popular">
<div class="headline-list__link" data-link-name="2 | text">
<p class="headline-list__count">2</p>
<div class="headline-list__text">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/us-withdraw-unesco-december-united-nations" class="fc-item__link" data-link-name="article"> <span class="headline-list__body fc-item__headline"> <span class="js-headline-text">Unesco: Israel joins US in quitting UN heritage agency over 'anti-Israel bias'</span></span> </a></h2>
</div>
</div> </li>
<li class="headline-list__item headline-column__item headline-column--tablet__item headline-column--desktop__item tone-news--most-popular">
<div class="headline-list__link" data-link-name="3 | text">
<p class="headline-list__count">3</p>
<div class="headline-list__text">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/sally-jones-the-uk-punk-singer-who-became-isiss-white-widow" class="fc-item__link" data-link-name="article"> <span class="headline-list__body fc-item__headline"> <span class="js-headline-text">Sally Jones: UK punk singer who became leading Isis recruiter</span></span> </a></h2>
</div>
</div> </li>
<li class="headline-list__item headline-column__item headline-column--tablet__item headline-column--desktop__item tone-news--most-popular">
<div class="headline-list__link" data-link-name="4 | text">
<p class="headline-list__count">4</p>
<div class="headline-list__text">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/trump-warns-its-possible-the-us-will-drop-out-of-nafta" class="fc-item__link" data-link-name="article"> <span class="headline-list__body fc-item__headline"> <span class="js-headline-text">Trump warns it's 'possible' the US will drop out of Nafta</span></span> </a></h2>
</div>
</div> </li>
<li class="headline-list__item headline-column__item headline-column--tablet__item headline-column--desktop__item tone-news--most-popular">
<div class="headline-list__link" data-link-name="5 | text">
<p class="headline-list__count">5</p>
<div class="headline-list__text">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/man-solves-mystery-of-1930s-sports-car-buried-on-salisbury-plain" class="fc-item__link" data-link-name="article"> <span class="headline-list__body fc-item__headline"> <span class="js-headline-text">Man solves mystery of 1930s sports car buried on Salisbury Plain</span></span> </a></h2>
</div>
</div> </li>
<li class="headline-list__item headline-column__item headline-column--tablet__item headline-column--desktop__item tone-news--most-popular">
<div class="headline-list__link" data-link-name="6 | text">
<p class="headline-list__count">6</p>
<div class="headline-list__text">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/cuba-mass-hysteria-sonic-attacks-neurologists" class="fc-item__link" data-link-name="article"> <span class="headline-list__body fc-item__headline"> <span class="js-headline-text">Mass hysteria may explain 'sonic attacks' in Cuba, say top neurologists</span></span> </a></h2>
</div>
</div> </li>
<li class="headline-list__item headline-column__item headline-column--tablet__item headline-column--desktop__item tone-feature--most-popular">
<div class="headline-list__link" data-link-name="7 | text">
<p class="headline-list__count">7</p>
<div class="headline-list__text">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/its-become-a-monster-is-irans-revolutionary-guard-a-terror-group" class="fc-item__link" data-link-name="article"> <span class="headline-list__body fc-item__headline"> <span class="js-headline-text">'It's become a monster': is Iran's revolutionary guard a terror group?</span></span> </a></h2>
</div>
</div> </li>
<li class="headline-list__item headline-column__item headline-column--tablet__item headline-column--desktop__item tone-feature--most-popular">
<div class="headline-list__link" data-link-name="8 | text">
<p class="headline-list__count">8</p>
<div class="headline-list__text">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/my-friend-kim-wall-journalist" class="fc-item__link" data-link-name="article"> <span class="headline-list__body fc-item__headline"> <span class="js-headline-text">Kim Wall was born to tell stories. I miss my friend's light, and her love</span></span> </a></h2>
</div>
</div> </li>
<li class="headline-list__item headline-column__item headline-column--tablet__item headline-column--desktop__item tone-news--most-popular">
<div class="headline-list__link" data-link-name="9 | text">
<p class="headline-list__count">9</p>
<div class="headline-list__text">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/white-widow-sally-jones-was-fleeing-raqqa-as-isiss-capital-fell" class="fc-item__link" data-link-name="article"> <span class="headline-list__body fc-item__headline"> <span class="js-headline-text">Sally Jones was fleeing Raqqa as Isis's capital fell</span></span> </a></h2>
</div>
</div> </li>
<li class="headline-list__item headline-column__item headline-column--tablet__item headline-column--desktop__item tone-news--most-popular">
<div class="headline-list__link" data-link-name="10 | text">
<p class="headline-list__count">10</p>
<div class="headline-list__text">
<h2 class="fc-item__title"><a href="https://www.theguardian.com/world/2017/oct/12/british-isis-member-sally-jones-white-widow-killed-airstrike-son-islamic-state-syria" class="fc-item__link" data-link-name="article"> <span class="headline-list__body fc-item__headline"> <span class="js-headline-text">British Isis member Sally Jones 'killed in airstrike with 12-year-old son'</span></span> </a></h2>
</div>
</div> </li>
</ul>
</div>
<div id="tabs-popular-2" class="js-tab-2 modern-hidden tabs__pane u-cf" role="tabpanel" aria-labelledby="tabs-popular-2-tab" data-link-name="across the guardian" data-link-context="most-read/most viewed">
<ul class="u-unstyled headline-list headline-list--large headline-column headline-column--tablet headline-column--desktop">
</ul>
</div>
<div class="fc-slice__popular-mpu fc-slice__item--mpu-candidate">
<div id="dfp-ad--inline3" class="js-ad-slot ad-slot ad-slot--inline3 ad-slot--container-inline hide-until-tablet" data-link-name="ad slot inline3" data-name="inline3" data-mobile="1,1|2,2|300,250|fluid">
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</section>
<section class="fc-container__mpu--mobile">
<div id="dfp-ad--inline6--mobile" class="js-ad-slot ad-slot ad-slot--inline6 ad-slot--container-inline ad-slot--mobile mobile-only" data-link-name="ad slot inline6" data-name="inline6" data-mobile="1,1|2,2|300,250|fluid">
</div>
</section>
<script data-schema="ItemList" type="application/ld+json">
                            {"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"https://www.theguardian.com/film/2017/oct/12/harvey-weinstein-nypd-and-london-police-investigating-allegations"},{"@type":"ListItem","position":1,"url":"https://www.theguardian.com/world/2017/oct/12/us-withdraw-unesco-december-united-nations"},{"@type":"ListItem","position":2,"url":"https://www.theguardian.com/politics/2017/oct/12/brexit-talks-at-disturbing-deadlock-over-divorce-bill-says-eu-negotiator"},{"@type":"ListItem","position":3,"url":"https://www.theguardian.com/world/2017/oct/12/cuba-mass-hysteria-sonic-attacks-neurologists"},{"@type":"ListItem","position":4,"url":"https://www.theguardian.com/us-news/2017/oct/12/trump-sabotage-obamacare-executive-order"},{"@type":"ListItem","position":5,"url":"https://www.theguardian.com/science/2017/oct/12/astronomers-find-half-of-the-missing-matter-in-the-universe"},{"@type":"ListItem","position":6,"url":"https://www.theguardian.com/us-news/2017/oct/12/trump-criticises-puerto-rico-hurricane-aid-cannot-go-on-forever"},{"@type":"ListItem","position":7,"url":"https://www.theguardian.com/world/2017/oct/12/pakistan-rescues-canadian-american-family-hostages-haqqani"},{"@type":"ListItem","position":8,"url":"https://www.theguardian.com/global-development/2017/oct/12/yemen-cholera-outbreak-worst-in-history-1-million-cases-by-end-of-year"},{"@type":"ListItem","position":9,"url":"https://www.theguardian.com/world/2017/oct/12/catalan-president-accuses-mariano-rajoy-of-ignoring-call-for-talks-carles-puigdemont"},{"@type":"ListItem","position":10,"url":"https://www.theguardian.com/uk-news/2017/oct/12/paramedics-save-man-after-whole-fish-jumps-down-throat"}],"@type":"ItemList","@context":"http://schema.org"}},{"@type":"ListItem","position":1,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"https://www.theguardian.com/world/2017/oct/12/its-become-a-monster-is-irans-revolutionary-guard-a-terror-group"},{"@type":"ListItem","position":1,"url":"https://www.theguardian.com/commentisfree/2017/oct/12/banning-rose-mcgowan-shows-nothings-changed-twitter-weinstein"},{"@type":"ListItem","position":2,"url":"https://www.theguardian.com/world/2017/oct/12/sally-jones-the-uk-punk-singer-who-became-isiss-white-widow"},{"@type":"ListItem","position":3,"url":"https://www.theguardian.com/world/2017/oct/12/kyrgyzstan-set-for-freest-and-fairest-election-in-central-asian-history"},{"@type":"ListItem","position":4,"url":"https://www.theguardian.com/world/2017/oct/12/spanish-ex-monk-mission-build-own-cathedral-justo-gallego"},{"@type":"ListItem","position":5,"url":"https://www.theguardian.com/tv-and-radio/2017/oct/12/mindhunter-jonathan-groff-david-fincher-serial-killer-gay-hollywood-frozen-hamilton"},{"@type":"ListItem","position":6,"url":"https://www.theguardian.com/film/2017/oct/12/the-snowman-review-michael-fassbender-tomas-alfredson-jo-nesbo"},{"@type":"ListItem","position":7,"url":"https://www.theguardian.com/technology/2017/oct/12/apple-id-iphone-password-demands-security-flaw-phishing-attack-fake-sign-in-request"}],"@type":"ItemList","@context":"http://schema.org"}},{"@type":"ListItem","position":2,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"https://www.theguardian.com/football/2017/oct/12/psg-chairman-nasser-al-khelaifi-accused-world-cup-bribery"},{"@type":"ListItem","position":1,"url":"https://www.theguardian.com/sport/blog/2017/oct/12/aaron-judge-mlb-new-york-yankees-cleveland-indians"},{"@type":"ListItem","position":2,"url":"https://www.theguardian.com/sport/2017/oct/12/european-rugby-champions-cup-2017-18-pool-by-pool-guide"},{"@type":"ListItem","position":3,"url":"https://www.theguardian.com/football/blog/2017/oct/12/jurgen-klopp-liverpool-how-much-progress-manchester-united"},{"@type":"ListItem","position":4,"url":"https://www.theguardian.com/football/audio/2017/oct/12/viking-claps-for-iceland-golf-claps-for-the-us-football-weekly-extra"},{"@type":"ListItem","position":5,"url":"https://www.theguardian.com/sport/2017/oct/13/pat-cummins-interview-australia-ashes"},{"@type":"ListItem","position":6,"url":"https://www.theguardian.com/football/blog/2017/oct/12/jupp-heynckes-bayern-munich-roy-hodgson-old-managers"},{"@type":"ListItem","position":7,"url":"https://www.theguardian.com/football/2017/oct/12/altinordu-dominate-turkish-football-homegrown-players"},{"@type":"ListItem","position":8,"url":"https://www.theguardian.com/football/blog/2017/oct/12/the-forgotten-story-of-the-colourful-xi-tragedy"},{"@type":"ListItem","position":9,"url":"https://www.theguardian.com/football/2017/oct/12/gordon-strachan-to-leave-scotland-job-world-cup"},{"@type":"ListItem","position":10,"url":"https://www.theguardian.com/sport/2017/oct/12/world-rugby-cautions-against-link-between-premiership-injuries-and-law-changes-rugby-union"},{"@type":"ListItem","position":11,"url":"https://www.theguardian.com/football/2017/oct/12/arsenal-may-sell-mesut-ozil-alexis-sanchez-january-arsene-wenger"},{"@type":"ListItem","position":12,"url":"https://www.theguardian.com/football/copa90/2017/oct/12/oscar-football-money-china-shanghai"},{"@type":"ListItem","position":13,"url":"https://www.theguardian.com/sport/blog/2017/oct/12/saracens-scarlets-european-champions-cup"}],"@type":"ItemList","@context":"http://schema.org"}},{"@type":"ListItem","position":3,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"snap/1507288114165"}],"@type":"ItemList","@context":"http://schema.org"}},{"@type":"ListItem","position":4,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"https://www.theguardian.com/commentisfree/2017/oct/12/britain-donald-trump-hatred-theresa-may-state-visit-protests"},{"@type":"ListItem","position":1,"url":"https://www.theguardian.com/politics/2017/oct/12/barniers-body-language-reveals-futility-and-deadlock-at-brexit-talks"},{"@type":"ListItem","position":2,"url":"https://www.theguardian.com/commentisfree/2017/oct/12/espn-jemele-hill-angry-black-woman-suspension-nfl"},{"@type":"ListItem","position":3,"url":"https://www.theguardian.com/commentisfree/2017/oct/12/what-to-say-somebody-miscarried-loss-baby"},{"@type":"ListItem","position":4,"url":"https://www.theguardian.com/commentisfree/2017/oct/12/torture-survivors-uk-detention-centres-home-office-high-court-ruling"}],"@type":"ItemList","@context":"http://schema.org"}},{"@type":"ListItem","position":5,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"https://www.theguardian.com/world/2017/oct/12/trump-warns-its-possible-the-us-will-drop-out-of-nafta"},{"@type":"ListItem","position":1,"url":"https://www.theguardian.com/world/2017/oct/12/kenya-bans-opposition-protests-as-election-crisis-deepens"},{"@type":"ListItem","position":2,"url":"https://www.theguardian.com/world/2017/oct/12/south-africa-judge-rules-police-murdered-anti-apartheid-activist-in-1971"},{"@type":"ListItem","position":3,"url":"https://www.theguardian.com/world/2017/oct/12/top-un-official-to-leave-myanmar-amid-criticism-rohingya-approach"},{"@type":"ListItem","position":4,"url":"https://www.theguardian.com/world/2017/oct/12/hamas-claims-deal-agreed-fatah-control-gaza-strip"},{"@type":"ListItem","position":5,"url":"https://www.theguardian.com/us-news/2017/oct/12/democrats-ban-proposal-ammunition-magazines-las-vegas"},{"@type":"ListItem","position":6,"url":"https://www.theguardian.com/world/2017/oct/12/philippines-rodrigo-duterte-police-war-drugs"},{"@type":"ListItem","position":7,"url":"https://www.theguardian.com/global-development/2017/oct/12/myanmar-mass-graves-mystery-surrounds-deaths-of-hindu-villagers-dirty-tricks-rohingya"},{"@type":"ListItem","position":8,"url":"https://www.theguardian.com/technology/2017/oct/12/bitcoin-price-5000-cryptocurrency-gold-bubble"},{"@type":"ListItem","position":9,"url":"https://www.theguardian.com/us-news/2017/oct/11/california-fires-wine-country-death-toll-napa-valley"},{"@type":"ListItem","position":10,"url":"https://www.theguardian.com/business/2017/oct/12/kobe-steel-scandal-car-general-motors-auto-train-aircraft"},{"@type":"ListItem","position":11,"url":"https://www.theguardian.com/lifeandstyle/2017/oct/12/italian-woman-sick-pay-leave-time-off-look-after-ill-dog"},{"@type":"ListItem","position":12,"url":"https://www.theguardian.com/environment/2017/oct/12/australian-desert-reaches-peak-budgie-as-thousands-dazzle-wildlife-photographer"},{"@type":"ListItem","position":13,"url":"https://www.theguardian.com/world/2017/oct/11/spanish-government-to-hold-crisis-talks-on-catalan-independence"},{"@type":"ListItem","position":14,"url":"https://www.theguardian.com/us-news/2017/oct/12/florida-puerto-rican-influx-hurricane-maria"},{"@type":"ListItem","position":15,"url":"https://www.theguardian.com/environment/2017/oct/12/fossil-fuels-win-billions-in-public-money-after-paris-climate-deal-angry-campaigners-claim"},{"@type":"ListItem","position":16,"url":"https://www.theguardian.com/world/2017/oct/11/rohingya-refugees-myanmar-aung-san-suu-kyi-un-report"},{"@type":"ListItem","position":17,"url":"https://www.theguardian.com/world/2017/oct/12/hong-kong-chief-implies-china-is-responsible-for-barring-british-activist"},{"@type":"ListItem","position":18,"url":"https://www.theguardian.com/world/2017/oct/12/british-transgender-woman-given-residency-in-safer-new-zealand"}],"@type":"ItemList","@context":"http://schema.org"}},{"@type":"ListItem","position":6,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"https://www.theguardian.com/world/2017/oct/12/how-europes-far-right-fell-in-love-with-australias-immigration-policy"},{"@type":"ListItem","position":1,"url":"https://www.theguardian.com/tv-and-radio/2017/oct/12/the-war-with-no-end-why-american-television-refuses-to-leave-the-trenches"},{"@type":"ListItem","position":2,"url":"https://www.theguardian.com/music/2017/oct/12/america-stand-up-eminems-freestyle-and-the-10-best-anti-trump-protest-songs-so-far"},{"@type":"ListItem","position":3,"url":"https://www.theguardian.com/culture/2017/oct/12/late-night-on-weinstein-the-second-giant-vortex-of-destructive-moisture-named-harvey"},{"@type":"ListItem","position":4,"url":"https://www.theguardian.com/working-in-development/2017/oct/12/traffic-accident-call-a-reporter-how-journalists-are-forcing-change-in-liberia"},{"@type":"ListItem","position":5,"url":"https://www.theguardian.com/film/2017/oct/12/worst-funniest-movie-poster-mistakes-ever-the-snowman"},{"@type":"ListItem","position":6,"url":"https://www.theguardian.com/lifeandstyle/2017/oct/12/jay-rayner-eldest-has-flown-the-nest-absence-leftovers"},{"@type":"ListItem","position":7,"url":"https://www.theguardian.com/artanddesign/2017/oct/12/wim-wenders-interview-polaroids-instant-stories-photographers-gallery"},{"@type":"ListItem","position":8,"url":"https://www.theguardian.com/science/brain-flapping/2017/oct/12/is-harvey-weinstein-a-sex-addict"},{"@type":"ListItem","position":9,"url":"https://www.theguardian.com/books/2017/oct/12/the-square-and-the-tower-by-niall-ferguson-review"},{"@type":"ListItem","position":10,"url":"https://www.theguardian.com/science/audio/2017/oct/12/the-party-how-can-gender-affect-autism-spectrum-disorders-science-weekly-podcast"}],"@type":"ItemList","@context":"http://schema.org"}},{"@type":"ListItem","position":7,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"snap/1486403500105"}],"@type":"ItemList","@context":"http://schema.org"}},{"@type":"ListItem","position":8,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"https://www.theguardian.com/environment/2017/oct/11/2017-deadliest-on-record-for-land-defenders-mining-logging"},{"@type":"ListItem","position":1,"url":"https://www.theguardian.com/environment/2017/oct/04/the-day-we-witnessed-wildlife-rangers-being-gunned-down-in-congo"},{"@type":"ListItem","position":2,"url":"https://www.theguardian.com/environment/ng-interactive/2017/jul/13/the-defenders-tracker"},{"@type":"ListItem","position":3,"url":"https://www.theguardian.com/world/2017/sep/29/cameroon-palm-oil-campaigner-arrested-crackdown-activists"},{"@type":"ListItem","position":4,"url":"https://www.theguardian.com/world/2017/oct/06/protect-lives-indigenous-people-can-limit-climate-change-says-un"},{"@type":"ListItem","position":5,"url":"https://www.theguardian.com/environment/2017/sep/29/bruce-parry-interview-borneo-penan-documentary"},{"@type":"ListItem","position":6,"url":"https://www.theguardian.com/environment/2017/sep/21/land-defenders-call-on-un-to-act-against-violence-by-state-funded-and-corporate-groups"},{"@type":"ListItem","position":7,"url":"https://www.theguardian.com/global-development/2017/sep/12/brazil-investigates-reports-of-massacre-among-amazon-tribe-javari-valley"},{"@type":"ListItem","position":8,"url":"https://www.theguardian.com/environment/2017/sep/11/they-lied-bolivia-untouchable-amazon-lands-tipnis-at-risk-once-more"},{"@type":"ListItem","position":9,"url":"https://www.theguardian.com/environment/2017/sep/06/six-farmers-shot-dead-over-land-rights-battle-in-peru"},{"@type":"ListItem","position":10,"url":"https://www.theguardian.com/global-development/2017/sep/04/villagers-in-indonesia-fight-for-a-land-rights-revolution"},{"@type":"ListItem","position":11,"url":"https://www.theguardian.com/environment/2017/aug/23/tribute-paid-to-silent-hero-conservationist"}],"@type":"ItemList","@context":"http://schema.org"}},{"@type":"ListItem","position":9,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"https://www.theguardian.com/world/2017/oct/12/white-widow-sally-jones-was-fleeing-raqqa-as-isiss-capital-fell"},{"@type":"ListItem","position":1,"url":"https://www.theguardian.com/media/2017/oct/12/us-journalist-who-broke-harvey-weinstein-story-to-get-channel-4-show"},{"@type":"ListItem","position":2,"url":"https://www.theguardian.com/film/2017/oct/12/andy-serkis-king-kong-was-the-epiphany-it-was-like-you-can-now-do-anything"},{"@type":"ListItem","position":3,"url":"https://www.theguardian.com/books/2017/oct/12/writers-defend-author-accused-plagiarism-jill-bialosky-poetry-will-save-your-life"}],"@type":"ItemList","@context":"http://schema.org"}},{"@type":"ListItem","position":10,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"https://www.theguardian.com/technology/2017/oct/12/shoe-colour-question-could-put-2015-dress-debate-in-the-shade"},{"@type":"ListItem","position":1,"url":"https://www.theguardian.com/lifeandstyle/shortcuts/2017/oct/11/what-does-it-mean-when-we-talk-in-our-sleep"},{"@type":"ListItem","position":2,"url":"https://www.theguardian.com/small-business-network/2017/oct/12/one-size-fits-all-the-designer-creating-clothes-that-grow-with-kids"}],"@type":"ItemList","@context":"http://schema.org"}},{"@type":"ListItem","position":11,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"https://www.theguardian.com/world/video/2017/oct/12/i-am-catalan-the-referendum-was-like-flipping-a-coin-it-didnt-make-sense-video"},{"@type":"ListItem","position":1,"url":"https://www.theguardian.com/global-development/video/2017/oct/12/colombia-trans-life-transgender-they-attack-us-for-being-who-we-are"},{"@type":"ListItem","position":2,"url":"https://www.theguardian.com/music/video/2017/oct/11/eminem-lambasts-trump-in-freestyle-rap-video"},{"@type":"ListItem","position":3,"url":"https://www.theguardian.com/world/video/2017/oct/11/i-am-catalan-its-about-building-a-new-society-for-all-video"},{"@type":"ListItem","position":4,"url":"https://www.theguardian.com/us-news/video/2017/oct/11/sheriffs-deputy-drives-through-raging-blaze-in-california-video"},{"@type":"ListItem","position":5,"url":"https://www.theguardian.com/politics/video/2017/oct/10/mhairi-black-snp-disappointed-in-jeremy-corbyn-video"}],"@type":"ItemList","@context":"http://schema.org"}},{"@type":"ListItem","position":12,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"https://www.theguardian.com/news/gallery/2017/oct/12/elizabeth-i-and-sophia-robot-pick--thursdays-photos"}],"@type":"ItemList","@context":"http://schema.org"}},{"@type":"ListItem","position":13,"item":{"url":"https://www.theguardian.com/international","itemListElement":[{"@type":"ListItem","position":0,"url":"https://www.theguardian.com/world/2017/oct/12/pakistan-rescues-canadian-american-family-hostages-haqqani"},{"@type":"ListItem","position":1,"url":"https://www.theguardian.com/world/2017/oct/12/us-withdraw-unesco-december-united-nations"},{"@type":"ListItem","position":2,"url":"https://www.theguardian.com/world/2017/oct/12/sally-jones-the-uk-punk-singer-who-became-isiss-white-widow"},{"@type":"ListItem","position":3,"url":"https://www.theguardian.com/world/2017/oct/12/trump-warns-its-possible-the-us-will-drop-out-of-nafta"},{"@type":"ListItem","position":4,"url":"https://www.theguardian.com/world/2017/oct/12/man-solves-mystery-of-1930s-sports-car-buried-on-salisbury-plain"},{"@type":"ListItem","position":5,"url":"https://www.theguardian.com/world/2017/oct/12/cuba-mass-hysteria-sonic-attacks-neurologists"},{"@type":"ListItem","position":6,"url":"https://www.theguardian.com/world/2017/oct/12/its-become-a-monster-is-irans-revolutionary-guard-a-terror-group"},{"@type":"ListItem","position":7,"url":"https://www.theguardian.com/world/2017/oct/12/my-friend-kim-wall-journalist"},{"@type":"ListItem","position":8,"url":"https://www.theguardian.com/world/2017/oct/12/white-widow-sally-jones-was-fleeing-raqqa-as-isiss-capital-fell"},{"@type":"ListItem","position":9,"url":"https://www.theguardian.com/world/2017/oct/12/british-isis-member-sally-jones-white-widow-killed-airstrike-son-islamic-state-syria"},{"@type":"ListItem","position":10,"url":"https://www.theguardian.com/world/2017/oct/12/is-targeting-of-isis-member-sally-jones-legally-justified"},{"@type":"ListItem","position":11,"url":"https://www.theguardian.com/world/2017/oct/12/joiners-arms-redevelopment-must-include-lgbt-nightclub-council-rules"},{"@type":"ListItem","position":12,"url":"https://www.theguardian.com/world/2017/oct/12/catalan-president-accuses-mariano-rajoy-of-ignoring-call-for-talks-carles-puigdemont"},{"@type":"ListItem","position":13,"url":"https://www.theguardian.com/world/2017/oct/12/christine-lagarde-imf-britain-eu-no-deal-brexit-talks"},{"@type":"ListItem","position":14,"url":"https://www.theguardian.com/world/2017/oct/11/sex-with-underage-wife-is-indian-supreme-court-rules"},{"@type":"ListItem","position":15,"url":"https://www.theguardian.com/world/2017/oct/12/top-un-official-to-leave-myanmar-amid-criticism-rohingya-approach"},{"@type":"ListItem","position":16,"url":"https://www.theguardian.com/world/2017/oct/12/anti-social-behaviour-ruling-could-halt-anti-abortion-protests-outside-clinics"},{"@type":"ListItem","position":17,"url":"https://www.theguardian.com/world/2017/oct/12/how-europes-far-right-fell-in-love-with-australias-immigration-policy"},{"@type":"ListItem","position":18,"url":"https://www.theguardian.com/world/2017/oct/12/minister-for-men-campaign-feminists-swayne-o-pie-society"},{"@type":"ListItem","position":19,"url":"https://www.theguardian.com/world/2017/oct/12/philippines-rodrigo-duterte-police-war-drugs"}],"@type":"ItemList","@context":"http://schema.org"}}],"@type":"ItemList","@context":"http://schema.org"}
                        </script>
<section class="fc-container__inner fc-trending-topics" data-component="trending-topics">
<div class="submeta submeta--borderless-bottom" data-link-name="keywords">
<span class="submeta__label">Topics</span>
<div class="submeta__keywords">
<ul class="submeta__links">
<li class="submeta__link-item"> <a class="  submeta__link" href="https://www.theguardian.com/world/europe-news" data-link-name="keyword: world/europe-news" itemprop="keywords"> Europe </a> </li>
<li class="submeta__link-item"> <a class="  submeta__link" href="https://www.theguardian.com/world/americas" data-link-name="keyword: world/americas" itemprop="keywords"> Americas </a> </li>
<li class="submeta__link-item"> <a class="  submeta__link" href="https://www.theguardian.com/world/south-and-central-asia" data-link-name="keyword: world/south-and-central-asia" itemprop="keywords"> South and Central Asia </a> </li>
<li class="submeta__link-item"> <a class="  submeta__link" href="https://www.theguardian.com/world/middleeast" data-link-name="keyword: world/middleeast" itemprop="keywords"> Middle East and North Africa </a> </li>
<li class="submeta__link-item"> <a class="  submeta__link" href="https://www.theguardian.com/environment/land-rights" data-link-name="keyword: environment/land-rights" itemprop="keywords"> Land rights </a> </li>
</ul>
</div>
</div>
</section>
<div class="fc-container fc-container--commercial">
<div id="dfp-ad--merchandising" class="js-ad-slot ad-slot ad-slot--merchandising ad-slot--commercial-component " data-link-name="ad slot merchandising" data-name="merchandising" data-label="false" data-refresh="false" data-mobile="1,1|2,2|88,88|fluid">
</div>
</div>
</div>
</div>
<footer class="l-footer u-cf" data-link-name="footer" data-component="footer">
<div class="l-footer__primary hide-on-mobile">
<div id="footer-nav" class="gs-container">
<div class="brand-bar modern-visible u-cf">
<a href="https://www.theguardian.com/international" data-link-name="site logo" class="guardian-logo-footer hide-on-mobile">
<span class="u-h">The Guardian</span>
<i class="i i-guardian-logo-160"></i>
</a>
<a class="brand-bar__item brand-bar__item--action" data-link-name="back to top" href="#top">
<span class="rounded-icon control__icon-wrapper">
<span class="inline-arrow-up inline-icon ">
<svg width="24" height="18" viewbox="0 0 24 18" class="inline-arrow-up__svg inline-icon__svg">
<path d="M.4 15.3l10.5-8.4L12 6l1.1.9 10.5 8.4-.5.7L12 9.7.9 16l-.5-.7z"/>
</svg>
</span>
</span>
<span class="control__info">back to top</span>
</a>
</div>
<div class="l-footer__navigation-wrapper u-cf">
<div class="js-navigation-footer navigation-container navigation-container--default">
<div class="gs-container navigation">
<div class="navigation__inner" aria-hidden="true">
<div class="navigation__scroll">
<div class="navigation__container navigation__container--second" data-component="footer-nav">
<ul class="top-navigation js-top-navigation">
<li class="top-navigation__item top-navigation__item--home">
<a href="https://www.theguardian.com/international" class="top-navigation__action top-navigation__action--has-icon" data-link-name="nav : primary : home" title="Back to homepage">
<span class="top-navigation__icon top-navigation__icon--home"></span>
<span class="u-h">home</span>
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk-news" data-link-name="nav : primary : UK">
UK
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/world" data-link-name="nav : primary : world">
world
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/sport" data-link-name="nav : primary : sport">
sport
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/football" data-link-name="nav : primary : football">
football
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/commentisfree" data-link-name="nav : primary : opinion">
opinion
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/culture" data-link-name="nav : primary : culture">
culture
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/business" data-link-name="nav : primary : business">
business
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/lifeandstyle" data-link-name="nav : primary : lifestyle">
lifestyle
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/fashion" data-link-name="nav : primary : fashion">
fashion
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/environment" data-link-name="nav : primary : environment">
environment
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/technology" data-link-name="nav : primary : tech">
tech
</a>
</li>
<li class="top-navigation__item">
<a class="top-navigation__action" href="https://www.theguardian.com/uk/travel" data-link-name="nav : primary : travel">
travel
</a>
</li>
</ul>
</div>
</div>
<a class="navigation-toggle js-navigation-toggle" href="#top" data-link-name="nav : allSections" data-target-nav="js-navigation-footer">
<span class="inline-arrow-up inline-icon modern-hidden">
<svg width="24" height="18" viewbox="0 0 24 18" class="modern-hidden__svg inline-arrow-up__svg inline-icon__svg">
<path d="M.4 15.3l10.5-8.4L12 6l1.1.9 10.5 8.4-.5.7L12 9.7.9 16l-.5-.7z"/>
</svg>
</span>
<i class="burger-icon modern-visible"></i>
<span class="navigation-toggle-label navigation-toggle-label--open" aria-haspopup="true" aria-controls="all-sections-popup" aria-label="view all sections">all<span class="navigation-toggle-label__extra"> sections</span></span>
<span class="navigation-toggle-label navigation-toggle-label--close" aria-label="close all sections">close</span>
</a>
</div>
<div class="js-mega-nav navigation__expandable" data-component="all-footer-nav" data-link-name="global navigation: footer : sections">
<nav role="navigation" aria-label="All sections">
<ul class="global-navigation js-global-navigation">
<li class="global-navigation__section global-navigation__section--home">
<a class="global-navigation__title" href="https://www.theguardian.com/international" data-link-name="nav : globalTop : home">
home
</a>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/uk-news" data-link-name="nav : globalTop : UK">
UK
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/education" data-link-name="nav : globalSub : education">
education
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/uk/media" data-link-name="nav : globalSub : media">
media
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/society" data-link-name="nav : globalSub : society">
society
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/law" data-link-name="nav : globalSub : law">
law
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/uk/scotland" data-link-name="nav : globalSub : scotland">
scotland
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/uk/wales" data-link-name="nav : globalSub : wales">
wales
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/uk/northernireland" data-link-name="nav : globalSub : northern ireland">
northern ireland
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/world" data-link-name="nav : globalTop : world">
world
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/world/europe-news" data-link-name="nav : globalSub : europe">
europe
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/us-news" data-link-name="nav : globalSub : US">
US
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/world/americas" data-link-name="nav : globalSub : americas">
americas
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/world/asia" data-link-name="nav : globalSub : asia">
asia
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/australia-news" data-link-name="nav : globalSub : australia">
australia
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/world/africa" data-link-name="nav : globalSub : africa">
africa
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/world/middleeast" data-link-name="nav : globalSub : middle east">
middle east
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/cities" data-link-name="nav : globalSub : cities">
cities
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/global-development" data-link-name="nav : globalSub : development">
development
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/uk/sport" data-link-name="nav : globalTop : sport">
sport
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/football" data-link-name="nav : globalSub : football">
football
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/sport/cricket" data-link-name="nav : globalSub : cricket">
cricket
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/sport/rugby-union" data-link-name="nav : globalSub : rugby union">
rugby union
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/sport/formulaone" data-link-name="nav : globalSub : F1">
F1
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/sport/tennis" data-link-name="nav : globalSub : tennis">
tennis
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/sport/golf" data-link-name="nav : globalSub : golf">
golf
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/sport/cycling" data-link-name="nav : globalSub : cycling">
cycling
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/sport/boxing" data-link-name="nav : globalSub : boxing">
boxing
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/sport/horse-racing" data-link-name="nav : globalSub : racing">
racing
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/sport/rugbyleague" data-link-name="nav : globalSub : rugby league">
rugby league
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/football" data-link-name="nav : globalTop : football">
football
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/football/live" data-link-name="nav : globalSub : live scores">
live scores
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/football/tables" data-link-name="nav : globalSub : tables">
tables
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/football/competitions" data-link-name="nav : globalSub : competitions">
competitions
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/football/results" data-link-name="nav : globalSub : results">
results
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/football/fixtures" data-link-name="nav : globalSub : fixtures">
fixtures
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/football/teams" data-link-name="nav : globalSub : clubs">
clubs
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/uk/commentisfree" data-link-name="nav : globalTop : opinion">
opinion
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/index/contributors" data-link-name="nav : globalSub : columnists">
columnists
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/tone/letters" data-link-name="nav : globalSub : letters">
letters
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/tone/editorials" data-link-name="nav : globalSub : editorials">
editorials
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/uk/culture" data-link-name="nav : globalTop : culture">
culture
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/uk/film" data-link-name="nav : globalSub : film">
film
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/uk/tv-and-radio" data-link-name="nav : globalSub : tv &amp; radio">
tv & radio
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/music" data-link-name="nav : globalSub : music">
music
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/technology/games" data-link-name="nav : globalSub : games">
games
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/books" data-link-name="nav : globalSub : books">
books
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/artanddesign" data-link-name="nav : globalSub : art &amp; design">
art & design
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/stage" data-link-name="nav : globalSub : stage">
stage
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/music/classicalmusicandopera" data-link-name="nav : globalSub : classical">
classical
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/uk/business" data-link-name="nav : globalTop : business">
business
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/business/economics" data-link-name="nav : globalSub : economics">
economics
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/business/banking" data-link-name="nav : globalSub : banking">
banking
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/business/retail" data-link-name="nav : globalSub : retail">
retail
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/business/stock-markets" data-link-name="nav : globalSub : markets">
markets
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/business/eurozone" data-link-name="nav : globalSub : eurozone">
eurozone
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/uk/lifeandstyle" data-link-name="nav : globalTop : lifestyle">
lifestyle
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/lifeandstyle/food-and-drink" data-link-name="nav : globalSub : food">
food
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/tone/recipes" data-link-name="nav : globalSub : recipes">
recipes
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/lifeandstyle/health-and-wellbeing" data-link-name="nav : globalSub : health &amp; fitness">
health & fitness
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/lifeandstyle/love-and-sex" data-link-name="nav : globalSub : love &amp; sex">
love & sex
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/lifeandstyle/family" data-link-name="nav : globalSub : family">
family
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/lifeandstyle/women" data-link-name="nav : globalSub : women">
women
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/lifeandstyle/home-and-garden" data-link-name="nav : globalSub : home &amp; garden">
home & garden
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/fashion" data-link-name="nav : globalTop : fashion">
fashion
</a>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/uk/environment" data-link-name="nav : globalTop : environment">
environment
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/environment/climate-change" data-link-name="nav : globalSub : climate change">
climate change
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/environment/wildlife" data-link-name="nav : globalSub : wildlife">
wildlife
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/environment/energy" data-link-name="nav : globalSub : energy">
energy
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/environment/pollution" data-link-name="nav : globalSub : pollution">
pollution
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/uk/technology" data-link-name="nav : globalTop : tech">
tech
</a>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/uk/travel" data-link-name="nav : globalTop : travel">
travel
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/travel/uk" data-link-name="nav : globalSub : UK">
UK
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/travel/europe" data-link-name="nav : globalSub : europe">
europe
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/travel/usa" data-link-name="nav : globalSub : US">
US
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/uk/money" data-link-name="nav : globalTop : money">
money
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/money/property" data-link-name="nav : globalSub : property">
property
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/money/savings" data-link-name="nav : globalSub : savings">
savings
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/money/pensions" data-link-name="nav : globalSub : pensions">
pensions
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/money/debt" data-link-name="nav : globalSub : borrowing">
borrowing
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/money/work-and-careers" data-link-name="nav : globalSub : careers">
careers
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/science" data-link-name="nav : globalTop : science">
science
</a>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/guardian-professional" data-link-name="nav : globalTop : professional networks">
professional networks
</a>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/observer" data-link-name="nav : globalTop : the observer">
the observer
</a>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/theguardian" data-link-name="nav : globalTop : today&#x27;s paper">
today's paper
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/tone/obituaries" data-link-name="nav : globalSub : obituaries">
obituaries
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/theguardian/g2" data-link-name="nav : globalSub : g2">
g2
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/theguardian/weekend" data-link-name="nav : globalSub : weekend">
weekend
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/theguardian/theguide" data-link-name="nav : globalSub : the guide">
the guide
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/theguardian/guardianreview" data-link-name="nav : globalSub : saturday review">
saturday review
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/theobserver" data-link-name="nav : globalTop : sunday&#x27;s paper">
sunday's paper
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/theobserver/news/comment" data-link-name="nav : globalSub : comment">
comment
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/theobserver/new-review" data-link-name="nav : globalSub : the new review">
the new review
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/theobserver/magazine" data-link-name="nav : globalSub : observer magazine">
observer magazine
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/membership" data-link-name="nav : globalTop : membership">
membership
</a>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/crosswords" data-link-name="nav : globalTop : crosswords">
crosswords
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/crosswords/crossword-blog" data-link-name="nav : globalSub : blog">
blog
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/crosswords/series/crossword-editor-update" data-link-name="nav : globalSub : editor">
editor
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/crosswords/series/quick" data-link-name="nav : globalSub : quick">
quick
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/crosswords/series/cryptic" data-link-name="nav : globalSub : cryptic">
cryptic
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/crosswords/series/prize" data-link-name="nav : globalSub : prize">
prize
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/crosswords/series/quiptic" data-link-name="nav : globalSub : quiptic">
quiptic
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/crosswords/series/genius" data-link-name="nav : globalSub : genius">
genius
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/crosswords/series/speedy" data-link-name="nav : globalSub : speedy">
speedy
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/crosswords/series/everyman" data-link-name="nav : globalSub : everyman">
everyman
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/crosswords/series/azed" data-link-name="nav : globalSub : azed">
azed
</a>
</li>
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/crosswords/series/weekend-crossword" data-link-name="nav : globalSub : weekend">
weekend
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://www.theguardian.com/video" data-link-name="nav : globalTop : video">
video
</a>
<ul class="global-navigation__children">
<li class="global-navigation__child">
<a class="global-navigation__action" href="https://www.theguardian.com/podcasts" data-link-name="nav : globalSub : podcasts">
podcasts
</a>
</li>
</ul>
</li>
<li class="global-navigation__section">
<a class="global-navigation__title" href="https://theguardian.newspapers.com" data-link-name="nav : globalTop : digital archive">
digital archive
</a>
</li>
</ul>
</nav>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="footer__primary mobile-only">
<div class="subnav">
<div class="gs-container">
<ul class="subnav__list" data-pillar-title="news">
<li class="subnav__item">
<a class="subnav-link" href="https://www.theguardian.com/world" data-link-name="nav2 : subnav : world news">
world
</a>
</li>
<li class="subnav__item">
<a class="subnav-link" href="https://www.theguardian.com/uk-news" data-link-name="nav2 : subnav : UK news">
UK
</a>
</li>
<li class="subnav__item">
<a class="subnav-link" href="https://www.theguardian.com/uk/business" data-link-name="nav2 : subnav : business">
business
</a>
</li>
<li class="subnav__item">
<a class="subnav-link" href="https://www.theguardian.com/science" data-link-name="nav2 : subnav : science">
science
</a>
</li>
<li class="subnav__item">
<a class="subnav-link" href="https://www.theguardian.com/global-development" data-link-name="nav2 : subnav : global development">
global development
</a>
</li>
<li class="subnav__item">
<a class="subnav-link" href="https://www.theguardian.com/football" data-link-name="nav2 : subnav : football">
football
</a>
</li>
</ul>
</div>
</div>
<a data-link-name="back to top" href="#top">
<div class="footer__back-to-top-container">
<div class="gs-container">
<div class="footer__back-to-top">
<span class="back-to-top__text">back to top</span>
<span class="back-to-top__icon-container">
<i class="back-to-top__icon"></i>
</span>
</div>
</div>
</div>
</a>
</div>
<div class="l-footer__secondary js-footer__secondary  gs-container" role="contentinfo">
<div class="colophon u-cf">
<div class="footer__email-container js-footer__email-container">
<iframe title="Guardian Email Sign-up Form" src="/email/form/footer/37" scrolling="no" seamless id="footer__email-form" frameborder="0" class="iframed--overflow-hidden email-sub__iframe js-email-sub__iframe" data-form-campaign-code="footer-daily-email-int" data-form-success-desc="We will send you our picks of the most important headlines tomorrow morning."></iframe>
</div>
<div class="colophon__lists-container">
<ul class="colophon__list">
<li class="colophon__item"><a data-link-name="uk : footer : membership" href="https://membership.theguardian.com/supporter?INTCMP=NGW_FOOTER_INT_GU_MEMBERSHIP&amp;acquisitionData=%7B&quot;source&quot;:&quot;GUARDIAN_WEB&quot;,&quot;componentType&quot;:&quot;ACQUISITIONS_FOOTER&quot;,&quot;componentId&quot;:&quot;NGW_FOOTER_INT_GU_MEMBERSHIP&quot;,&quot;campaignCode&quot;:&quot;NGW_FOOTER_INT_GU_MEMBERSHIP&quot;%7D">
become a supporter</a>
</li>
<li class="colophon__item"><a data-link-name="uk : footer : contribute" href="https://contribute.theguardian.com?INTCMP=gdnwb_copts_memco_dotcom_footer&amp;acquisitionData=%7B&quot;source&quot;:&quot;GUARDIAN_WEB&quot;,&quot;componentType&quot;:&quot;ACQUISITIONS_FOOTER&quot;,&quot;componentId&quot;:&quot;gdnwb_copts_memco_dotcom_footer&quot;,&quot;campaignCode&quot;:&quot;gdnwb_copts_memco_dotcom_footer&quot;%7D">
make a contribution</a>
</li>
<li class="colophon__item"><a data-link-name="securedrop" href="https://securedrop.theguardian.com/">
securedrop</a>
</li>
<li class="colophon__item"><a data-link-name="tech feedback" class="international : footer : js-tech-feedback-report" href="https://www.theguardian.com/info/tech-feedback">
solve technical issue</a>
</li>
</ul>
<ul class="colophon__list">
<li class="colophon__item"><a data-link-name="international : footer : advertise with us" href="https://advertising.theguardian.com">
advertise with us</a>
</li>
<li class="colophon__item"><a data-link-name="international : footer : work for us" href="https://workforus.theguardian.com">
work for us</a>
</li>
<li class="colophon__item"><a data-link-name="international : footer : contact us" href="https://www.theguardian.com/help/contact-us">
contact us</a>
</li>
<li class="colophon__item"><a data-link-name="complaints" href="https://www.theguardian.com/info/complaints-and-corrections">
complaints &amp; corrections</a>
</li>
</ul>
<ul class="colophon__list">
<li class="colophon__item"><a data-link-name="terms" href="https://www.theguardian.com/help/terms-of-service">
terms &amp; conditions</a>
</li>
<li class="colophon__item"><a data-link-name="privacy" href="https://www.theguardian.com/info/privacy">
privacy policy</a></li>
<li class="colophon__item"><a data-link-name="cookie" href="https://www.theguardian.com/info/cookies">
cookie policy</a>
</li>
<li class="colophon__item"><a data-link-name="digital newspaper archive" href="https://theguardian.newspapers.com">
digital newspaper archive</a>
</li>
</ul>
<ul class="colophon__list">
<li class="colophon__item"><a data-link-name="international : footer : all topics" href="https://www.theguardian.com/index/subjects/a">
all topics</a>
</li>
<li class="colophon__item"><a data-link-name="international : footer : all contributors" href="https://www.theguardian.com/index/contributors">
all contributors</a>
</li>
<li class="colophon__item"><a data-link-name="international : footer : facebook" href="https://www.facebook.com/theguardian">
Facebook</a>
</li>
<li class="colophon__item"><a data-link-name="international : footer : twitter" href="https://twitter.com/guardian">
Twitter</a>
</li>
</ul>
</div>
</div>
<div class="copyright-container">
<div class="really-serious-copyright">© 2017 Guardian News and Media Limited or its affiliated companies. All rights reserved.</div>
</div>
</div>
</footer>
<script>try{(function(isVeryModern,document,window){if(isVeryModern){var decodeBase64=function(str){return decodeURIComponent(atob(str.replace(/-/g,"+").replace(/_/g,"/").replace(/,/g,"\x3d")))};var cookieData=function(a){var d=[],e=document.cookie.split(";");a=RegExp("^\\s*"+a+"\x3d\\s*(.*?)\\s*$");for(var b=0;b<e.length;b++){var f=e[b].match(a);f&&d.push(f[1])}if(d.length>0)return d[0];return null}("GU_U");var userData=cookieData?JSON.parse(decodeBase64(cookieData.split(".")[0])):null;if(userData){var displayName=decodeURIComponent(userData[2]);window.guardian.config.user={id:userData[0],displayName:displayName,accountCreatedDate:userData[6],emailVerified:userData[7],rawResponse:cookieData}}}})(guardian.isEnhanced&&"atob"in window,document,window)}catch(e){};try{(function(document,window){if(typeof window.getComputedStyle!=="function")return;var ad=document.createElement("div");ad.style.position="absolute";ad.style.left="0";ad.style.top="0";ad.style.height="10px";ad.style.zIndex="-1";ad.innerHTML="\x26nbsp;";ad.setAttribute("class","ad_unit");window.requestAnimationFrame(function(){document.body.appendChild(ad);window.requestAnimationFrame(function(){var adBlockers=window.guardian.adBlockers;var adStyles=window.getComputedStyle(ad);var displayProp=adStyles.getPropertyValue("display");var mozBindingProp=adStyles.getPropertyValue("-moz-binding");adBlockers.active=displayProp==="none"||mozBindingProp&&mozBindingProp.indexOf("about:")!==-1;runEachListener(adBlockers.onDetect);adBlockers.onDetect={push:function(){var toRun=Array.prototype.slice.call(arguments,0);runEachListener(toRun)}};function runEachListener(listeners){for(var i=0;i<listeners.length;i++)try{listeners[i](adBlockers.active)}catch(e){}}})})})(document,window)}catch(e){};try{(function(isVeryModern,document,window){var user=window.guardian.config.user;if(isVeryModern&&user)window.requestAnimationFrame(function(){var $profileInfoElem=document.getElementsByClassName("js-profile-info")[0];var $profileNavElem=document.getElementsByClassName("js-profile-nav")[0];if(!$profileInfoElem&&!$profileNavElem)return;$profileInfoElem.innerHTML=user.displayName;$profileNavElem.classList.add("is-signed-in");var $signInLinkElem=$profileNavElem.getElementsByTagName("a")[0];if($signInLinkElem)if(user.id)$signInLinkElem.addEventListener("click",function(e){e.preventDefault()});else $signInLinkElem.setAttribute("href",$signInLinkElem.getAttribute("href").replace("signin","public/edit/"));var $register=document.getElementsByClassName("js-profile-register");if($register.length){$register=$register[0];$register.parentElement.removeChild($register)}})})("classList"in document.documentElement,document,window)}catch(e){};(function(window,document){function getCookieValue(name){var nameEq=name+"\x3d",cookies=document.cookie.split(";"),value=null;cookies.forEach(function(cookie){while(cookie.charAt(0)===" ")cookie=cookie.substring(1,cookie.length);if(cookie.indexOf(nameEq)===0)value=cookie.substring(nameEq.length,cookie.length)});return value}window.guardian.config.ophan.browserId=getCookieValue("bwid")})(window,document);</script>
<script id='google_analytics'>(function(){function convertContentType(contentType){var result=contentType;if(typeof contentType==='string'){result=contentType.toLowerCase().split(' ').join('');}return result;}function getQueryParam(key){var query=window.location.search.substring(1);var vars=query.split("&");var pairs=vars.map(function(x){return x.split('=')});return pairs.filter(function(xs){return xs.length==2&&xs[0]==key}).map(function(xs){return xs[1]})[0];}function getAnalyticsEdition(){var edition=(guardian.config.page.edition||'').toLowerCase()
return edition==='int'?'international':edition;}function getAnalyticsTitle(){var analyticsTitle=(guardian.config.page.webTitle||'');return(analyticsTitle==='Network Front')?getAnalyticsEdition()+' network front':analyticsTitle;}function getExperienceValue(){return'none';}var identityId=null;if(guardian.config.user){identityId=guardian.config.user.id;}var isLoggedIn=(!!identityId).toString();(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,'script','//www.google-analytics.com/analytics.js','ga');ga('create','UA-78705427-1','auto','allEditorialPropertyTracker',{'sampleRate':100,'siteSpeedSampleRate':0.1,'userId':identityId});ga('create','UA-33592456-1','auto','guardianTestPropertyTracker',{'sampleRate':5,'siteSpeedSampleRate':0.1,'userId':identityId});ga('allEditorialPropertyTracker.set','forceSSL',true);ga('allEditorialPropertyTracker.set','title',getAnalyticsTitle());ga('allEditorialPropertyTracker.set','dimension1',guardian.config.ophan.pageViewId);ga('allEditorialPropertyTracker.set','dimension2',guardian.config.ophan.browserId);ga('allEditorialPropertyTracker.set','dimension3','theguardian.com');ga('allEditorialPropertyTracker.set','dimension4',guardian.config.page.section);ga('allEditorialPropertyTracker.set','dimension5',convertContentType(guardian.config.page.contentType));ga('allEditorialPropertyTracker.set','dimension6',guardian.config.page.commissioningDesks);ga('allEditorialPropertyTracker.set','dimension7',guardian.config.page.contentId);ga('allEditorialPropertyTracker.set','dimension8',guardian.config.page.authorIds);ga('allEditorialPropertyTracker.set','dimension9',guardian.config.page.keywordIds);ga('allEditorialPropertyTracker.set','dimension10',guardian.config.page.toneIds);ga('allEditorialPropertyTracker.set','dimension11',guardian.config.page.seriesId);ga('allEditorialPropertyTracker.set','dimension15',identityId);ga('allEditorialPropertyTracker.set','dimension16',isLoggedIn);ga('allEditorialPropertyTracker.set','dimension21',getQueryParam('INTCMP'));ga('allEditorialPropertyTracker.set','dimension22',getQueryParam('CMP_BUNIT'));ga('allEditorialPropertyTracker.set','dimension23',getQueryParam('CMP_TU'));ga('allEditorialPropertyTracker.set','dimension26',(!!guardian.config.page.isHosted).toString());ga('allEditorialPropertyTracker.set','dimension27',navigator.userAgent);ga('allEditorialPropertyTracker.set','dimension29',window.location.href);ga('allEditorialPropertyTracker.set','dimension30',getAnalyticsEdition());ga('allEditorialPropertyTracker.set','dimension43',getExperienceValue());if(document.location.hash==='#fbLogin'){ga('allEditorialPropertyTracker.set','referrer',null);document.location.hash='';}ga('guardianTestPropertyTracker.set','forceSSL',true);ga('guardianTestPropertyTracker.set','title',getAnalyticsTitle());ga('guardianTestPropertyTracker.set','dimension1',guardian.config.ophan.pageViewId);ga('guardianTestPropertyTracker.set','dimension2',guardian.config.ophan.browserId);ga('guardianTestPropertyTracker.set','dimension3','theguardian.com');ga('guardianTestPropertyTracker.set','dimension4',guardian.config.page.section);ga('guardianTestPropertyTracker.set','dimension5',convertContentType(guardian.config.page.contentType));ga('guardianTestPropertyTracker.set','dimension6',guardian.config.page.commissioningDesks);ga('guardianTestPropertyTracker.set','dimension7',guardian.config.page.contentId);ga('guardianTestPropertyTracker.set','dimension8',guardian.config.page.authorIds);ga('guardianTestPropertyTracker.set','dimension9',guardian.config.page.keywordIds);ga('guardianTestPropertyTracker.set','dimension10',guardian.config.page.toneIds);ga('guardianTestPropertyTracker.set','dimension11',guardian.config.page.seriesId);ga('guardianTestPropertyTracker.set','dimension15',identityId);ga('guardianTestPropertyTracker.set','dimension16',isLoggedIn);ga('guardianTestPropertyTracker.set','dimension21',getQueryParam('INTCMP'));ga('guardianTestPropertyTracker.set','dimension22',getQueryParam('CMP_BUNIT'));ga('guardianTestPropertyTracker.set','dimension23',getQueryParam('CMP_TU'));ga('guardianTestPropertyTracker.set','dimension26',(!!guardian.config.page.isHosted).toString());ga('guardianTestPropertyTracker.set','dimension27',navigator.userAgent);ga('guardianTestPropertyTracker.set','dimension29',window.location.href);ga('guardianTestPropertyTracker.set','dimension30',getAnalyticsEdition());ga('guardianTestPropertyTracker.set','dimension43',getExperienceValue());if(document.location.hash==='#fbLogin'){ga('guardianTestPropertyTracker.set','referrer',null);document.location.hash='';}ga('allEditorialPropertyTracker.send','pageview',{hitCallback:function(){var image=new Image();image.src="//beacon.gu-web.net/count/pvg.gif";}});try{var NG_STORAGE_KEY='gu.analytics.referrerVars';var referrerVarsData=window.sessionStorage.getItem(NG_STORAGE_KEY);var referrerVars=JSON.parse(referrerVarsData);if(referrerVars&&referrerVars.value){var d=new Date().getTime();if(d-referrerVars.value.time<60*1000){ga('allEditorialPropertyTracker.send','event','Click','Internal',referrerVars.value.tag,{nonInteraction:true,dimension12:referrerVars.value.path});}window.sessionStorage.removeItem(NG_STORAGE_KEY);}}catch(e){}guardian.app&&guardian.app.mediator&&guardian.app.mediator.emit('modules:ga:ready');})();</script>
<noscript id="googleNoScript">
<img id="googleConfidenceNoScriptImage" alt="" src="//beacon.gu-web.net/count/pvg.gif" width="1" height="1" class="u-h"/>
</noscript>
<script id='comscore'>var _comscore=_comscore||[];_comscore.push({c1:"2",c2:"6035250",comscorekw:guardian.config.page.keywords});(function(){var s=document.createElement("script"),el=document.getElementsByTagName("script")[0];s.async=true;s.src="https://sb.scorecardresearch.com/beacon.js";el.parentNode.insertBefore(s,el);})();</script>
<noscript>
<img src="https://sb.scorecardresearch.com/p?c1=2&c2=6035250&cv=2.0&cj=1&comscorekw="/>
</noscript>
<noscript>
<div style="display:inline;">
<img height="1" width="1" style="border-style:none;" alt="" src="//googleads.g.doubleclick.net/pagead/viewthroughconversion/971225648/?value=0&amp;guid=ON&amp;script=0"/>
</div>
</noscript>
<img src="//beacon.gu-web.net/count/pv.gif" alt="" style="display : none ;" rel="nofollow"/>
<img src="https://www.facebook.com/tr?id=279880532344561&ev=PageView&noscript=1" height="1" width="1" style="display:none" rel="nofollow" alt=""/>
</body>
</html>

"""


class GetTheGaurdianData():
    HOME_PAGE_DATA = None
    HOME_PAGE_DATA_FORMATTED = None
    LOCAL_LOAD = False
    FORMATTED_FOR_CSV = None
    @staticmethod
    def load_home_page(ghp):
        if not GetTheGaurdianData.LOCAL_LOAD:
            r = requests.get("https://www.theguardian.com/")
            soup = BeautifulSoup(r.text, "html5lib")
            GetTheGaurdianData.HOME_PAGE_DATA = soup
            # l = soup.findAll('div', {'class': 'fc-item__container'})
        else:
            soup = BeautifulSoup(ghp, "html5lib")
            GetTheGaurdianData.HOME_PAGE_DATA = soup
        print("succesfully retrieved the home page")

    
    @staticmethod
    def load_headlines(quantity_of_articles=10):
        soup = GetTheGaurdianData.HOME_PAGE_DATA
        l = soup.findAll("div", class_="fc-item__container")
        headlines = []
        
        if quantity_of_articles == 'all':
            start = 0
            finish = len(l)
        elif quantity_of_articles == 10:
            start = 6
            finish = 8
        
        for item in l[start:finish]:
            headline = {}
            headline['headline_title'] = item.find('span', {"class": "u-faux-block-link__cta fc-item__headline"}).text
            try:
                headline['headline_body'] = item.find('div', {"class": "fc-item__standfirst"}).text 
            except:
                headline['headline_body'] = 'No body on front page'
                
            try:
                headline['headline_kicker'] = item.find('span', {'class': 'fc-item__kicker'}).text
            except:
                headline['headline_kicker'] = 'None found'
                
            headline['headline_link'] = item.find('a', {'class': "fc-item__link"}).get('href')
            
            
            headlines.append(headline)
            
        GetTheGaurdianData.HOME_PAGE_DATA_FORMATTED = headlines
        return headlines
        
        
        
    @staticmethod
    def get_per_page_details(data, position):
        data_with_details = []
        author_names = None
        
        # for article in GetTheGaurdianData.HOME_PAGE_DATA_FORMATTED:
        article = GetTheGaurdianData.HOME_PAGE_DATA_FORMATTED[position]
        meta_data = {}
        meta_data['title'] = article['headline_title']
        # Load the article page
        r = requests.get(article['headline_link'])
        soup = BeautifulSoup(r.text, "html5lib")
        
        # create an object out of the meta content data
        meta_content = soup.find('div', {'class': "content__meta-container"})
        
        if meta_content == None:
            print("this article doesn't have regular meta content")
            meta_data = {
                    'authors': 'None Found',
                    'keywords': 'None Found',
                    'date': 'None Found'
                    }
            data_with_details.append(meta_data)
            return data_with_details
            
        # Get the author(s)
        authors = meta_content.findAll('span', {'itemprop': 'name'})
        
        if len(authors) > 0:
            meta_data['authors'] = authors[0].text
            if len(authors) > 1:
                for author in authors[1:]:
                    meta_data['authors'] += ', ' + author.text
        else:
            meta_data['authors'] = 'No Authors Found'
            print("Authors: ", meta_data['authors'])
                
        # Get the date
        
        date_string = soup.find('time', {'class': 'content__dateline-wpd'}).text
        
        date_time_string = soup.find('span', {'class': 'content__dateline-time'}).text
        meta_data['date'] = date_string + ' ' + date_time_string
        print(meta_data['date'])
        
        # get meta tags
        keywords = soup.findAll('li', {'class': 'submeta__link-item'})
        meta_data['keywords'] = ''
        for keyword in keywords:
            text = keyword.find('a').text
            link = keyword.find('a').get('href')
            meta_data['keywords'] += "<a href='{}'>{}</a> ".format(link, text)
        
        data_with_details.append(meta_data) 
        print(data_with_details)
        return data_with_details
        
        
        
            
                
        # return data_with_details
        

# g = GetTheGaurdianData()
# g.load_home_page(ghp)
# g.load_headlines()