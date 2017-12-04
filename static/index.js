$(() => {
    let date = new Date();
    let d = date.getDate();
    
    let message_list = ['Not yet dummy 😝', 'Wait for it...👀', 'Take the hint! 🙃', 'I said NO!😶', 'This is random 😵', 'You will be put on the bad list! 🙄', 'Santa is not coming to town ... yet 😛', 'Try tommorrow... 😱', 'Enter password: 🔐', 'Few more days! 💩']
    for (let i = 1; i <= 25; i++) {
        $(`.day${i}`).click(function() {
            if (i <= parseInt(d)) {
                $("h1", this).addClass("hidden");
                $("img", this).removeClass("hidden");
            } else {
                var j = Math.floor(Math.random() * 10);
                $("h1", this).text(message_list[j]);
            }
        });
    }

    $("html").click(() => {
        let $santaDiv = $(".santa_div"),
            $santaClone = $santaDiv.clone(true);
        
        $santaDiv.before($santaClone);

        $(`.${$santaDiv.attr("class")}:last`).remove();
    });
});
