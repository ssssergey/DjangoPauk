'use strict';

angular.module('startPage')
    .constant("baseURL", "/")
    .service('itemsFactory', ['$resource', 'baseURL', function ($resource, baseURL) {
        this.getItems = function () {
            return $resource(baseURL + "api/:id?format=json", null, {'update': {method: 'PUT'}});
        };
        this.getCountries = function () {
            return $resource(baseURL + "api/countries?format=json", null, {'update': {method: 'PUT'}});
        };
        this.getCountryList = function () {
            return $resource(baseURL + "api/countries/:slug?format=json", null, {'update': {method: 'PUT'}});
        };
        this.download = function () {
            return $resource(baseURL + "api/generate_docx/?name=:country_name&slug=:country_slug", null, {
                getFile: {
                    method: 'GET',
                    url: baseURL + "api/generate_docx/?name=:country_name&slug=:country_slug",
                    cache: false
                }
            });
        };
    }]);
