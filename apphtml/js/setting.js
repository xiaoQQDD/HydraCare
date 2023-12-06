
function loadData() {
    $.get("/getsetting", function(res){
        console.log(res);
        $('#goal').val(res.goal);
        $('#start').val(res.start);
        $('#end').val(res.end);
        $('#gap').val(res.gap);
    })
}

loadData();