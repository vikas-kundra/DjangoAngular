var validApp = angular.module('myApp', []).config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

// create angular controller and pass in $scope and $http
validApp.controller("displayController",['$scope','$http', 'AjaxCall', function ($scope,$http,AjaxCall){
    $scope.user = {};
    $scope.table_data = '';
    console.log('Inside function');
    method = 'GET';
    url = '/userapp/display/';
    data_val = '';
    AjaxCall.val(method, url, data_val).success(function (data) {
        console.log('Call for button click successful');
        console.log(data);
        $scope.table_data = JSON.parse(data);
        console.log('Value in angularjs');
        console.log($scope.table_data);
        console.log('Type is!!1');
        console.log(typeof $scope.table_data)
    });

}
]);
