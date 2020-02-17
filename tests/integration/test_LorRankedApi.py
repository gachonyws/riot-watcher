import pytest


@pytest.mark.integration
@pytest.mark.parametrize(
    "region", ["EUROPE", "ASIA", "AMERICAS",],
)
class TestLorRankedApi:
    def test_leaderboards(self, lor_context, region):
        actual_response = lor_context.watcher.ranked.leaderboards(region)

        lor_context.verify_api_call(
            region, "/lor/ranked/v1/leaderboards", {}, actual_response,
        )

