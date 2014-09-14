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


<body style="background-image : url('~/../img/GreeLog_Cover_Photo.jpg'); ">

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
</div>




 <!-- MAIN CONTENT -->
 <div class="container" style="display:block;margin-top:65px;">

 	<h5> Upcoming events </h5>


 	<div class="row">
        <div class="col-md-4">
          <div class="tasks">
	          <h4 style="display:inline;margin-right:10px">Heading</h4>
	          <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
	          <p><a class="btn btn-default"  data-toggle="modal" data-target="#submitTaskModal" role="button">View &raquo;</a></p>
	        </div>
        </div>
        <div class="col-md-4">
          <div class="tasks">
	          <h4 style="display:inline;margin-right:10px">Heading</h4>

	          <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
	          <p><a class="btn btn-default"  data-toggle="modal" data-target="#submitTaskModal" role="button">View &raquo;</a></p>
	       </div>
       </div>
        <div class="col-md-4">
        	<div class="tasks">
	          <h4 style="display:inline;margin-right:10px">Heading</h4>
	          <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
	          <p><a class="btn btn-default"  data-toggle="modal" data-target="#submitTaskModal" role="button">View &raquo;</a></p>
	        </div>
        </div>
      </div>



 </div> <!-- Main container end -->



 <div class="modal fade" id="submitTaskModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h4 class="modal-title">Event Name</h4>
            </div>

            <div class="modal-body">
                <!-- The form is placed inside the body of modal -->
                <form id="submitEventForm" method="post" class="form-horizontal">
                    <div class="form-group">
                        <label class="col-md-3 control-label">Link</label>
                        <input type="text" style="display:none" class="form-control" name="eid" />
                        <div class="col-md-9">
                           <label id="eLink" class="control-label">Link</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-md-3 control-label">Description</label>
                        <div class="col-md-9">
                            <label id="eDescription" class="control-label">Hackathon</label>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="col-md-3 control-label">Venue</label>
                        <div class="col-md-9">
                            <label id="eDescription" class="control-label">VJTI College asdfasdf asd asdfasdf asdf asdfasdfasdfasdfasd fas dfasd fasdf asdf asdfasdfads fasdfsadfasdf fa fasdf asdf asdf asdfasdf</label>
                        </div>
                    </div>

                    </br>
                    <div class="form-group">

                        <label class="col-md-3 control-label">Going</label>
                        <div class="col-md-5">
                          <div class="btn-group">
                            <button type="submit" class="btn btn-success">Yes</button>
                            <button type="submit" class="btn btn-warning">May be</button>
                            <button type="submit" class="btn btn-danger">No</button>
                          </div>

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
                <li class="menu-list" onclick="location.href='~/../_dashboard'">Task</li>
                <li class="menu-list" onclick="location.href='~/../_insert_post'">New Post</li>
                <li class="active menu-list" onclick="location.href='~/../events.tpl'">Events</li>
                <li class="menu-list" onclick="location.href='~/../events.tpl'">Explore</li>
			</ul>

        </div><!--/.navbar-collapse -->
      </div>
 </div>
</div>





</div>
</body>


<script type="text/javascript">




</script>

