.PHONY: verify profile fixture
verify:
	python scripts/verify_participant_pack.py
profile:
	python scripts/profile_baseline.py
fixture:
	python scripts/build_app_fixture.py
