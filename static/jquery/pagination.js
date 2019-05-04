// 'use strict';
// var numberOfItems = $('.container .all').length;
// alert(numberOfItems);

$('#pagination-demo').twbsPagination({
        totalPages: 16,
        visiblePages: 6,
        next: 'Next',
        prev: 'Prev',
        onPageClick: function (event, page) {
            //fetch content and render here
            $('#page-content').text('Page ' + page) + ' content here';
        }
    });