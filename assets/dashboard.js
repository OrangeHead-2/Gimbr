document.addEventListener("DOMContentLoaded", function() {
  const sidebarToggle = document.getElementById("sidebar-toggle");
  if (sidebarToggle) {
    sidebarToggle.addEventListener("click", function() {
      document.body.classList.toggle("sidebar-collapsed");
    });
  }

  async function updateMetrics() {
    try {
      const resp = await fetch("/api/dashboard/metrics");
      const data = await resp.json();
      document.getElementById("metric-failure-rate").textContent = (data.failure_rate * 100).toFixed(2) + "%";
      document.getElementById("metric-total-structures").textContent = data.total_structures;
    } catch (e) {}
  }
  updateMetrics();

  if (window.Chart) {
    fetch("/api/dashboard/failure_probability_hist")
      .then(r => r.json())
      .then(data => {
        new Chart(document.getElementById("failureProbHist"), {
          type: "bar",
          data: {
            labels: data.bins,
            datasets: [{
              label: "Failure Probability",
              data: data.counts,
              backgroundColor: "#3867d6"
            }]
          }
        });
      });
  }
});