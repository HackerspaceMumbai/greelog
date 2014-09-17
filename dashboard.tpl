<!DOCTYPE html>
<html ng-app="appUser">

<head>
<title>Greelog: Dashboard</title>

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


<body style="background-image : url('~/../img/GreeLog_Cover_Photo.jpg'); background-size: cover">

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
              <h5><span id= "username" style="color : #FFFFFF; margin-right:10px;">Welcome</span>
                 <button type="button" class="btn btn-success">
                      Karma <span class="badge">325</span>
                 </button>
              </h5>
            </div>
            <button type="submit"  style= "background: #B8B8B8;margin-left:20px;"class="btn">Logout</button>
          </form>
        </div><!--/.navbar-collapse -->
      </div>
 </div>
</div>




 <!-- MAIN CONTENT -->
 <div class="container" style="display:block;margin-top:65px">

 	<h5> Recommended task </h5>


 	<div class="row">
        <div class="col-md-4">
          <div class="tasks">
	          <h4 style="display:inline;margin-right:10px">Rain-Water Harvesting</h4> <span style="display:inline;"class="badge">250</span>
	          <p>Conserve the rain water by implementing rain water harvesting system at your society.</p>
	          <p><a class="btn btn-default"  data-toggle="modal" data-target="#submitTaskModal" role="button">Submit details &raquo;</a></p>
	        </div>
        </div>
        <div class="col-md-4">
          <div class="tasks">
	          <h4 style="display:inline;margin-right:10px">Adopt-a-tree</h4> <span style="display:inline;"class="badge">50</span>

	          <p>By helping to water and care for a young street tree, you can help build a healthy tree canopy on your street.</p>
	          <p><a class="btn btn-default"  data-toggle="modal" data-target="#submitTaskModal" role="button">Submit details &raquo;</a></p>
	       </div>
       </div>
        <div class="col-md-4">
        	<div class="tasks">
	          <h4 style="display:inline;margin-right:10px">Replace standard bulbs with CFLs</h4> <span style="display:inline;"class="badge">30</span>
	          <p>Compact fluorescent light bulbs are more energy-efficient than regular bulbs, while giving off the same amount of light.</p>
	          <p><a class="btn btn-default"  data-toggle="modal" data-target="#submitTaskModal" role="button">Submit details &raquo;</a></p>
	        </div>
        </div>

      </div>



 </div> <!-- Main container end -->



 <div class="modal fade" id="submitTaskModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h4 class="modal-title">Submit task</h4>
            </div>

            <div class="modal-body">
                <!-- The form is placed inside the body of modal -->
                <form id="submitTaskForm"  class="form-horizontal">
                    <div class="form-group">
                        <label class="col-md-3 control-label">Link</label>
                        <input type="text" style="display:none" class="form-control" name="tid" />
                        <div class="col-md-5">
                            <input type="text" class="form-control" name="link" />
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-md-3 control-label">Description</label>
                        <div class="col-md-5">
                            <textarea type="text" rows="3" class="form-control" name="description" ></textarea>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="col-md-5 col-md-offset-3">
                            <button type="submit" onclick="location.href='http://greelog.pythonanywhere.com/_dashboard'" class="btn btn-success">Done</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>


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
				  <li class="active menu-list">Tasks</li>
            	  <li class="menu-list" onclick="location.href='http://greelog.pythonanywhere.com/_insert_post'">New Post</li>
            	  <li class="menu-list" onclick="location.href='http://greelog.pythonanywhere.com/_events'">Events</li>
            	  <li class="menu-list" onclick="location.href='http://greelog.pythonanywhere.com/_explore'">Explore</li>
			</ul>

        </div><!--/.navbar-collapse -->
      </div>
 </div>
</div>





</div>
</body>


<script type="text/javascript">




</script>