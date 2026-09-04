def test_response_includes_request_id_header(client):
    response = client.get("/health")

    assert "X-Request-ID" in response.headers
    assert len(response.headers["X-Request-ID"]) > 0


def test_incoming_request_id_is_echoed_back(client):
    response = client.get("/health", headers={"X-Request-ID": "test-req-123"})

    assert response.headers["X-Request-ID"] == "test-req-123"


def test_metrics_endpoint_exposes_prometheus_format(client):
    client.get("/health")
    response = client.get("/metrics")

    assert response.status_code == 200
    assert "http_requests_total" in response.text
