$("document").ready(function () {
  $("#owner").click(function () {
    $("#petownerform").css("visibility", "visible");
    $("#petform").css("visibility", "hidden");

    console.log("owner!!");
  });

  $("#pet").click(function () {
    $("#petform").css("visibility", "visible");
    $("#petownerform").css("visibility", "hidden");
    console.log("pet!!");
  });
});
