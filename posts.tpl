<!DOCTYPE html>
<html ng-app="appUser">

<head>
<title>Greelog</title>

<meta name="viewport" content="width=device-width, initial-scale=1">
<meta content="text/html;charset=utf-8" http-equiv="Content-Type">
<meta content="utf-8" http-equiv="encoding">

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="~/../css/greelog.css">


<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>

<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.23/angular.min.js"></script>

<script src="~/../js/greelog.js"></script>
<style>

.input_text{

	width: 80%;
}
</style>



</head>


<body style="background-image : url('~/../img/GreeLog_Cover_Photo.jpg');background-size: cover">

<div id='content' ng-controller="dashoboard_controller">

 <div class="navbar navbar-inverse navbar-fixed-top" role="navigation" style="display:block">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Greelog</a>
        </div>
        <div class="navbar-collapse collapse">

	  	<!--  <div style="float:left; margin: 15px 0px 0px 20px;color:#FFFFFF">My task </div> -->

          <form name="loginForm" methode="POST" action="/_logout" class="navbar-form navbar-right" role="form">

            <div class="form-group">
              <h5><span id= "username" style="color : #FFFFFF; margin-right:10px;">Welcome</span><span style="margin-right:25px;" class="badge">42</span> </h5>
            </div>
            <button type="submit"  style= "background: #B8B8B8"class="btn">Logout</button>
          </form>
        </div><!--/.navbar-collapse -->
      </div>
 </div>





 <!-- MAIN CONTENT -->
 <div class="container-fluid" style="display:block;margin-top:55px;">

 	  <form id="submitPostForm" method="post" class="form-horizontal"style="margin:0 100px 0 100px;background: rgba(255,255,255,0.2) !important;padding :10px 0px 10px 0px">
                    <div class="form-group">
                        <label style="text-align:right !important;color :#FFFFFF;font-size:120%" class="col-sm-3 control-label">Title</label>
                        <input type="text" style="display:none" class="form-control" name="tid" />
                        <div class="col-md-5">
                            <input type="text" class="form-control" style="background : #F5F5F5" name="title" />
                        </div>
                    </div>
                    <div class="form-group">
                        <label style="text-align:right !important;color :#FFFFFF;font-size:120%" class="col-sm-3 control-label">Body</label>
                        <div class="col-md-7">
                            <textarea type="text" rows="15" style="background : #F5F5F5" class="form-control input-lg" name="description" ></textarea>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="col-md-5 col-md-offset-3">
                            <button type="submit" class="btn btn-success" style= "padding: 0.5em 1em 0.5em 1em;font-size:120%">Draft</button>
                            <button type="submit" class="btn btn-success" style="padding:0.5em 1em 0.5em 1em;margin-left:3em;font-size:120%">Publish</button>
                        </div>

                    </div>
    </form>


 </div> <!-- Main container end -->






<!-- FOOTER -->
<div class="navbar navbar-inverse navbar-fixed-bottom" role="navigation" style="display:block;max-height:20px !important">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bottom-navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <div class="left" style="margin-left: 10px">
                        <span style="color:#FFFFFF" id="ccore"></span>
          </div>
        </div>
        <div class="navbar-collapse collapse" id= "bottom-navbar-collapse">

	  		<ul class="list-inline custom" style="float : right;color: #FFFFFF">
				        <li class="menu-list" onclick="location.href='~/../_dashboard'">Tasks</li>
                <li class="active menu-list" onclick="location.href='~/../_insert_post'">New Post</li>
                <li class="menu-list" onclick="location.href='http://greelog.pythonanywhere.com/_events'">Events</li>
                <li class="menu-list" onclick="location.href='http://greelog.pythonanywhere.com/_events'">Explore</li>
			 </ul>

        </div><!--/.navbar-collapse -->
      </div>
 </div>






</div>
</body>


