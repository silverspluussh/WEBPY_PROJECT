//wait for page to load first before applying script
$(document).ready(function() {
    console.log("loaded");
    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();

        var form = $("#register-form").serialize();
        $.ajax({
            url: "/postregistration",
            type: "POST" ,
            data: form,
            success: function(res) {
                console.log("Form Submitted")
                console.log(res);
            }
        });
    });
    $(document).on("submit", "#login-form", function(e){
        e.preventDefault();

        var logs=$(this).serialize();
        $.ajax({
              url: "/login_checker",
              type: "POST",
              data: logs,
              success: function(response){
                             if (response == "error"){
                                      alert("could not login")
                                }else{
                                      console.log("you are logged in as :", response);
                                      window.location.href = "/";
                                }
              }
         });
    });
    $(document).on("click", "#logout-link", function(e){
        e.preventDefault();

        $.ajax({
               url: "/logout",
               type: "GET",
               success: function(res){
                             if(res == "success"){
                                    window.location.href = "/login";
                             }else{
                                    alert("An error occurred");
                             }
               }

         });

     });
});