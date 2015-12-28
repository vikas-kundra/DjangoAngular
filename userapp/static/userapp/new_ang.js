

var formApp = angular.module('formApp', []).config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

    // create angular controller and pass in $scope and $http
    formApp.controller("formController",function($scope,$http) {
     $scope.formData = {};

  $scope.processForm = function() {
  $http({
  method  : 'POST',
  url     : '/userapp/latestlogin/',
  data    : $.param($scope.formData),  // pass in data as strings
  headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  // set the headers so angular passing info as form data (not request payload)
 })
  .success(function(data) {
    console.log("Values are");
    console.log(data);
    $scope.custom = data.success;
    if (data.success == 'true')
    {
    console.log("Redirection possible");
    window.location ="/userapp/index";
    }
    else
    {
    $scope.custom = 'Please enter the correct credentials';
    }

    })
    }});
