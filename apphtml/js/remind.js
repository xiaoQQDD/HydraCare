
function startRemind() {
    $.get("/getsetting", function(res){
        console.log(res);
        startTimer(res.start, res.end, res.gap);
    })
}

function startTimer(start, end, gap) {
    let now = new Date();
    let now_str = now.getHours() + ":" + now.getMinutes();
    let start_time = new Date();
    start_time.setHours(start);
    start_time.setMinutes(0);
    start_time.setSeconds(0);
    let start_str = start_time.getHours() + ":" + start_time.getMinutes();
    let end_time = new Date();
    end_time.setHours(end);
    end_time.setMinutes(59);
    end_time.setSeconds(59);

    console.log(start_time, end_time );

    while(start_time < end_time){
        start_str = start_time.getHours() + ":" + start_time.getMinutes();
        // console.log(start_str);
        if(now_str == start_str){
            sendNotification();
            setTimeout(() => {
                startTimer(start, end, gap);
            }, 60 * 1000);
            break;
        }
        start_time.setMinutes(start_time.getMinutes() + gap);
    }
    
}

function sendNotification(){
    let notify = $(`
    <div class="drink-notify" style="position: fixed; top: 10px; left: 0; width: 100%; 
    height: 100px; background-color: #00000055; 
    color: #ffffff; text-align: center; 
    border:5px solid #55ff22;
    border-radius: 10px;
    z-index:9999">
        <div style="float:right;margin:5px 5px 0 0">
            <button class="btn btn-danger" onclick="$('.drink-notify').remove()">
                X
            </button>
        </div>
        It's time to take a break! <br>
        Have some drinks...
    </div>`);
    $(".drink-notify").remove();
    $('body').append(notify);
}

startRemind();