
var myApp = angular.module('myApp', []);

myApp.controller('SpicyController', ['$scope', function($scope) {
    $scope.customSpice = "default";
    $scope.spice = 'very';
    $scope.selected_val = 'None'

    $scope.names=[{name:'India',currency:'Rupee'},
                  {name:'Japan',currency:'Yen'},
                  {name:'US',currency:'Dollar'}]
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

