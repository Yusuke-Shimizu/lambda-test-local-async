.DEFAULT_GOAL := help

help: ## Show help
	@echo "Commands:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

.PHONY: setup
setup: ## setup
	pip3 install -r requirements.txt

.PHONY: diff
diff: ## diff
	cdk diff LambdaTestLocalAsyncStack-$(ENV) -c env=$(ENV)

.PHONY: deploy
deploy: ## deploy
	cdk deploy LambdaTestLocalAsyncStack-$(ENV) -c env=$(ENV)

.PHONY: test
test: ## test
	curl -X POST https://drq0zz4nol.execute-api.ap-northeast-1.amazonaws.com/prod/
	curl -X POST https://q5vnugq28d.execute-api.ap-northeast-1.amazonaws.com/prod/
