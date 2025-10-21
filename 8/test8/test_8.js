import http from "k6/http";
import { check} from "k6";

export default function () {
  const res = http.get(`https://quickpizza.grafana.com/`, { timeout: "10s" });

  check(res, {
    "status is 200": (r) => r.status === 200,
  });
}