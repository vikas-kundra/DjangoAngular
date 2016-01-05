
var myApp = angular.module('myApp', ['ngRoute']);

myApp.config(['$routeProvider','$locationProvider',
    function($routeProvider,$locationProvider) {
        $routeProvider.
            when('/display', {
                templateUrl: 'static/userapp/newPage.html',
                controller: 'displayController'

            }).when('/insert', {
                template : '<h2>Welcome to insert page</h2>',
                controller  : 'insertController'
            }).when('/index', {
                templateUrl : '../templates/userapp/pages/index.html',
                controller  : 'SpicyController'
            }).otherwise({
                redirectTo: '/index'
            });

    }]);


myApp.controller('SpicyController', ['$scope', function($scope) {
    $scope.customSpice = "default";
    $scope.spice = 'very';
    $scope.selected_val = 'None';
    $scope.names=[{name:'India',currency:'Rupee'},
                  {name:'Japan',currency:'Yen'},
                  {name:'US',currency:'Dollar'}];
    $scope.selected = $scope.names[0];
    $scope.spicy = function() {
        $scope.spice = $scope.customSpice;
    };

    $scope.static = function() {
        $scope.spice = 'Custom message will be displayed on this click';
    };

//    $scope.change = function() {
//        $scope.selected_val = $scope.selected.currency;
//    };
}]);


myApp.controller('displayController', function($scope) {
    $scope.message = 'Look! I am an about display.';
});

myApp.controller('insertController', function($scope) {
    $scope.message = 'This is insert page.';
});