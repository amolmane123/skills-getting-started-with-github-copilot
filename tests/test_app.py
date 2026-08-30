from fastapi.testclient import TestClient

from src import app as app_module

client = TestClient(app_module.app)


def test_unregister_participant_removes_email_from_activity():
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    original_participants = app_module.activities[activity_name]["participants"][:]
    app_module.activities[activity_name]["participants"] = []

    try:
        # Act
        signup_response = client.post(
            f"/activities/{activity_name}/signup?email={email}"
        )
        unregister_response = client.delete(
            f"/activities/{activity_name}/unregister?email={email}"
        )

        # Assert
        assert signup_response.status_code == 200
        assert unregister_response.status_code == 200
        assert email not in app_module.activities[activity_name]["participants"]
    finally:
        app_module.activities[activity_name]["participants"] = original_participants
