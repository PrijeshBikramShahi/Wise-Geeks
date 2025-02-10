document.getElementById("startupButton").addEventListener("click", function () {
  document.getElementById("startupForm").style.display = "block";
  document.getElementById("investorForm").style.display = "none";
});

document
  .getElementById("investorButton")
  .addEventListener("click", function () {
    document.getElementById("investorForm").style.display = "block";
    document.getElementById("startupForm").style.display = "none";
  });

// Handle form submissions for both
document
  .getElementById("startupDetailsForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    alert("Startup details submitted for review!");
  });

document
  .getElementById("investorDetailsForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    alert("Investor details submitted for review!");
  });
