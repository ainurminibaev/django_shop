/**
 * Created by ainurminibaev on 29.11.14.
 */
$(document).ready(function () {
    var page = 0;
    $(".js-catalog").click(function () {
        var $this = $(this);
        if (!$this.hasClass('active')) {
            $(".js-catalog").removeClass('active');
            $this.addClass("active");
            page = 0;
            catalogAjaxReloader();
        }
    });

    function catalogAjaxReloader() {
        var param_map = {};
        var catalog = $(".js-catalog.active");
        var id = null;
        if (catalog.length) {
            id = parseInt(catalog.data('id'));
            if (id < 0) {
                id = null;
            }
        }

        param_map.catalog = id;
        param_map.page = page
        param_map.csrfmiddlewaretoken = csrf_token;
        $.ajax({
            "method": "POST",
            "url": "/catalog/ajax",
            "data": param_map,
            "success": function (data) {
                var ddiv = $("<div></div>").append(data);
                if (ddiv.find(".js-good").length == 0) {
//TODO hide more btn
                }
                if (page == 0) {
                    $(".js-catalog-body").html(data);
                } else {
                    $(".js-catalog-body").append(data);
                }
                page++;
            },
            "error": function (data) {
                console.log("data loading error");
            }
        });

    }
});

