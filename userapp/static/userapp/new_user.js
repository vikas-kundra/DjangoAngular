var validApp = angular.module('validApp', []).config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

// create angular controller and pass in $scope and $http
validApp.controller("mainController", function ($scope, $http) {
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

