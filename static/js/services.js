'use strict';

angular.module('startPage')
    .constant("baseURL", "/")
    .service('itemsFactory', ['$resource', 'baseURL', function ($resource, baseURL) {
        this.getItems = function () {
            return $resource(baseURL + "api-app/:id?format=json", null, {'update': {method: 'PUT'}});
        };
        this.getCountryList = function () {
            return $resource(baseURL + "api-app/countries/:slug?format=json", null, {'update': {method: 'PUT'}});
        };
        this.getCountryNames = function () {
            return $resource(baseURL + "api-app/countrynames?format=json", null, {'update': {method: 'PUT'}});
        };
        this.atlantCountries = function () {
            return $resource(baseURL + "api-atlant/countries?format=json", null, {'update': {method: 'PUT'}});
        };
        //this.download = function () {
        //    return $resource(baseURL + "api-atlant/generate_docx/?name=:country_name&slug=:country_slug", null, {
        //        getFile: {
        //            method: 'GET',
        //            url: baseURL + "api-atlant/generate_docx/?name=:country_name&slug=:country_slug",
        //            cache: false
        //        }
        //    });
        //};
    }]);
