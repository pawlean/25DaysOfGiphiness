$(() => {
    const date = new Date();
    const d = date.getDate();   
    const message_list = ['Not yet dummy 😝', 'Wait for it...👀', 'Take the hint! 🙃',
                          'I said NO!😶', 'This is random 😵', 'You will be put on the bad list! 🙄',
                          'Santa is not coming to town ... yet 😛', 'Try tommorrow... 😱',
                          'Enter password: 🔐', 'Few more days! 💩'];

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
        const MAX_SANTAS = 5;
        let $santaDiv = $(".santa_div").first(),
            numOfSantas = $(".santa_div").length,
            $santaClone = $santaDiv.clone(true);
        
        if (numOfSantas < MAX_SANTAS) {
            // Make more santas only if we're currently under the limit
            $santaDiv.before($santaClone);
            // Clean up the santa once they've finished animating
            $santaClone.on("animationend", function() {
                $(this).remove();
            });
        }
    });
});
