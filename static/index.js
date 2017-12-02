$(() => {
  for (let i = 1; i <= 25; i++) {
    $(`.day${i}`).click(function() {
      $("h1", this).addClass("hidden");
      $("img", this).removeClass("hidden");
    });
  }
});
