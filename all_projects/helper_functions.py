from typing import Union


def get_leetcode_data_from_response_object(response_object) -> dict[str, Union[str, float]]:
    response_object = response_object.json()
    if response_object["message"] == "retrieved":
        data = dict()
        data['error'] = None
        data['easy'] = f"{response_object['easySolved']} / {response_object['totalEasy']}"
        data['medium'] = f"{response_object['mediumSolved']} / {response_object['totalMedium']}"
        data['hard'] = f"{response_object['hardSolved']} / {response_object['totalHard']}"
        data['totalSolved'] = f"{response_object['totalSolved']} / {response_object['totalQuestions']}"
        data['rank'] = response_object['ranking']
        data['total_submissions_this_year'] = sum(
            response_object['submissionCalendar'].values())

        return data
    return {"error": "user data not availabe, please check leetcode handle"}
