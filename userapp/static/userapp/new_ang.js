var formApp = angular.module('formApp', ['commons']);

// create angular controller and pass in $scope and $http
formApp.controller("formController", ['$scope', '$http', 'AjaxCall', function ($scope, $http, AjaxCall) {

    $scope.formData = {};
    $scope.newprocessForm = function () {
        var data_val, email_val, method, url,new_email,email_s;
        email_s = {'email':$scope.formData.email}

        data_val = $.param($scope.formData);
        email_val = $scope.formData.email;
        email_val = $.param(email_s)
        new_email = $.param($scope.formData.email)
        console.log('New email');
        console.log(email_s)
        console.log('Value of email is');
        console.log(email_val);
        console.log('Value before is');
        console.log(data_val);
        method = 'POST';
        url = '/userapp/latestlogin/';
        AjaxCall.val(method, url, data_val).success(function (data) {
            console.log("Values are");
            console.log(data);
            if (data.success == 'true') {
                method = 'POST';
                url = '/userapp/index/';
                console.log("Redirection possible");
              //window.location ="/userapp/index";
                AjaxCall.val(method,url,email_val).success(function(data){
                    console.log('Call Successful')
                });
            }
            else {
                console.log('Please enter the correct credentials');
            }
        }).error(function (data) {
            console.log('Ajax Call not completed');
            console.log(data)
        })
        ;
        console.log('Ending')
    };

}]);



