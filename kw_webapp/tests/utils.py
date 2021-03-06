from datetime import timedelta

import responses
from django.contrib.auth.models import User

from kw_webapp.constants import API_KEY
from kw_webapp.models import Vocabulary, Reading, UserSpecific, Profile
from kw_webapp.tasks import build_user_information_api_string, build_API_sync_string_for_user_for_levels
from kw_webapp.tests import sample_api_responses


def create_user(username):
    u = User.objects.create(username=username)
    u.set_password(username)
    u.save()
    return u


def create_review(vocabulary, user):
    u = UserSpecific.objects.create(vocabulary=vocabulary, user=user)
    u.streak = 1
    u.save()
    return u


def create_lesson(vocabulary, user):
    u = UserSpecific.objects.create(vocabulary=vocabulary, user=user)
    u.streak = 0
    u.save()
    return u


def create_profile(user, api_key, level):
    p = Profile.objects.create(user=user, api_key=api_key, level=level)
    p.unlocked_levels.create(level=level)
    return p


def create_vocab(meaning):
    v = Vocabulary.objects.create(meaning=meaning)
    return v


def create_reading(vocab, reading, character, level):
    r = Reading.objects.create(vocabulary=vocab,
                               kana=reading, level=level, character=character)
    return r


def create_review_for_specific_time(user, meaning, time_to_review):
    timed_review = create_review(create_vocab(meaning), user)
    timed_review.needs_review = False
    timed_review.streak = 1
    timed_review.last_studied = time_to_review + timedelta(hours=-6)
    timed_review.next_review_date = time_to_review
    timed_review.save()
    return timed_review


def build_test_api_string_for_merging():
    api_call = "https://www.wanikani.com/api/user/{}/vocabulary/TEST".format(API_KEY)
    return api_call


def mock_vocab_list_response_with_single_vocabulary(user):
    responses.add(responses.GET, build_API_sync_string_for_user_for_levels(user, user.profile.level),
                  json=sample_api_responses.single_vocab_response,
                  status=200,
                  content_type='application/json')


def mock_user_info_response_with_higher_level(api_key):
    responses.add(responses.GET, build_user_information_api_string(api_key),
                  json=sample_api_responses.user_information_response_with_higher_level,
                  status=200,
                  content_type='application/json')


def mock_user_info_response(api_key):
    responses.add(responses.GET, build_user_information_api_string(api_key),
                  json=sample_api_responses.user_information_response,
                  status=200,
                  content_type='application/json')


def mock_invalid_api_user_info_response(api_key):
    responses.add(responses.GET, build_user_information_api_string(api_key),
                  json={"Nothing":"Nothing"},
                  status=200,
                  content_type='application/json')


def mock_vocab_list_response_with_single_vocabulary_with_four_synonyms(user):
    responses.add(responses.GET, build_API_sync_string_for_user_for_levels(user, [user.profile.level, ]),
                  json=sample_api_responses.single_vocab_response_with_4_meaning_synonyms,
                  status=200,
                  content_type='application/json')


def mock_vocab_list_response_with_single_vocabulary_with_changed_meaning(user):
    responses.add(responses.GET, build_API_sync_string_for_user_for_levels(user, [user.profile.level, ]),
                  json=sample_api_responses.single_vocab_response_with_changed_meaning,
                  status=200,
                  content_type='application/json')


def setupTestFixture(self):
    #Setup an admin user.
    self.admin = create_user("admin")
    create_profile(self.admin, "any_key", 5)
    self.admin.is_staff = True
    self.admin.save()

    # Setup a non-admin user.
    self.user = create_user("Tadgh")
    create_profile(self.user, "any_key", 5)

    # Setup some basic vocabulary / reading / review information.
    self.vocabulary = create_vocab("radioactive bat")
    self.reading = create_reading(self.vocabulary, "ねこ", "猫", 5)
    self.review = create_review(self.vocabulary, self.user)

