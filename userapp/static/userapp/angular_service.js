/**
 * Created by ubuntu on 28/12/15.
 */

var commons = angular.module('commons', []).config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});


commons.service('AjaxCall', function ($http) {
    this.val = function (method,url,dataval) {
        console.log('Inside ajaxCall');
        console.log(dataval)
    return     $http({
            method: method,
            url: url,
            data: dataval,  // pass in data as strings
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)

        });


    };

});

