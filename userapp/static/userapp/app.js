
var myApp = angular.module('myApp', ['ngRoute']).config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

myApp.config(['$routeProvider','$locationProvider',
    function($routeProvider,$locationProvider) {
        $routeProvider.
            when('/display', {
                templateUrl: 'static/userapp/newPage.html',
                controller: 'displayController'

            }).when('/insert', {
                templateUrl : 'static/userapp/new_user_ang.html',
                controller  : 'mainController'
            }).otherwise({
                redirectTo: '/'
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


myApp.controller("mainController", function ($scope, $http) {
    $scope.user = {};

    $scope.submitForm = function (isValid) {

        if (isValid) {



            //Code For ajax call for sending function

            $http({
                method: 'POST',
                url: '/userapp/post/new/',
                data: $.param($scope.user),  // pass in data as strings
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)
            })
                .success(function (data) {
                    console.log("Form submitted")
                    console.log(data)
                })
        }
    }
}).directive('equal', function () {

    return {
        require: 'ngModel',
        scope: {
            equal: '='
        },
        link: function (scope, elem, attrs, ctrl) {

            ctrl.$validators.equal = function (modelValue, viewValue) {
                return modelValue === scope.equal;
            };

            scope.$watch('equal', function (newVal, oldVal) {
                ctrl.$validate();
            });
        }
    };
});
;
