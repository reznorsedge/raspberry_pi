  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>docopt/docopt.py at master · docopt/docopt</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <link rel="xhr-socket" href="/_sockets" />


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="4275063" name="octolytics-actor-id" /><meta content="b464e105316ce58ba20008518abf1caa611ed5bbde2f36ed7e331167d726d0b0" name="octolytics-actor-hash" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="Yw7iWJYPgKqYLJ/OPl10qqJUrgUmInrrBwTAImeeMA0=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-fdebe8d3f60746fb87c763a59741ff520ae3d8e8.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-d530e63e2c132c7f0e6ac7228e7e1ab9ef2a8d94.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-92d138f450f2960501e28397a2f63b0f100590f0.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-4037f12703c2d563310be4fcd52a229189468cce.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="80973bfd2a5cb09c53d745b26b5b1dc0">

        <link data-pjax-transient rel='permalink' href='/docopt/docopt/blob/50e0a41cd3445fc116d9feeb0fab50276ad41ab0/docopt.py'>
    <meta property="og:title" content="docopt"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/docopt/docopt"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/e82bc289285e348387313a00cfd84979?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="docopt - Pythonic command line arguments parser, that will make you smile"/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="docopt/docopt"/>

    <meta name="description" content="docopt - Pythonic command line arguments parser, that will make you smile" />


    <meta content="1820478" name="octolytics-dimension-user_id" /><meta content="3959394" name="octolytics-dimension-repository_id" />
  <link href="https://github.com/docopt/docopt/commits/master.atom" rel="alternate" title="Recent Commits to docopt:master" type="application/atom+xml" />

  </head>


  <body class="logged_in page-blob macintosh vis-public env-production  ">
    <div id="wrapper">

      

      
      
      

      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-icon mega-icon-invertocat"></span>
</a>

    <div class="divider-vertical"></div>

      <a href="/notifications" class="notification-indicator tooltipped downwards" title="You have no unread notifications">
    <span class="mail-status all-read"></span>
  </a>
  <div class="divider-vertical"></div>


      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">
  <a href="/search/advanced" class="advanced-search-icon tooltipped downwards command-bar-search" id="advanced_search" title="Advanced search"><span class="mini-icon mini-icon-advanced-search "></span></a>

  <input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    data-username="reznorsedge"
      data-repo="docopt/docopt"
      data-branch="master"
      data-sha="f49ee8ba4293a59e5bd7253118b764f2d155d57f"
  >

    <input type="hidden" name="nwo" value="docopt/docopt" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item selected">
            <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item">
            <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="mini-icon help tooltipped downwards" title="Show command bar help">
    <span class="mini-icon mini-icon-help"></span>
  </span>

    <input type="hidden" name="type" value="Code" />

  <input type="hidden" name="ref" value="cmdform">

  <div class="divider-vertical"></div>

</form>
        <ul class="top-nav">
            <li class="explore"><a href="https://github.com/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="http://help.github.com">Help</a></li>
        </ul>
      </div>

    

  

    <ul id="user-links">
      <li>
        <a href="https://github.com/reznorsedge" class="name">
          <img height="20" src="https://secure.gravatar.com/avatar/ab739400e7e07e9470813d9c4b6b8160?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /> reznorsedge
        </a>
      </li>

        <li>
          <a href="/new" id="new_repo" class="tooltipped downwards" title="Create a new repo">
            <span class="mini-icon mini-icon-create"></span>
          </a>
        </li>

        <li>
          <a href="/settings/profile" id="account_settings"
            class="tooltipped downwards"
            title="Account settings ">
            <span class="mini-icon mini-icon-account-settings"></span>
          </a>
        </li>
        <li>
          <a class="tooltipped downwards" href="/logout" data-method="post" id="logout" title="Sign out">
            <span class="mini-icon mini-icon-logout"></span>
          </a>
        </li>

    </ul>


<div class="js-new-dropdown-contents hidden">
  <ul class="dropdown-menu">
    <li>
      <a href="/new"><span class="mini-icon mini-icon-create"></span> New repository</a>
    </li>
    <li>
        <a href="https://github.com/docopt/docopt/issues/new"><span class="mini-icon mini-icon-issue-opened"></span> New issue</a>
    </li>
    <li>
    </li>
    <li>
      <a href="/organizations/new"><span class="mini-icon mini-icon-u-list"></span> New organization</a>
    </li>
  </ul>
</div>


    
  </div>
</div>

      

      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              

<ul class="pagehead-actions">


    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="Yw7iWJYPgKqYLJ/OPl10qqJUrgUmInrrBwTAImeeMA0=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="3959394" />

    <div class="select-menu js-menu-container js-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">
          <span class="mini-icon mini-icon-watching"></span>
          Watch
        </span>
      </span>

      <div class="select-menu-modal-holder js-menu-content">
        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="mini-icon mini-icon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container">

            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for discussions in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="mini-icon mini-icon-watching"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
              <div class="select-menu-item-text">
                <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="mini-icon mini-icon-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="mini-icon mini-icon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

    <li class="js-toggler-container js-social-container starring-container on">
      <a href="/docopt/docopt/unstar" class="minibutton js-toggler-target star-button starred upwards" title="Unstar this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="mini-icon mini-icon-remove-star"></span>
        <span class="text">Unstar</span>
      </a>
      <a href="/docopt/docopt/star" class="minibutton js-toggler-target star-button unstarred upwards" title="Star this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="mini-icon mini-icon-star"></span>
        <span class="text">Star</span>
      </a>
      <a class="social-count js-social-count" href="/docopt/docopt/stargazers">1,224</a>
    </li>

        <li>
          <a href="/docopt/docopt/fork" class="minibutton js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="nofollow" data-method="post">
            <span class="mini-icon mini-icon-branch-create"></span>
            <span class="text">Fork</span>
          </a>
          <a href="/docopt/docopt/network" class="social-count">71</a>
        </li>


</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-icon mega-icon-public-repo"></span>
                <span class="author vcard">
                  <a href="/docopt" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">docopt</span>
                  </a></span> /
                <strong><a href="/docopt/docopt" class="js-current-repository">docopt</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li class="pulse-nav"><a href="/docopt/docopt/pulse" class="js-selected-navigation-item " data-selected-links="pulse /docopt/docopt/pulse" rel="nofollow"><span class="mini-icon mini-icon-pulse"></span></a></li>
    <li><a href="/docopt/docopt" class="js-selected-navigation-item selected" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /docopt/docopt">Code</a></li>
    <li><a href="/docopt/docopt/network" class="js-selected-navigation-item " data-selected-links="repo_network /docopt/docopt/network">Network</a></li>
    <li><a href="/docopt/docopt/pulls" class="js-selected-navigation-item " data-selected-links="repo_pulls /docopt/docopt/pulls">Pull Requests <span class='counter'>3</span></a></li>

      <li><a href="/docopt/docopt/issues" class="js-selected-navigation-item " data-selected-links="repo_issues /docopt/docopt/issues">Issues <span class='counter'>26</span></a></li>



    <li><a href="/docopt/docopt/graphs" class="js-selected-navigation-item " data-selected-links="repo_graphs repo_contributors /docopt/docopt/graphs">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/docopt/docopt/tags" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_tags /docopt/docopt/tags">Tags <span class="counter ">10</span></a></li>
    </ul>
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="mini-icon mini-icon-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">

        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="mini-icon mini-icon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches">

            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/call-module/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="call-module" rel="nofollow" title="call-module">call-module</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/delegation/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="delegation" rel="nofollow" title="delegation">delegation</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/error-messages/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="error-messages" rel="nofollow" title="error-messages">error-messages</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item selected">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/master/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/moving-tests-to-agnostic/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="moving-tests-to-agnostic" rel="nofollow" title="moving-tests-to-agnostic">moving-tests-to-agnostic</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/peg-parser/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="peg-parser" rel="nofollow" title="peg-parser">peg-parser</a>
                </div> <!-- /.select-menu-item -->
            </div>

              <div class="select-menu-no-results">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags">
            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/0.6.1/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="0.6.1" rel="nofollow" title="0.6.1">0.6.1</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/0.6.0/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="0.6.0" rel="nofollow" title="0.6.0">0.6.0</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/0.5.0/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="0.5.0" rel="nofollow" title="0.5.0">0.5.0</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/0.4.2/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="0.4.2" rel="nofollow" title="0.4.2">0.4.2</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/0.4.1/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="0.4.1" rel="nofollow" title="0.4.1">0.4.1</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/0.4.0/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="0.4.0" rel="nofollow" title="0.4.0">0.4.0</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/0.3.0/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="0.3.0" rel="nofollow" title="0.3.0">0.3.0</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/0.2.0/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="0.2.0" rel="nofollow" title="0.2.0">0.2.0</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/0.1.1/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="0.1.1" rel="nofollow" title="0.1.1">0.1.1</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/docopt/docopt/blob/0.1.0/docopt.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="0.1.0" rel="nofollow" title="0.1.0">0.1.0</a>
                </div> <!-- /.select-menu-item -->
            </div>

            <div class="select-menu-no-results">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/docopt/docopt" class="selected js-selected-navigation-item tabnav-tab" data-selected-links="repo_source /docopt/docopt">Files</a></li>
    <li><a href="/docopt/docopt/commits/master" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_commits /docopt/docopt/commits/master">Commits</a></li>
    <li><a href="/docopt/docopt/branches" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_branches /docopt/docopt/branches" rel="nofollow">Branches <span class="counter ">6</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:a641f15baa3021558de84d98ce87a3ea -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:a641f15baa3021558de84d98ce87a3ea -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/docopt/docopt" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">docopt</span></a></span></span><span class="separator"> / </span><strong class="final-path">docopt.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="docopt.py" data-copied-hint="copied!" title="copy to clipboard"><span class="mini-icon mini-icon-clipboard"></span></span>
        </div>

      <a href="/docopt/docopt/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/8ae368318a55e95748b85f82ca83a289?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><a href="/halst" rel="author">halst</a></span>
    <time class="js-relative-date" datetime="2013-04-08T09:27:28-07:00" title="2013-04-08 09:27:28">April 08, 2013</time>
    <div class="commit-title">
        <a href="/docopt/docopt/commit/84fd4bca9c09743df8501a5da148a258197f1445" class="message">Merge remote-tracking branch 'origin/master'</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>8</strong> contributors</a></p>
          <a class="avatar tooltipped downwards" title="halst" href="/docopt/docopt/commits/master/docopt.py?author=halst"><img height="20" src="https://secure.gravatar.com/avatar/8ae368318a55e95748b85f82ca83a289?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="Vlad-Shcherbina" href="/docopt/docopt/commits/master/docopt.py?author=Vlad-Shcherbina"><img height="20" src="https://secure.gravatar.com/avatar/d9cf527da96fb9172bff0284e8cc13ae?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="Met48" href="/docopt/docopt/commits/master/docopt.py?author=Met48"><img height="20" src="https://secure.gravatar.com/avatar/f0f407bf72ab68dc828739176ac336c4?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="schmir" href="/docopt/docopt/commits/master/docopt.py?author=schmir"><img height="20" src="https://secure.gravatar.com/avatar/1548e13088e0f8e55c25f4c543ad9140?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="johari" href="/docopt/docopt/commits/master/docopt.py?author=johari"><img height="20" src="https://secure.gravatar.com/avatar/a9911c6bfc7b6e2b219e4dec24ab8d72?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="jeffrimko" href="/docopt/docopt/commits/master/docopt.py?author=jeffrimko"><img height="20" src="https://secure.gravatar.com/avatar/6aac48e7c3ea7bf4f515223c4c5c52aa?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="xiaq" href="/docopt/docopt/commits/master/docopt.py?author=xiaq"><img height="20" src="https://secure.gravatar.com/avatar/dcecdb372d2c5c8741b5d7a52eead983?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="andreypopp" href="/docopt/docopt/commits/master/docopt.py?author=andreypopp"><img height="20" src="https://secure.gravatar.com/avatar/b81f3c915bb1782e6ebe5a542e57ef9b?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2>Users on GitHub who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/8ae368318a55e95748b85f82ca83a289?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/halst">halst</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/d9cf527da96fb9172bff0284e8cc13ae?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/Vlad-Shcherbina">Vlad-Shcherbina</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/f0f407bf72ab68dc828739176ac336c4?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/Met48">Met48</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/1548e13088e0f8e55c25f4c543ad9140?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/schmir">schmir</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/a9911c6bfc7b6e2b219e4dec24ab8d72?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/johari">johari</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/6aac48e7c3ea7bf4f515223c4c5c52aa?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/jeffrimko">jeffrimko</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/dcecdb372d2c5c8741b5d7a52eead983?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/xiaq">xiaq</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/b81f3c915bb1782e6ebe5a542e57ef9b?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/andreypopp">andreypopp</a>
        </li>
      </ul>
    </div>
  </div>


    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/docopt/docopt/blob/50e0a41cd3445fc116d9feeb0fab50276ad41ab0/docopt.py" data-title="docopt/docopt.py at master · docopt/docopt · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>582 lines (473 sloc)</span>
                <span>19.78 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                        <a class="minibutton tooltipped leftwards"
                           title="Clicking this button will automatically fork this project so you can edit the file"
                           href="/docopt/docopt/edit/master/docopt.py"
                           data-method="post" rel="nofollow">Edit</a>
                  <a href="/docopt/docopt/raw/master/docopt.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/docopt/docopt/blame/master/docopt.py" class="button minibutton ">Blame</a>
                  <a href="/docopt/docopt/commits/master/docopt.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>
<span id="L441" rel="#L441">441</span>
<span id="L442" rel="#L442">442</span>
<span id="L443" rel="#L443">443</span>
<span id="L444" rel="#L444">444</span>
<span id="L445" rel="#L445">445</span>
<span id="L446" rel="#L446">446</span>
<span id="L447" rel="#L447">447</span>
<span id="L448" rel="#L448">448</span>
<span id="L449" rel="#L449">449</span>
<span id="L450" rel="#L450">450</span>
<span id="L451" rel="#L451">451</span>
<span id="L452" rel="#L452">452</span>
<span id="L453" rel="#L453">453</span>
<span id="L454" rel="#L454">454</span>
<span id="L455" rel="#L455">455</span>
<span id="L456" rel="#L456">456</span>
<span id="L457" rel="#L457">457</span>
<span id="L458" rel="#L458">458</span>
<span id="L459" rel="#L459">459</span>
<span id="L460" rel="#L460">460</span>
<span id="L461" rel="#L461">461</span>
<span id="L462" rel="#L462">462</span>
<span id="L463" rel="#L463">463</span>
<span id="L464" rel="#L464">464</span>
<span id="L465" rel="#L465">465</span>
<span id="L466" rel="#L466">466</span>
<span id="L467" rel="#L467">467</span>
<span id="L468" rel="#L468">468</span>
<span id="L469" rel="#L469">469</span>
<span id="L470" rel="#L470">470</span>
<span id="L471" rel="#L471">471</span>
<span id="L472" rel="#L472">472</span>
<span id="L473" rel="#L473">473</span>
<span id="L474" rel="#L474">474</span>
<span id="L475" rel="#L475">475</span>
<span id="L476" rel="#L476">476</span>
<span id="L477" rel="#L477">477</span>
<span id="L478" rel="#L478">478</span>
<span id="L479" rel="#L479">479</span>
<span id="L480" rel="#L480">480</span>
<span id="L481" rel="#L481">481</span>
<span id="L482" rel="#L482">482</span>
<span id="L483" rel="#L483">483</span>
<span id="L484" rel="#L484">484</span>
<span id="L485" rel="#L485">485</span>
<span id="L486" rel="#L486">486</span>
<span id="L487" rel="#L487">487</span>
<span id="L488" rel="#L488">488</span>
<span id="L489" rel="#L489">489</span>
<span id="L490" rel="#L490">490</span>
<span id="L491" rel="#L491">491</span>
<span id="L492" rel="#L492">492</span>
<span id="L493" rel="#L493">493</span>
<span id="L494" rel="#L494">494</span>
<span id="L495" rel="#L495">495</span>
<span id="L496" rel="#L496">496</span>
<span id="L497" rel="#L497">497</span>
<span id="L498" rel="#L498">498</span>
<span id="L499" rel="#L499">499</span>
<span id="L500" rel="#L500">500</span>
<span id="L501" rel="#L501">501</span>
<span id="L502" rel="#L502">502</span>
<span id="L503" rel="#L503">503</span>
<span id="L504" rel="#L504">504</span>
<span id="L505" rel="#L505">505</span>
<span id="L506" rel="#L506">506</span>
<span id="L507" rel="#L507">507</span>
<span id="L508" rel="#L508">508</span>
<span id="L509" rel="#L509">509</span>
<span id="L510" rel="#L510">510</span>
<span id="L511" rel="#L511">511</span>
<span id="L512" rel="#L512">512</span>
<span id="L513" rel="#L513">513</span>
<span id="L514" rel="#L514">514</span>
<span id="L515" rel="#L515">515</span>
<span id="L516" rel="#L516">516</span>
<span id="L517" rel="#L517">517</span>
<span id="L518" rel="#L518">518</span>
<span id="L519" rel="#L519">519</span>
<span id="L520" rel="#L520">520</span>
<span id="L521" rel="#L521">521</span>
<span id="L522" rel="#L522">522</span>
<span id="L523" rel="#L523">523</span>
<span id="L524" rel="#L524">524</span>
<span id="L525" rel="#L525">525</span>
<span id="L526" rel="#L526">526</span>
<span id="L527" rel="#L527">527</span>
<span id="L528" rel="#L528">528</span>
<span id="L529" rel="#L529">529</span>
<span id="L530" rel="#L530">530</span>
<span id="L531" rel="#L531">531</span>
<span id="L532" rel="#L532">532</span>
<span id="L533" rel="#L533">533</span>
<span id="L534" rel="#L534">534</span>
<span id="L535" rel="#L535">535</span>
<span id="L536" rel="#L536">536</span>
<span id="L537" rel="#L537">537</span>
<span id="L538" rel="#L538">538</span>
<span id="L539" rel="#L539">539</span>
<span id="L540" rel="#L540">540</span>
<span id="L541" rel="#L541">541</span>
<span id="L542" rel="#L542">542</span>
<span id="L543" rel="#L543">543</span>
<span id="L544" rel="#L544">544</span>
<span id="L545" rel="#L545">545</span>
<span id="L546" rel="#L546">546</span>
<span id="L547" rel="#L547">547</span>
<span id="L548" rel="#L548">548</span>
<span id="L549" rel="#L549">549</span>
<span id="L550" rel="#L550">550</span>
<span id="L551" rel="#L551">551</span>
<span id="L552" rel="#L552">552</span>
<span id="L553" rel="#L553">553</span>
<span id="L554" rel="#L554">554</span>
<span id="L555" rel="#L555">555</span>
<span id="L556" rel="#L556">556</span>
<span id="L557" rel="#L557">557</span>
<span id="L558" rel="#L558">558</span>
<span id="L559" rel="#L559">559</span>
<span id="L560" rel="#L560">560</span>
<span id="L561" rel="#L561">561</span>
<span id="L562" rel="#L562">562</span>
<span id="L563" rel="#L563">563</span>
<span id="L564" rel="#L564">564</span>
<span id="L565" rel="#L565">565</span>
<span id="L566" rel="#L566">566</span>
<span id="L567" rel="#L567">567</span>
<span id="L568" rel="#L568">568</span>
<span id="L569" rel="#L569">569</span>
<span id="L570" rel="#L570">570</span>
<span id="L571" rel="#L571">571</span>
<span id="L572" rel="#L572">572</span>
<span id="L573" rel="#L573">573</span>
<span id="L574" rel="#L574">574</span>
<span id="L575" rel="#L575">575</span>
<span id="L576" rel="#L576">576</span>
<span id="L577" rel="#L577">577</span>
<span id="L578" rel="#L578">578</span>
<span id="L579" rel="#L579">579</span>
<span id="L580" rel="#L580">580</span>
<span id="L581" rel="#L581">581</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="sd">&quot;&quot;&quot;Pythonic command-line interface parser that will make you smile.</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="sd"> * http://docopt.org</span></div><div class='line' id='LC4'><span class="sd"> * Repository and issue-tracker: https://github.com/docopt/docopt</span></div><div class='line' id='LC5'><span class="sd"> * Licensed under terms of MIT license (see LICENSE-MIT)</span></div><div class='line' id='LC6'><span class="sd"> * Copyright (c) 2013 Vladimir Keleshev, vladimir@keleshev.com</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC9'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC10'><span class="kn">import</span> <span class="nn">re</span></div><div class='line' id='LC11'><br/></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;docopt&#39;</span><span class="p">]</span></div><div class='line' id='LC14'><span class="n">__version__</span> <span class="o">=</span> <span class="s">&#39;0.6.1&#39;</span></div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'><br/></div><div class='line' id='LC17'><span class="k">class</span> <span class="nc">DocoptLanguageError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Error in construction of usage-message by developer.&quot;&quot;&quot;</span></div><div class='line' id='LC20'><br/></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'><span class="k">class</span> <span class="nc">DocoptExit</span><span class="p">(</span><span class="ne">SystemExit</span><span class="p">):</span></div><div class='line' id='LC23'><br/></div><div class='line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Exit in case user invoked program with incorrect arguments.&quot;&quot;&quot;</span></div><div class='line' id='LC25'><br/></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">usage</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC27'><br/></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ne">SystemExit</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="p">(</span><span class="n">message</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">usage</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">())</span></div><div class='line' id='LC30'><br/></div><div class='line' id='LC31'><br/></div><div class='line' id='LC32'><span class="k">class</span> <span class="nc">Pattern</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">==</span> <span class="nb">repr</span><span class="p">(</span><span class="n">other</span><span class="p">)</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">hash</span><span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span></div><div class='line' id='LC39'><br/></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">fix</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fix_identities</span><span class="p">()</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fix_repeating_arguments</span><span class="p">()</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span></div><div class='line' id='LC44'><br/></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">fix_identities</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">uniq</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Make pattern-tree tips point to same object if they are equal.&quot;&quot;&quot;</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s">&#39;children&#39;</span><span class="p">):</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">uniq</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">flat</span><span class="p">()))</span> <span class="k">if</span> <span class="n">uniq</span> <span class="ow">is</span> <span class="bp">None</span> <span class="k">else</span> <span class="n">uniq</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">child</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">):</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">child</span><span class="p">,</span> <span class="s">&#39;children&#39;</span><span class="p">):</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">child</span> <span class="ow">in</span> <span class="n">uniq</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">uniq</span><span class="p">[</span><span class="n">uniq</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">child</span><span class="p">)]</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">child</span><span class="o">.</span><span class="n">fix_identities</span><span class="p">(</span><span class="n">uniq</span><span class="p">)</span></div><div class='line' id='LC56'><br/></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">fix_repeating_arguments</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Fix elements that should accumulate/increment values.&quot;&quot;&quot;</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">either</span> <span class="o">=</span> <span class="p">[</span><span class="nb">list</span><span class="p">(</span><span class="n">child</span><span class="o">.</span><span class="n">children</span><span class="p">)</span> <span class="k">for</span> <span class="n">child</span> <span class="ow">in</span> <span class="n">transform</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">children</span><span class="p">]</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">either</span><span class="p">:</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="p">[</span><span class="n">child</span> <span class="k">for</span> <span class="n">child</span> <span class="ow">in</span> <span class="n">case</span> <span class="k">if</span> <span class="n">case</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="n">child</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">]:</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">e</span><span class="p">)</span> <span class="ow">is</span> <span class="n">Argument</span> <span class="ow">or</span> <span class="nb">type</span><span class="p">(</span><span class="n">e</span><span class="p">)</span> <span class="ow">is</span> <span class="n">Option</span> <span class="ow">and</span> <span class="n">e</span><span class="o">.</span><span class="n">argcount</span><span class="p">:</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">e</span><span class="o">.</span><span class="n">value</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">e</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="nb">type</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">value</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="nb">list</span><span class="p">:</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">e</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">e</span><span class="o">.</span><span class="n">value</span><span class="o">.</span><span class="n">split</span><span class="p">()</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">e</span><span class="p">)</span> <span class="ow">is</span> <span class="n">Command</span> <span class="ow">or</span> <span class="nb">type</span><span class="p">(</span><span class="n">e</span><span class="p">)</span> <span class="ow">is</span> <span class="n">Option</span> <span class="ow">and</span> <span class="n">e</span><span class="o">.</span><span class="n">argcount</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">e</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span></div><div class='line' id='LC70'><br/></div><div class='line' id='LC71'><br/></div><div class='line' id='LC72'><span class="k">def</span> <span class="nf">transform</span><span class="p">(</span><span class="n">pattern</span><span class="p">):</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Expand pattern into an (almost) equivalent one, but with single Either.</span></div><div class='line' id='LC74'><br/></div><div class='line' id='LC75'><span class="sd">    Example: ((-a | -b) (-c | -d)) =&gt; (-a -c | -a -d | -b -c | -b -d)</span></div><div class='line' id='LC76'><span class="sd">    Quirks: [-a] =&gt; (-a), (-a...) =&gt; (-a -a)</span></div><div class='line' id='LC77'><br/></div><div class='line' id='LC78'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">groups</span> <span class="o">=</span> <span class="p">[[</span><span class="n">pattern</span><span class="p">]]</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="n">groups</span><span class="p">:</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">children</span> <span class="o">=</span> <span class="n">groups</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parents</span> <span class="o">=</span> <span class="p">[</span><span class="n">Required</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">OptionsShortcut</span><span class="p">,</span> <span class="n">Either</span><span class="p">,</span> <span class="n">OneOrMore</span><span class="p">]</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">any</span><span class="p">(</span><span class="n">t</span> <span class="ow">in</span> <span class="nb">map</span><span class="p">(</span><span class="nb">type</span><span class="p">,</span> <span class="n">children</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">parents</span><span class="p">):</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">child</span> <span class="o">=</span> <span class="p">[</span><span class="n">c</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">children</span> <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">c</span><span class="p">)</span> <span class="ow">in</span> <span class="n">parents</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">children</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">child</span><span class="p">)</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">child</span><span class="p">)</span> <span class="ow">is</span> <span class="n">Either</span><span class="p">:</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">child</span><span class="o">.</span><span class="n">children</span><span class="p">:</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">groups</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">c</span><span class="p">]</span> <span class="o">+</span> <span class="n">children</span><span class="p">)</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="nb">type</span><span class="p">(</span><span class="n">child</span><span class="p">)</span> <span class="ow">is</span> <span class="n">OneOrMore</span><span class="p">:</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">groups</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">child</span><span class="o">.</span><span class="n">children</span> <span class="o">*</span> <span class="mi">2</span> <span class="o">+</span> <span class="n">children</span><span class="p">)</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">groups</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">child</span><span class="o">.</span><span class="n">children</span> <span class="o">+</span> <span class="n">children</span><span class="p">)</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">children</span><span class="p">)</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Either</span><span class="p">(</span><span class="o">*</span><span class="p">[</span><span class="n">Required</span><span class="p">(</span><span class="o">*</span><span class="n">e</span><span class="p">)</span> <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">result</span><span class="p">])</span></div><div class='line' id='LC97'><br/></div><div class='line' id='LC98'><br/></div><div class='line' id='LC99'><span class="k">class</span> <span class="nc">LeafPattern</span><span class="p">(</span><span class="n">Pattern</span><span class="p">):</span></div><div class='line' id='LC100'><br/></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Leaf/terminal node of a pattern tree.&quot;&quot;&quot;</span></div><div class='line' id='LC102'><br/></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">value</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">name</span><span class="p">,</span> <span class="n">value</span></div><div class='line' id='LC105'><br/></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">(</span><span class="si">%r</span><span class="s">, </span><span class="si">%r</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__name__</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span></div><div class='line' id='LC108'><br/></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">flat</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">types</span><span class="p">):</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="p">]</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">types</span> <span class="ow">or</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="ow">in</span> <span class="n">types</span> <span class="k">else</span> <span class="p">[]</span></div><div class='line' id='LC111'><br/></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">match</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">collected</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">collected</span> <span class="o">=</span> <span class="p">[]</span> <span class="k">if</span> <span class="n">collected</span> <span class="ow">is</span> <span class="bp">None</span> <span class="k">else</span> <span class="n">collected</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pos</span><span class="p">,</span> <span class="n">match</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">single_match</span><span class="p">(</span><span class="n">left</span><span class="p">)</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">match</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">collected</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">left_</span> <span class="o">=</span> <span class="n">left</span><span class="p">[:</span><span class="n">pos</span><span class="p">]</span> <span class="o">+</span> <span class="n">left</span><span class="p">[</span><span class="n">pos</span> <span class="o">+</span> <span class="mi">1</span><span class="p">:]</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">same_name</span> <span class="o">=</span> <span class="p">[</span><span class="n">a</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">collected</span> <span class="k">if</span> <span class="n">a</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">]</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span> <span class="ow">in</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span> <span class="ow">is</span> <span class="nb">int</span><span class="p">:</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">increment</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">increment</span> <span class="o">=</span> <span class="p">([</span><span class="n">match</span><span class="o">.</span><span class="n">value</span><span class="p">]</span> <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">match</span><span class="o">.</span><span class="n">value</span><span class="p">)</span> <span class="ow">is</span> <span class="nb">str</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span> <span class="n">match</span><span class="o">.</span><span class="n">value</span><span class="p">)</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">same_name</span><span class="p">:</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">match</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">increment</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span><span class="p">,</span> <span class="n">left_</span><span class="p">,</span> <span class="n">collected</span> <span class="o">+</span> <span class="p">[</span><span class="n">match</span><span class="p">]</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">same_name</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">value</span> <span class="o">+=</span> <span class="n">increment</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span><span class="p">,</span> <span class="n">left_</span><span class="p">,</span> <span class="n">collected</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span><span class="p">,</span> <span class="n">left_</span><span class="p">,</span> <span class="n">collected</span> <span class="o">+</span> <span class="p">[</span><span class="n">match</span><span class="p">]</span></div><div class='line' id='LC131'><br/></div><div class='line' id='LC132'><br/></div><div class='line' id='LC133'><span class="k">class</span> <span class="nc">BranchPattern</span><span class="p">(</span><span class="n">Pattern</span><span class="p">):</span></div><div class='line' id='LC134'><br/></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Branch/inner node of a pattern tree.&quot;&quot;&quot;</span></div><div class='line' id='LC136'><br/></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">children</span><span class="p">):</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">children</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">children</span><span class="p">)</span></div><div class='line' id='LC139'><br/></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">(</span><span class="si">%s</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__name__</span><span class="p">,</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="n">a</span><span class="p">)</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">))</span></div><div class='line' id='LC143'><br/></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">flat</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">types</span><span class="p">):</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="ow">in</span> <span class="n">types</span><span class="p">:</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="p">]</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">sum</span><span class="p">([</span><span class="n">child</span><span class="o">.</span><span class="n">flat</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">)</span> <span class="k">for</span> <span class="n">child</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">],</span> <span class="p">[])</span></div><div class='line' id='LC148'><br/></div><div class='line' id='LC149'><br/></div><div class='line' id='LC150'><span class="k">class</span> <span class="nc">Argument</span><span class="p">(</span><span class="n">LeafPattern</span><span class="p">):</span></div><div class='line' id='LC151'><br/></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">single_match</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">left</span><span class="p">):</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">n</span><span class="p">,</span> <span class="n">pattern</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">left</span><span class="p">):</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">pattern</span><span class="p">)</span> <span class="ow">is</span> <span class="n">Argument</span><span class="p">:</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">n</span><span class="p">,</span> <span class="n">Argument</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">pattern</span><span class="o">.</span><span class="n">value</span><span class="p">)</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span></div><div class='line' id='LC157'><br/></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nd">@classmethod</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">class_</span><span class="p">,</span> <span class="n">source</span><span class="p">):</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="s">&#39;(&lt;\S*?&gt;)&#39;</span><span class="p">,</span> <span class="n">source</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">value</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="s">&#39;\[default: (.*)\]&#39;</span><span class="p">,</span> <span class="n">source</span><span class="p">,</span> <span class="n">flags</span><span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">I</span><span class="p">)</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">class_</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">value</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">value</span> <span class="k">else</span> <span class="bp">None</span><span class="p">)</span></div><div class='line' id='LC163'><br/></div><div class='line' id='LC164'><br/></div><div class='line' id='LC165'><span class="k">class</span> <span class="nc">Command</span><span class="p">(</span><span class="n">Argument</span><span class="p">):</span></div><div class='line' id='LC166'><br/></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">value</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">name</span><span class="p">,</span> <span class="n">value</span></div><div class='line' id='LC169'><br/></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">single_match</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">left</span><span class="p">):</span></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">n</span><span class="p">,</span> <span class="n">pattern</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">left</span><span class="p">):</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">pattern</span><span class="p">)</span> <span class="ow">is</span> <span class="n">Argument</span><span class="p">:</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">pattern</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">:</span></div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">n</span><span class="p">,</span> <span class="n">Command</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span></div><div class='line' id='LC178'><br/></div><div class='line' id='LC179'><br/></div><div class='line' id='LC180'><span class="k">class</span> <span class="nc">Option</span><span class="p">(</span><span class="n">LeafPattern</span><span class="p">):</span></div><div class='line' id='LC181'><br/></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">short</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="nb">long</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">argcount</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">value</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">argcount</span> <span class="ow">in</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">short</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">long</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">argcount</span> <span class="o">=</span> <span class="n">short</span><span class="p">,</span> <span class="nb">long</span><span class="p">,</span> <span class="n">argcount</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="bp">None</span> <span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="bp">False</span> <span class="ow">and</span> <span class="n">argcount</span> <span class="k">else</span> <span class="n">value</span></div><div class='line' id='LC186'><br/></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nd">@classmethod</span></div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">class_</span><span class="p">,</span> <span class="n">option_description</span><span class="p">):</span></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">short</span><span class="p">,</span> <span class="nb">long</span><span class="p">,</span> <span class="n">argcount</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="bp">False</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">options</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">description</span> <span class="o">=</span> <span class="n">option_description</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">partition</span><span class="p">(</span><span class="s">&#39;  &#39;</span><span class="p">)</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">options</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;,&#39;</span><span class="p">,</span> <span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;=&#39;</span><span class="p">,</span> <span class="s">&#39; &#39;</span><span class="p">)</span></div><div class='line' id='LC192'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">options</span><span class="o">.</span><span class="n">split</span><span class="p">():</span></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">s</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;--&#39;</span><span class="p">):</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">long</span> <span class="o">=</span> <span class="n">s</span></div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">s</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;-&#39;</span><span class="p">):</span></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">short</span> <span class="o">=</span> <span class="n">s</span></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">argcount</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC199'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">argcount</span><span class="p">:</span></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">matched</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="s">&#39;\[default: (.*)\]&#39;</span><span class="p">,</span> <span class="n">description</span><span class="p">,</span> <span class="n">flags</span><span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">I</span><span class="p">)</span></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">value</span> <span class="o">=</span> <span class="n">matched</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">matched</span> <span class="k">else</span> <span class="bp">None</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">class_</span><span class="p">(</span><span class="n">short</span><span class="p">,</span> <span class="nb">long</span><span class="p">,</span> <span class="n">argcount</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span></div><div class='line' id='LC203'><br/></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">single_match</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">left</span><span class="p">):</span></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">n</span><span class="p">,</span> <span class="n">pattern</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">left</span><span class="p">):</span></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="n">pattern</span><span class="o">.</span><span class="n">name</span><span class="p">:</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">n</span><span class="p">,</span> <span class="n">pattern</span></div><div class='line' id='LC208'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span></div><div class='line' id='LC209'><br/></div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nd">@property</span></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC212'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">long</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">short</span></div><div class='line' id='LC213'><br/></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;Option(</span><span class="si">%r</span><span class="s">, </span><span class="si">%r</span><span class="s">, </span><span class="si">%r</span><span class="s">, </span><span class="si">%r</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">short</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">long</span><span class="p">,</span></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">argcount</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span></div><div class='line' id='LC217'><br/></div><div class='line' id='LC218'><br/></div><div class='line' id='LC219'><span class="k">class</span> <span class="nc">Required</span><span class="p">(</span><span class="n">BranchPattern</span><span class="p">):</span></div><div class='line' id='LC220'><br/></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">match</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">collected</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">collected</span> <span class="o">=</span> <span class="p">[]</span> <span class="k">if</span> <span class="n">collected</span> <span class="ow">is</span> <span class="bp">None</span> <span class="k">else</span> <span class="n">collected</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">l</span> <span class="o">=</span> <span class="n">left</span></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">c</span> <span class="o">=</span> <span class="n">collected</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">pattern</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">:</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">matched</span><span class="p">,</span> <span class="n">l</span><span class="p">,</span> <span class="n">c</span> <span class="o">=</span> <span class="n">pattern</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">l</span><span class="p">,</span> <span class="n">c</span><span class="p">)</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">matched</span><span class="p">:</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">collected</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span><span class="p">,</span> <span class="n">l</span><span class="p">,</span> <span class="n">c</span></div><div class='line' id='LC230'><br/></div><div class='line' id='LC231'><br/></div><div class='line' id='LC232'><span class="k">class</span> <span class="nc">Optional</span><span class="p">(</span><span class="n">BranchPattern</span><span class="p">):</span></div><div class='line' id='LC233'><br/></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">match</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">collected</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">collected</span> <span class="o">=</span> <span class="p">[]</span> <span class="k">if</span> <span class="n">collected</span> <span class="ow">is</span> <span class="bp">None</span> <span class="k">else</span> <span class="n">collected</span></div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">pattern</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">:</span></div><div class='line' id='LC237'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">m</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">collected</span> <span class="o">=</span> <span class="n">pattern</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">left</span><span class="p">,</span> <span class="n">collected</span><span class="p">)</span></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">collected</span></div><div class='line' id='LC239'><br/></div><div class='line' id='LC240'><br/></div><div class='line' id='LC241'><span class="k">class</span> <span class="nc">OptionsShortcut</span><span class="p">(</span><span class="n">Optional</span><span class="p">):</span></div><div class='line' id='LC242'><br/></div><div class='line' id='LC243'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Marker/placeholder for [options] shortcut.&quot;&quot;&quot;</span></div><div class='line' id='LC244'><br/></div><div class='line' id='LC245'><br/></div><div class='line' id='LC246'><span class="k">class</span> <span class="nc">OneOrMore</span><span class="p">(</span><span class="n">BranchPattern</span><span class="p">):</span></div><div class='line' id='LC247'><br/></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">match</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">collected</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">collected</span> <span class="o">=</span> <span class="p">[]</span> <span class="k">if</span> <span class="n">collected</span> <span class="ow">is</span> <span class="bp">None</span> <span class="k">else</span> <span class="n">collected</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">l</span> <span class="o">=</span> <span class="n">left</span></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">c</span> <span class="o">=</span> <span class="n">collected</span></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">l_</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">matched</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">times</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="n">matched</span><span class="p">:</span></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># could it be that something didn&#39;t match but changed l or c?</span></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">matched</span><span class="p">,</span> <span class="n">l</span><span class="p">,</span> <span class="n">c</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">l</span><span class="p">,</span> <span class="n">c</span><span class="p">)</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">times</span> <span class="o">+=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">matched</span> <span class="k">else</span> <span class="mi">0</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">l_</span> <span class="o">==</span> <span class="n">l</span><span class="p">:</span></div><div class='line' id='LC261'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">l_</span> <span class="o">=</span> <span class="n">l</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">times</span> <span class="o">&gt;=</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span><span class="p">,</span> <span class="n">l</span><span class="p">,</span> <span class="n">c</span></div><div class='line' id='LC265'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">collected</span></div><div class='line' id='LC266'><br/></div><div class='line' id='LC267'><br/></div><div class='line' id='LC268'><span class="k">class</span> <span class="nc">Either</span><span class="p">(</span><span class="n">BranchPattern</span><span class="p">):</span></div><div class='line' id='LC269'><br/></div><div class='line' id='LC270'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">match</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">collected</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">collected</span> <span class="o">=</span> <span class="p">[]</span> <span class="k">if</span> <span class="n">collected</span> <span class="ow">is</span> <span class="bp">None</span> <span class="k">else</span> <span class="n">collected</span></div><div class='line' id='LC272'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">outcomes</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC273'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">pattern</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">:</span></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">matched</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">outcome</span> <span class="o">=</span> <span class="n">pattern</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">left</span><span class="p">,</span> <span class="n">collected</span><span class="p">)</span></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">matched</span><span class="p">:</span></div><div class='line' id='LC276'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">outcomes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">outcome</span><span class="p">)</span></div><div class='line' id='LC277'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">outcomes</span><span class="p">:</span></div><div class='line' id='LC278'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">min</span><span class="p">(</span><span class="n">outcomes</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">outcome</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">outcome</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span></div><div class='line' id='LC279'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">collected</span></div><div class='line' id='LC280'><br/></div><div class='line' id='LC281'><br/></div><div class='line' id='LC282'><span class="k">class</span> <span class="nc">Tokens</span><span class="p">(</span><span class="nb">list</span><span class="p">):</span></div><div class='line' id='LC283'><br/></div><div class='line' id='LC284'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">source</span><span class="p">,</span> <span class="n">error</span><span class="o">=</span><span class="n">DocoptExit</span><span class="p">):</span></div><div class='line' id='LC285'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span> <span class="o">+=</span> <span class="n">source</span><span class="o">.</span><span class="n">split</span><span class="p">()</span> <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="s">&#39;split&#39;</span><span class="p">)</span> <span class="k">else</span> <span class="n">source</span></div><div class='line' id='LC286'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">error</span> <span class="o">=</span> <span class="n">error</span></div><div class='line' id='LC287'><br/></div><div class='line' id='LC288'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nd">@staticmethod</span></div><div class='line' id='LC289'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">from_pattern</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></div><div class='line' id='LC290'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">r&#39;([\[\]\(\)\|]|\.\.\.)&#39;</span><span class="p">,</span> <span class="s">r&#39; \1 &#39;</span><span class="p">,</span> <span class="n">source</span><span class="p">)</span></div><div class='line' id='LC291'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span> <span class="o">=</span> <span class="p">[</span><span class="n">s</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">re</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;\s+|(\S*&lt;.*?&gt;)&#39;</span><span class="p">,</span> <span class="n">source</span><span class="p">)</span> <span class="k">if</span> <span class="n">s</span><span class="p">]</span></div><div class='line' id='LC292'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Tokens</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">error</span><span class="o">=</span><span class="n">DocoptLanguageError</span><span class="p">)</span></div><div class='line' id='LC293'><br/></div><div class='line' id='LC294'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">move</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC295'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="k">else</span> <span class="bp">None</span></div><div class='line' id='LC296'><br/></div><div class='line' id='LC297'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">current</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC298'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="k">else</span> <span class="bp">None</span></div><div class='line' id='LC299'><br/></div><div class='line' id='LC300'><br/></div><div class='line' id='LC301'><span class="k">def</span> <span class="nf">parse_long</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">):</span></div><div class='line' id='LC302'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;long ::= &#39;--&#39; chars [ ( &#39; &#39; | &#39;=&#39; ) chars ] ;&quot;&quot;&quot;</span></div><div class='line' id='LC303'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">long</span><span class="p">,</span> <span class="n">eq</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="n">tokens</span><span class="o">.</span><span class="n">move</span><span class="p">()</span><span class="o">.</span><span class="n">partition</span><span class="p">(</span><span class="s">&#39;=&#39;</span><span class="p">)</span></div><div class='line' id='LC304'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="nb">long</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;--&#39;</span><span class="p">)</span></div><div class='line' id='LC305'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">value</span> <span class="o">=</span> <span class="bp">None</span> <span class="k">if</span> <span class="n">eq</span> <span class="o">==</span> <span class="n">value</span> <span class="o">==</span> <span class="s">&#39;&#39;</span> <span class="k">else</span> <span class="n">value</span></div><div class='line' id='LC306'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">similar</span> <span class="o">=</span> <span class="p">[</span><span class="n">o</span> <span class="k">for</span> <span class="n">o</span> <span class="ow">in</span> <span class="n">options</span> <span class="k">if</span> <span class="n">o</span><span class="o">.</span><span class="n">long</span> <span class="o">==</span> <span class="nb">long</span><span class="p">]</span></div><div class='line' id='LC307'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tokens</span><span class="o">.</span><span class="n">error</span> <span class="ow">is</span> <span class="n">DocoptExit</span> <span class="ow">and</span> <span class="n">similar</span> <span class="o">==</span> <span class="p">[]:</span>  <span class="c"># if no exact match</span></div><div class='line' id='LC308'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">similar</span> <span class="o">=</span> <span class="p">[</span><span class="n">o</span> <span class="k">for</span> <span class="n">o</span> <span class="ow">in</span> <span class="n">options</span> <span class="k">if</span> <span class="n">o</span><span class="o">.</span><span class="n">long</span> <span class="ow">and</span> <span class="n">o</span><span class="o">.</span><span class="n">long</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="nb">long</span><span class="p">)]</span></div><div class='line' id='LC309'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">similar</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>  <span class="c"># might be simply specified ambiguously 2+ times?</span></div><div class='line' id='LC310'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">tokens</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s"> is not a unique prefix: </span><span class="si">%s</span><span class="s">?&#39;</span> <span class="o">%</span></div><div class='line' id='LC311'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="nb">long</span><span class="p">,</span> <span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">o</span><span class="o">.</span><span class="n">long</span> <span class="k">for</span> <span class="n">o</span> <span class="ow">in</span> <span class="n">similar</span><span class="p">)))</span></div><div class='line' id='LC312'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">similar</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC313'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">argcount</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">eq</span> <span class="o">==</span> <span class="s">&#39;=&#39;</span> <span class="k">else</span> <span class="mi">0</span></div><div class='line' id='LC314'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">o</span> <span class="o">=</span> <span class="n">Option</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="nb">long</span><span class="p">,</span> <span class="n">argcount</span><span class="p">)</span></div><div class='line' id='LC315'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">options</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">o</span><span class="p">)</span></div><div class='line' id='LC316'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tokens</span><span class="o">.</span><span class="n">error</span> <span class="ow">is</span> <span class="n">DocoptExit</span><span class="p">:</span></div><div class='line' id='LC317'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">o</span> <span class="o">=</span> <span class="n">Option</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="nb">long</span><span class="p">,</span> <span class="n">argcount</span><span class="p">,</span> <span class="n">value</span> <span class="k">if</span> <span class="n">argcount</span> <span class="k">else</span> <span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC318'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC319'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">o</span> <span class="o">=</span> <span class="n">Option</span><span class="p">(</span><span class="n">similar</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">short</span><span class="p">,</span> <span class="n">similar</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">long</span><span class="p">,</span></div><div class='line' id='LC320'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">similar</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">argcount</span><span class="p">,</span> <span class="n">similar</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">value</span><span class="p">)</span></div><div class='line' id='LC321'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">o</span><span class="o">.</span><span class="n">argcount</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC322'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC323'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">tokens</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s"> must not have an argument&#39;</span> <span class="o">%</span> <span class="n">o</span><span class="o">.</span><span class="n">long</span><span class="p">)</span></div><div class='line' id='LC324'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC325'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tokens</span><span class="o">.</span><span class="n">current</span><span class="p">()</span> <span class="ow">in</span> <span class="p">[</span><span class="bp">None</span><span class="p">,</span> <span class="s">&#39;--&#39;</span><span class="p">]:</span></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">tokens</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s"> requires argument&#39;</span> <span class="o">%</span> <span class="n">o</span><span class="o">.</span><span class="n">long</span><span class="p">)</span></div><div class='line' id='LC328'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">value</span> <span class="o">=</span> <span class="n">tokens</span><span class="o">.</span><span class="n">move</span><span class="p">()</span></div><div class='line' id='LC329'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tokens</span><span class="o">.</span><span class="n">error</span> <span class="ow">is</span> <span class="n">DocoptExit</span><span class="p">:</span></div><div class='line' id='LC330'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">o</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span> <span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="k">else</span> <span class="bp">True</span></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">o</span><span class="p">]</span></div><div class='line' id='LC332'><br/></div><div class='line' id='LC333'><br/></div><div class='line' id='LC334'><span class="k">def</span> <span class="nf">parse_shorts</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">):</span></div><div class='line' id='LC335'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;shorts ::= &#39;-&#39; ( chars )* [ [ &#39; &#39; ] chars ] ;&quot;&quot;&quot;</span></div><div class='line' id='LC336'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span> <span class="o">=</span> <span class="n">tokens</span><span class="o">.</span><span class="n">move</span><span class="p">()</span></div><div class='line' id='LC337'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">token</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;-&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">token</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;--&#39;</span><span class="p">)</span></div><div class='line' id='LC338'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">left</span> <span class="o">=</span> <span class="n">token</span><span class="o">.</span><span class="n">lstrip</span><span class="p">(</span><span class="s">&#39;-&#39;</span><span class="p">)</span></div><div class='line' id='LC339'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parsed</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC340'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="n">left</span> <span class="o">!=</span> <span class="s">&#39;&#39;</span><span class="p">:</span></div><div class='line' id='LC341'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">short</span><span class="p">,</span> <span class="n">left</span> <span class="o">=</span> <span class="s">&#39;-&#39;</span> <span class="o">+</span> <span class="n">left</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">left</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span></div><div class='line' id='LC342'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">similar</span> <span class="o">=</span> <span class="p">[</span><span class="n">o</span> <span class="k">for</span> <span class="n">o</span> <span class="ow">in</span> <span class="n">options</span> <span class="k">if</span> <span class="n">o</span><span class="o">.</span><span class="n">short</span> <span class="o">==</span> <span class="n">short</span><span class="p">]</span></div><div class='line' id='LC343'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">similar</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC344'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">tokens</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s"> is specified ambiguously </span><span class="si">%d</span><span class="s"> times&#39;</span> <span class="o">%</span></div><div class='line' id='LC345'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="n">short</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">similar</span><span class="p">)))</span></div><div class='line' id='LC346'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">similar</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC347'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">o</span> <span class="o">=</span> <span class="n">Option</span><span class="p">(</span><span class="n">short</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC348'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">options</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">o</span><span class="p">)</span></div><div class='line' id='LC349'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tokens</span><span class="o">.</span><span class="n">error</span> <span class="ow">is</span> <span class="n">DocoptExit</span><span class="p">:</span></div><div class='line' id='LC350'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">o</span> <span class="o">=</span> <span class="n">Option</span><span class="p">(</span><span class="n">short</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC351'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span>  <span class="c"># why copying is necessary here?</span></div><div class='line' id='LC352'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">o</span> <span class="o">=</span> <span class="n">Option</span><span class="p">(</span><span class="n">short</span><span class="p">,</span> <span class="n">similar</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">long</span><span class="p">,</span></div><div class='line' id='LC353'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">similar</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">argcount</span><span class="p">,</span> <span class="n">similar</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">value</span><span class="p">)</span></div><div class='line' id='LC354'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">value</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC355'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">o</span><span class="o">.</span><span class="n">argcount</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC356'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">left</span> <span class="o">==</span> <span class="s">&#39;&#39;</span><span class="p">:</span></div><div class='line' id='LC357'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tokens</span><span class="o">.</span><span class="n">current</span><span class="p">()</span> <span class="ow">in</span> <span class="p">[</span><span class="bp">None</span><span class="p">,</span> <span class="s">&#39;--&#39;</span><span class="p">]:</span></div><div class='line' id='LC358'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">tokens</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s"> requires argument&#39;</span> <span class="o">%</span> <span class="n">short</span><span class="p">)</span></div><div class='line' id='LC359'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">value</span> <span class="o">=</span> <span class="n">tokens</span><span class="o">.</span><span class="n">move</span><span class="p">()</span></div><div class='line' id='LC360'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC361'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">value</span> <span class="o">=</span> <span class="n">left</span></div><div class='line' id='LC362'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">left</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC363'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tokens</span><span class="o">.</span><span class="n">error</span> <span class="ow">is</span> <span class="n">DocoptExit</span><span class="p">:</span></div><div class='line' id='LC364'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">o</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span> <span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="k">else</span> <span class="bp">True</span></div><div class='line' id='LC365'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parsed</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">o</span><span class="p">)</span></div><div class='line' id='LC366'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">parsed</span></div><div class='line' id='LC367'><br/></div><div class='line' id='LC368'><br/></div><div class='line' id='LC369'><span class="k">def</span> <span class="nf">parse_pattern</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">options</span><span class="p">):</span></div><div class='line' id='LC370'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tokens</span> <span class="o">=</span> <span class="n">Tokens</span><span class="o">.</span><span class="n">from_pattern</span><span class="p">(</span><span class="n">source</span><span class="p">)</span></div><div class='line' id='LC371'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="n">parse_expr</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">)</span></div><div class='line' id='LC372'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tokens</span><span class="o">.</span><span class="n">current</span><span class="p">()</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC373'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">tokens</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&#39;unexpected ending: </span><span class="si">%r</span><span class="s">&#39;</span> <span class="o">%</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">tokens</span><span class="p">))</span></div><div class='line' id='LC374'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Required</span><span class="p">(</span><span class="o">*</span><span class="n">result</span><span class="p">)</span></div><div class='line' id='LC375'><br/></div><div class='line' id='LC376'><br/></div><div class='line' id='LC377'><span class="k">def</span> <span class="nf">parse_expr</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">):</span></div><div class='line' id='LC378'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;expr ::= seq ( &#39;|&#39; seq )* ;&quot;&quot;&quot;</span></div><div class='line' id='LC379'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seq</span> <span class="o">=</span> <span class="n">parse_seq</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">)</span></div><div class='line' id='LC380'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tokens</span><span class="o">.</span><span class="n">current</span><span class="p">()</span> <span class="o">!=</span> <span class="s">&#39;|&#39;</span><span class="p">:</span></div><div class='line' id='LC381'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">seq</span></div><div class='line' id='LC382'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="p">[</span><span class="n">Required</span><span class="p">(</span><span class="o">*</span><span class="n">seq</span><span class="p">)]</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">seq</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="k">else</span> <span class="n">seq</span></div><div class='line' id='LC383'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="n">tokens</span><span class="o">.</span><span class="n">current</span><span class="p">()</span> <span class="o">==</span> <span class="s">&#39;|&#39;</span><span class="p">:</span></div><div class='line' id='LC384'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tokens</span><span class="o">.</span><span class="n">move</span><span class="p">()</span></div><div class='line' id='LC385'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seq</span> <span class="o">=</span> <span class="n">parse_seq</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">)</span></div><div class='line' id='LC386'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">+=</span> <span class="p">[</span><span class="n">Required</span><span class="p">(</span><span class="o">*</span><span class="n">seq</span><span class="p">)]</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">seq</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="k">else</span> <span class="n">seq</span></div><div class='line' id='LC387'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">Either</span><span class="p">(</span><span class="o">*</span><span class="n">result</span><span class="p">)]</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">result</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="k">else</span> <span class="n">result</span></div><div class='line' id='LC388'><br/></div><div class='line' id='LC389'><br/></div><div class='line' id='LC390'><span class="k">def</span> <span class="nf">parse_seq</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">):</span></div><div class='line' id='LC391'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;seq ::= ( atom [ &#39;...&#39; ] )* ;&quot;&quot;&quot;</span></div><div class='line' id='LC392'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC393'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="n">tokens</span><span class="o">.</span><span class="n">current</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">[</span><span class="bp">None</span><span class="p">,</span> <span class="s">&#39;]&#39;</span><span class="p">,</span> <span class="s">&#39;)&#39;</span><span class="p">,</span> <span class="s">&#39;|&#39;</span><span class="p">]:</span></div><div class='line' id='LC394'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">atom</span> <span class="o">=</span> <span class="n">parse_atom</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">)</span></div><div class='line' id='LC395'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tokens</span><span class="o">.</span><span class="n">current</span><span class="p">()</span> <span class="o">==</span> <span class="s">&#39;...&#39;</span><span class="p">:</span></div><div class='line' id='LC396'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">atom</span> <span class="o">=</span> <span class="p">[</span><span class="n">OneOrMore</span><span class="p">(</span><span class="o">*</span><span class="n">atom</span><span class="p">)]</span></div><div class='line' id='LC397'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tokens</span><span class="o">.</span><span class="n">move</span><span class="p">()</span></div><div class='line' id='LC398'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">+=</span> <span class="n">atom</span></div><div class='line' id='LC399'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">result</span></div><div class='line' id='LC400'><br/></div><div class='line' id='LC401'><br/></div><div class='line' id='LC402'><span class="k">def</span> <span class="nf">parse_atom</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">):</span></div><div class='line' id='LC403'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;atom ::= &#39;(&#39; expr &#39;)&#39; | &#39;[&#39; expr &#39;]&#39; | &#39;options&#39;</span></div><div class='line' id='LC404'><span class="sd">             | long | shorts | argument | command ;</span></div><div class='line' id='LC405'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC406'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span> <span class="o">=</span> <span class="n">tokens</span><span class="o">.</span><span class="n">current</span><span class="p">()</span></div><div class='line' id='LC407'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC408'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">token</span> <span class="ow">in</span> <span class="s">&#39;([&#39;</span><span class="p">:</span></div><div class='line' id='LC409'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tokens</span><span class="o">.</span><span class="n">move</span><span class="p">()</span></div><div class='line' id='LC410'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">matching</span><span class="p">,</span> <span class="n">pattern</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;(&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s">&#39;)&#39;</span><span class="p">,</span> <span class="n">Required</span><span class="p">],</span> <span class="s">&#39;[&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s">&#39;]&#39;</span><span class="p">,</span> <span class="n">Optional</span><span class="p">]}[</span><span class="n">token</span><span class="p">]</span></div><div class='line' id='LC411'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="n">pattern</span><span class="p">(</span><span class="o">*</span><span class="n">parse_expr</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">))</span></div><div class='line' id='LC412'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tokens</span><span class="o">.</span><span class="n">move</span><span class="p">()</span> <span class="o">!=</span> <span class="n">matching</span><span class="p">:</span></div><div class='line' id='LC413'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">tokens</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&quot;unmatched &#39;</span><span class="si">%s</span><span class="s">&#39;&quot;</span> <span class="o">%</span> <span class="n">token</span><span class="p">)</span></div><div class='line' id='LC414'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">result</span><span class="p">]</span></div><div class='line' id='LC415'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">token</span> <span class="o">==</span> <span class="s">&#39;options&#39;</span><span class="p">:</span></div><div class='line' id='LC416'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tokens</span><span class="o">.</span><span class="n">move</span><span class="p">()</span></div><div class='line' id='LC417'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">OptionsShortcut</span><span class="p">()]</span></div><div class='line' id='LC418'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">token</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;--&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="n">token</span> <span class="o">!=</span> <span class="s">&#39;--&#39;</span><span class="p">:</span></div><div class='line' id='LC419'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">parse_long</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">)</span></div><div class='line' id='LC420'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">token</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;-&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="n">token</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&#39;-&#39;</span><span class="p">,</span> <span class="s">&#39;--&#39;</span><span class="p">):</span></div><div class='line' id='LC421'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">parse_shorts</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">)</span></div><div class='line' id='LC422'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">token</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;&lt;&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="n">token</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;&gt;&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="n">token</span><span class="o">.</span><span class="n">isupper</span><span class="p">():</span></div><div class='line' id='LC423'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">Argument</span><span class="p">(</span><span class="n">tokens</span><span class="o">.</span><span class="n">move</span><span class="p">())]</span></div><div class='line' id='LC424'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC425'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">Command</span><span class="p">(</span><span class="n">tokens</span><span class="o">.</span><span class="n">move</span><span class="p">())]</span></div><div class='line' id='LC426'><br/></div><div class='line' id='LC427'><br/></div><div class='line' id='LC428'><span class="k">def</span> <span class="nf">parse_argv</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">,</span> <span class="n">options_first</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC429'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Parse command-line argument vector.</span></div><div class='line' id='LC430'><br/></div><div class='line' id='LC431'><span class="sd">    If options_first:</span></div><div class='line' id='LC432'><span class="sd">        argv ::= [ long | shorts ]* [ argument ]* [ &#39;--&#39; [ argument ]* ] ;</span></div><div class='line' id='LC433'><span class="sd">    else:</span></div><div class='line' id='LC434'><span class="sd">        argv ::= [ long | shorts | argument ]* [ &#39;--&#39; [ argument ]* ] ;</span></div><div class='line' id='LC435'><br/></div><div class='line' id='LC436'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC437'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parsed</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC438'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="n">tokens</span><span class="o">.</span><span class="n">current</span><span class="p">()</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC439'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tokens</span><span class="o">.</span><span class="n">current</span><span class="p">()</span> <span class="o">==</span> <span class="s">&#39;--&#39;</span><span class="p">:</span></div><div class='line' id='LC440'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">parsed</span> <span class="o">+</span> <span class="p">[</span><span class="n">Argument</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">tokens</span><span class="p">]</span></div><div class='line' id='LC441'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">tokens</span><span class="o">.</span><span class="n">current</span><span class="p">()</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;--&#39;</span><span class="p">):</span></div><div class='line' id='LC442'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parsed</span> <span class="o">+=</span> <span class="n">parse_long</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">)</span></div><div class='line' id='LC443'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">tokens</span><span class="o">.</span><span class="n">current</span><span class="p">()</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;-&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="n">tokens</span><span class="o">.</span><span class="n">current</span><span class="p">()</span> <span class="o">!=</span> <span class="s">&#39;-&#39;</span><span class="p">:</span></div><div class='line' id='LC444'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parsed</span> <span class="o">+=</span> <span class="n">parse_shorts</span><span class="p">(</span><span class="n">tokens</span><span class="p">,</span> <span class="n">options</span><span class="p">)</span></div><div class='line' id='LC445'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">options_first</span><span class="p">:</span></div><div class='line' id='LC446'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">parsed</span> <span class="o">+</span> <span class="p">[</span><span class="n">Argument</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">tokens</span><span class="p">]</span></div><div class='line' id='LC447'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC448'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parsed</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Argument</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="n">tokens</span><span class="o">.</span><span class="n">move</span><span class="p">()))</span></div><div class='line' id='LC449'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">parsed</span></div><div class='line' id='LC450'><br/></div><div class='line' id='LC451'><br/></div><div class='line' id='LC452'><span class="k">def</span> <span class="nf">parse_defaults</span><span class="p">(</span><span class="n">doc</span><span class="p">):</span></div><div class='line' id='LC453'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">defaults</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC454'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">parse_section</span><span class="p">(</span><span class="s">&#39;options:&#39;</span><span class="p">,</span> <span class="n">doc</span><span class="p">):</span></div><div class='line' id='LC455'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># FIXME corner case &quot;bla: options: --foo&quot;</span></div><div class='line' id='LC456'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">partition</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)</span>  <span class="c"># get rid of &quot;options:&quot;</span></div><div class='line' id='LC457'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">split</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s"> *(-\S+?)&#39;</span><span class="p">,</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">+</span> <span class="n">s</span><span class="p">)[</span><span class="mi">1</span><span class="p">:]</span></div><div class='line' id='LC458'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">split</span> <span class="o">=</span> <span class="p">[</span><span class="n">s1</span> <span class="o">+</span> <span class="n">s2</span> <span class="k">for</span> <span class="n">s1</span><span class="p">,</span> <span class="n">s2</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">split</span><span class="p">[::</span><span class="mi">2</span><span class="p">],</span> <span class="n">split</span><span class="p">[</span><span class="mi">1</span><span class="p">::</span><span class="mi">2</span><span class="p">])]</span></div><div class='line' id='LC459'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">options</span> <span class="o">=</span> <span class="p">[</span><span class="n">Option</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">s</span><span class="p">)</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">split</span> <span class="k">if</span> <span class="n">s</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;-&#39;</span><span class="p">)]</span></div><div class='line' id='LC460'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">defaults</span> <span class="o">+=</span> <span class="n">options</span></div><div class='line' id='LC461'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">defaults</span></div><div class='line' id='LC462'><br/></div><div class='line' id='LC463'><br/></div><div class='line' id='LC464'><span class="k">def</span> <span class="nf">parse_section</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">source</span><span class="p">):</span></div><div class='line' id='LC465'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pattern</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">&#39;^([^</span><span class="se">\n</span><span class="s">]*&#39;</span> <span class="o">+</span> <span class="n">name</span> <span class="o">+</span> <span class="s">&#39;[^</span><span class="se">\n</span><span class="s">]*</span><span class="se">\n</span><span class="s">?(?:[ </span><span class="se">\t</span><span class="s">].*?(?:</span><span class="se">\n</span><span class="s">|$))*)&#39;</span><span class="p">,</span></div><div class='line' id='LC466'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">re</span><span class="o">.</span><span class="n">IGNORECASE</span> <span class="o">|</span> <span class="n">re</span><span class="o">.</span><span class="n">MULTILINE</span><span class="p">)</span></div><div class='line' id='LC467'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">s</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">pattern</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="n">source</span><span class="p">)]</span></div><div class='line' id='LC468'><br/></div><div class='line' id='LC469'><br/></div><div class='line' id='LC470'><span class="k">def</span> <span class="nf">formal_usage</span><span class="p">(</span><span class="n">section</span><span class="p">):</span></div><div class='line' id='LC471'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">section</span> <span class="o">=</span> <span class="n">section</span><span class="o">.</span><span class="n">partition</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)</span>  <span class="c"># drop &quot;usage:&quot;</span></div><div class='line' id='LC472'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pu</span> <span class="o">=</span> <span class="n">section</span><span class="o">.</span><span class="n">split</span><span class="p">()</span></div><div class='line' id='LC473'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;( &#39;</span> <span class="o">+</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s">&#39;) | (&#39;</span> <span class="k">if</span> <span class="n">s</span> <span class="o">==</span> <span class="n">pu</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">else</span> <span class="n">s</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">pu</span><span class="p">[</span><span class="mi">1</span><span class="p">:])</span> <span class="o">+</span> <span class="s">&#39; )&#39;</span></div><div class='line' id='LC474'><br/></div><div class='line' id='LC475'><br/></div><div class='line' id='LC476'><span class="k">def</span> <span class="nf">extras</span><span class="p">(</span><span class="n">help</span><span class="p">,</span> <span class="n">version</span><span class="p">,</span> <span class="n">options</span><span class="p">,</span> <span class="n">doc</span><span class="p">):</span></div><div class='line' id='LC477'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">help</span> <span class="ow">and</span> <span class="nb">any</span><span class="p">((</span><span class="n">o</span><span class="o">.</span><span class="n">name</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&#39;-h&#39;</span><span class="p">,</span> <span class="s">&#39;--help&#39;</span><span class="p">))</span> <span class="ow">and</span> <span class="n">o</span><span class="o">.</span><span class="n">value</span> <span class="k">for</span> <span class="n">o</span> <span class="ow">in</span> <span class="n">options</span><span class="p">):</span></div><div class='line' id='LC478'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="n">doc</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">))</span></div><div class='line' id='LC479'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">()</span></div><div class='line' id='LC480'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">version</span> <span class="ow">and</span> <span class="nb">any</span><span class="p">(</span><span class="n">o</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="s">&#39;--version&#39;</span> <span class="ow">and</span> <span class="n">o</span><span class="o">.</span><span class="n">value</span> <span class="k">for</span> <span class="n">o</span> <span class="ow">in</span> <span class="n">options</span><span class="p">):</span></div><div class='line' id='LC481'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="n">version</span><span class="p">)</span></div><div class='line' id='LC482'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">()</span></div><div class='line' id='LC483'><br/></div><div class='line' id='LC484'><br/></div><div class='line' id='LC485'><span class="k">class</span> <span class="nc">Dict</span><span class="p">(</span><span class="nb">dict</span><span class="p">):</span></div><div class='line' id='LC486'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC487'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;{</span><span class="si">%s</span><span class="s">}&#39;</span> <span class="o">%</span> <span class="s">&#39;,</span><span class="se">\n</span><span class="s"> &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%r</span><span class="s">: </span><span class="si">%r</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">i</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">items</span><span class="p">()))</span></div><div class='line' id='LC488'><br/></div><div class='line' id='LC489'><br/></div><div class='line' id='LC490'><span class="k">def</span> <span class="nf">docopt</span><span class="p">(</span><span class="n">doc</span><span class="p">,</span> <span class="n">argv</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">version</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">options_first</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC491'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Parse `argv` based on command-line interface described in `doc`.</span></div><div class='line' id='LC492'><br/></div><div class='line' id='LC493'><span class="sd">    `docopt` creates your command-line interface based on its</span></div><div class='line' id='LC494'><span class="sd">    description that you pass as `doc`. Such description can contain</span></div><div class='line' id='LC495'><span class="sd">    --options, &lt;positional-argument&gt;, commands, which could be</span></div><div class='line' id='LC496'><span class="sd">    [optional], (required), (mutually | exclusive) or repeated...</span></div><div class='line' id='LC497'><br/></div><div class='line' id='LC498'><span class="sd">    Parameters</span></div><div class='line' id='LC499'><span class="sd">    ----------</span></div><div class='line' id='LC500'><span class="sd">    doc : str</span></div><div class='line' id='LC501'><span class="sd">        Description of your command-line interface.</span></div><div class='line' id='LC502'><span class="sd">    argv : list of str, optional</span></div><div class='line' id='LC503'><span class="sd">        Argument vector to be parsed. sys.argv[1:] is used if not</span></div><div class='line' id='LC504'><span class="sd">        provided.</span></div><div class='line' id='LC505'><span class="sd">    help : bool (default: True)</span></div><div class='line' id='LC506'><span class="sd">        Set to False to disable automatic help on -h or --help</span></div><div class='line' id='LC507'><span class="sd">        options.</span></div><div class='line' id='LC508'><span class="sd">    version : any object</span></div><div class='line' id='LC509'><span class="sd">        If passed, the object will be printed if --version is in</span></div><div class='line' id='LC510'><span class="sd">        `argv`.</span></div><div class='line' id='LC511'><span class="sd">    options_first : bool (default: False)</span></div><div class='line' id='LC512'><span class="sd">        Set to True to require options precede positional arguments,</span></div><div class='line' id='LC513'><span class="sd">        i.e. to forbid options and positional arguments intermix.</span></div><div class='line' id='LC514'><br/></div><div class='line' id='LC515'><span class="sd">    Returns</span></div><div class='line' id='LC516'><span class="sd">    -------</span></div><div class='line' id='LC517'><span class="sd">    args : dict</span></div><div class='line' id='LC518'><span class="sd">        A dictionary, where keys are names of command-line elements</span></div><div class='line' id='LC519'><span class="sd">        such as e.g. &quot;--verbose&quot; and &quot;&lt;path&gt;&quot;, and values are the</span></div><div class='line' id='LC520'><span class="sd">        parsed values of those elements.</span></div><div class='line' id='LC521'><br/></div><div class='line' id='LC522'><span class="sd">    Example</span></div><div class='line' id='LC523'><span class="sd">    -------</span></div><div class='line' id='LC524'><span class="sd">    &gt;&gt;&gt; from docopt import docopt</span></div><div class='line' id='LC525'><span class="sd">    &gt;&gt;&gt; doc = &#39;&#39;&#39;</span></div><div class='line' id='LC526'><span class="sd">    ... Usage:</span></div><div class='line' id='LC527'><span class="sd">    ...     my_program tcp &lt;host&gt; &lt;port&gt; [--timeout=&lt;seconds&gt;]</span></div><div class='line' id='LC528'><span class="sd">    ...     my_program serial &lt;port&gt; [--baud=&lt;n&gt;] [--timeout=&lt;seconds&gt;]</span></div><div class='line' id='LC529'><span class="sd">    ...     my_program (-h | --help | --version)</span></div><div class='line' id='LC530'><span class="sd">    ...</span></div><div class='line' id='LC531'><span class="sd">    ... Options:</span></div><div class='line' id='LC532'><span class="sd">    ...     -h, --help  Show this screen and exit.</span></div><div class='line' id='LC533'><span class="sd">    ...     --baud=&lt;n&gt;  Baudrate [default: 9600]</span></div><div class='line' id='LC534'><span class="sd">    ... &#39;&#39;&#39;</span></div><div class='line' id='LC535'><span class="sd">    &gt;&gt;&gt; argv = [&#39;tcp&#39;, &#39;127.0.0.1&#39;, &#39;80&#39;, &#39;--timeout&#39;, &#39;30&#39;]</span></div><div class='line' id='LC536'><span class="sd">    &gt;&gt;&gt; docopt(doc, argv)</span></div><div class='line' id='LC537'><span class="sd">    {&#39;--baud&#39;: &#39;9600&#39;,</span></div><div class='line' id='LC538'><span class="sd">     &#39;--help&#39;: False,</span></div><div class='line' id='LC539'><span class="sd">     &#39;--timeout&#39;: &#39;30&#39;,</span></div><div class='line' id='LC540'><span class="sd">     &#39;--version&#39;: False,</span></div><div class='line' id='LC541'><span class="sd">     &#39;&lt;host&gt;&#39;: &#39;127.0.0.1&#39;,</span></div><div class='line' id='LC542'><span class="sd">     &#39;&lt;port&gt;&#39;: &#39;80&#39;,</span></div><div class='line' id='LC543'><span class="sd">     &#39;serial&#39;: False,</span></div><div class='line' id='LC544'><span class="sd">     &#39;tcp&#39;: True}</span></div><div class='line' id='LC545'><br/></div><div class='line' id='LC546'><span class="sd">    See also</span></div><div class='line' id='LC547'><span class="sd">    --------</span></div><div class='line' id='LC548'><span class="sd">    * For video introduction see http://docopt.org</span></div><div class='line' id='LC549'><span class="sd">    * Full documentation is available in README.rst as well as online</span></div><div class='line' id='LC550'><span class="sd">      at https://github.com/docopt/docopt#readme</span></div><div class='line' id='LC551'><br/></div><div class='line' id='LC552'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC553'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">argv</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span> <span class="k">if</span> <span class="n">argv</span> <span class="ow">is</span> <span class="bp">None</span> <span class="k">else</span> <span class="n">argv</span></div><div class='line' id='LC554'><br/></div><div class='line' id='LC555'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">usage_sections</span> <span class="o">=</span> <span class="n">parse_section</span><span class="p">(</span><span class="s">&#39;usage:&#39;</span><span class="p">,</span> <span class="n">doc</span><span class="p">)</span></div><div class='line' id='LC556'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">usage_sections</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC557'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">DocoptLanguageError</span><span class="p">(</span><span class="s">&#39;&quot;usage:&quot; (case-insensitive) not found.&#39;</span><span class="p">)</span></div><div class='line' id='LC558'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">usage_sections</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC559'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">DocoptLanguageError</span><span class="p">(</span><span class="s">&#39;More than one &quot;usage:&quot; (case-insensitive).&#39;</span><span class="p">)</span></div><div class='line' id='LC560'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">DocoptExit</span><span class="o">.</span><span class="n">usage</span> <span class="o">=</span> <span class="n">usage_sections</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC561'><br/></div><div class='line' id='LC562'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">options</span> <span class="o">=</span> <span class="n">parse_defaults</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span></div><div class='line' id='LC563'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pattern</span> <span class="o">=</span> <span class="n">parse_pattern</span><span class="p">(</span><span class="n">formal_usage</span><span class="p">(</span><span class="n">DocoptExit</span><span class="o">.</span><span class="n">usage</span><span class="p">),</span> <span class="n">options</span><span class="p">)</span></div><div class='line' id='LC564'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># [default] syntax for argument is disabled</span></div><div class='line' id='LC565'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#for a in pattern.flat(Argument):</span></div><div class='line' id='LC566'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    same_name = [d for d in arguments if d.name == a.name]</span></div><div class='line' id='LC567'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    if same_name:</span></div><div class='line' id='LC568'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#        a.value = same_name[0].value</span></div><div class='line' id='LC569'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">argv</span> <span class="o">=</span> <span class="n">parse_argv</span><span class="p">(</span><span class="n">Tokens</span><span class="p">(</span><span class="n">argv</span><span class="p">),</span> <span class="nb">list</span><span class="p">(</span><span class="n">options</span><span class="p">),</span> <span class="n">options_first</span><span class="p">)</span></div><div class='line' id='LC570'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pattern_options</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">pattern</span><span class="o">.</span><span class="n">flat</span><span class="p">(</span><span class="n">Option</span><span class="p">))</span></div><div class='line' id='LC571'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">options_shortcut</span> <span class="ow">in</span> <span class="n">pattern</span><span class="o">.</span><span class="n">flat</span><span class="p">(</span><span class="n">OptionsShortcut</span><span class="p">):</span></div><div class='line' id='LC572'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">doc_options</span> <span class="o">=</span> <span class="n">parse_defaults</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span></div><div class='line' id='LC573'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">options_shortcut</span><span class="o">.</span><span class="n">children</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">doc_options</span><span class="p">)</span> <span class="o">-</span> <span class="n">pattern_options</span><span class="p">)</span></div><div class='line' id='LC574'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#if any_options:</span></div><div class='line' id='LC575'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    options_shortcut.children += [Option(o.short, o.long, o.argcount)</span></div><div class='line' id='LC576'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#                    for o in argv if type(o) is Option]</span></div><div class='line' id='LC577'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">extras</span><span class="p">(</span><span class="n">help</span><span class="p">,</span> <span class="n">version</span><span class="p">,</span> <span class="n">argv</span><span class="p">,</span> <span class="n">doc</span><span class="p">)</span></div><div class='line' id='LC578'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">matched</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">collected</span> <span class="o">=</span> <span class="n">pattern</span><span class="o">.</span><span class="n">fix</span><span class="p">()</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">argv</span><span class="p">)</span></div><div class='line' id='LC579'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">matched</span> <span class="ow">and</span> <span class="n">left</span> <span class="o">==</span> <span class="p">[]:</span>  <span class="c"># better error message if left?</span></div><div class='line' id='LC580'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Dict</span><span class="p">((</span><span class="n">a</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">a</span><span class="o">.</span><span class="n">value</span><span class="p">)</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="p">(</span><span class="n">pattern</span><span class="o">.</span><span class="n">flat</span><span class="p">()</span> <span class="o">+</span> <span class="n">collected</span><span class="p">))</span></div><div class='line' id='LC581'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">DocoptExit</span><span class="p">()</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <h2>Jump to Line</h2>
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="textfield js-jump-to-line-field" type="text">
            <div class="full-button">
              <button type="submit" class="button">Go</button>
            </div>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1360648843" height="64" width="64">
</div>


        </div>
      </div>
      <div class="modal-backdrop"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.08279s from fe3.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-icon mega-icon-invertocat"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/docopt/docopt/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-icon mega-icon-normalscreen"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="mini-icon mini-icon-brightness"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="mini-icon mini-icon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.08339' data-host='fe3'></span>
    
  </body>
</html>
