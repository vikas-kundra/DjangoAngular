/**
 * Created by ubuntu on 28/12/15.
 */

var service_ajax = angular.module('service_ajax', []);

service_ajax.service('AjaxCall', function($http, $dataval){

    this.val = $http({
        method  : 'POST',
        url     : '/userapp/latestlogin/',
        data    : $dataval,  // pass in data as strings
        headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  // set the headers so angular passing info as form data (not request payload)
    })
    return val;
});

