var BASE_URL = "http://localhost/Greelog/"
var request_config = {"Content-Type" : 'multipart/form-data'};



    appUser = angular.module("appUser",[]);


    appUser.controller('home_controller', function($scope){
	 
	    $scope.user_credentials={};
		$scope.user={};
		$scope.login_validation = '';
		$scope.validation = '';	

    });


// Dashboard controller 



    appUser.controller('dashboard_controller', function($scope){
	 
	    $scope.pages={
	    	
	    }



	    
		$scope.user={};
		$scope.login_validation = '';
		$scope.validation = '';   

	

    });