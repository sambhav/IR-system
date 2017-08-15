//Calling search function on keyup for instant results
$('#search').keyup(function () {
    post();
});

//Search post Function
function post()
{
    var search = $('#search').val();
    $.ajax(
    {
        url: '/search',
        data: $('form').serialize(),
        type: 'POST',
        success: function (response)
        {
            // $('#search').html("");
            var resp = $.parseJSON(response);
            var tfidf = resp['tfidf'];
            var bm25 = resp['bm25'];
            console.log(tfidf);
            console.log(bm25);
            // for (var i = 0; i < arr.length - 1; i++)
            // {
            //     var result = "<div class='result'>"
            //     result += "<div class='resultTitle'>" + arr[i][0] + "</div>";
            //     result += "<div class='resultLink'>" + "<a href='" + arr[i][1] + "'>" + arr[i][1] + "</a></div>";
            //     result += "<div class='resultContent'>" + arr[i][2] + "</div>";
            //     result += "</div>"
            //     $('#Search').append("<div>" + result + "</div>");
            // }
            // if (arr[i][0] == 1) $('#Suggestions').html("No results for this. Did You Mean: <b>" + arr[i][1] + "</b>");
            // else $('#Suggestions').html("");
        },
        error: function (error)
        {
            console.log(error);
        }
    });
}
