var formApp = angular.module('formApp',['commons']);

    // create angular controller and pass in $scope and $http
formApp.controller("formController",['$scope','$http','AjaxCall',function($scope,$http, AjaxCall) {

    $scope.formData = {};
         $scope.newprocessForm = function() {
            var data_val;
            data_val = $.param($scope.formData);
            console.log('Value before is')
             console.log(data_val)
             AjaxCall.val(data_val).success(function(data) {
                 console.log("Values are");
                 console.log(data);
             })
            console.log('Ending')
        };

}]);



