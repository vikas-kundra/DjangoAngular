/**
 * Created by ubuntu on 28/12/15.
 */

var commons = angular.module('commons', []).config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});


commons.service('AjaxCall', function ($http) {
    this.val = function (dataval) {
        console.log(dataval)
    return     $http({
            method: 'POST',
            url: '/userapp/latestlogin/',
            data: dataval,  // pass in data as strings
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)

        });


    };

});

