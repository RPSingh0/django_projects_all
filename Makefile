help:
	@python help_make.py
update_my_code_rupinder:
	git checkout main
	git pull origin main
	git checkout rupinder
	git pull origin main

update_my_code_rishabh:
	git checkout main
	git pull origin main
	git checkout rishabh
	git pull origin main

push_changes_rupinder:
	git checkout rupinder
	git add .
	git commit -m"$(message)"
	git push origin rupinder

push_changes_rishabh:
	git checkout rishabh
	git add .
	git commit -m"$(message)"
	git push origin rishabh

create_pull_request_rupinder:
	git checkout rupinder
	gh pr create -t "$(message)" -b ""

create_pull_request_rishabh:
	git checkout rishabh
	gh pr create -t "$(message)" -b ""