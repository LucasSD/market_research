import json

from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
from market_research.graphqlapigraphene.schema import schema
from market_research.taskapi.models import Tile, Task

class GetTilesTest(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    @classmethod
    def setUpTestData(cls):
        cls.tile1 = mixer.blend(Tile)
        cls.tile2 = mixer.blend(Tile, title="random_title")

    def test_get_all_tiles(self):
        response = self.query(
        '''
        query {
            tiles {
                title
                status
                launchDate
            }
        }
        ''',
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert len(content['data']['tiles']) == 2

    def test_get_one_tile(self):
        response = self.query(
            '''
                query($title: String!){
                    tile(title: $title) {
                        title
                        status
                        launchDate
                    }
            }
            ''',
            variables={'title': "random_title"},
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert content['data']['tile']["title"] == "random_title"
        assert content['data']['tile']["status"]
        assert content['data']['tile']["launchDate"]


class GetAllTasksTest(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    @classmethod
    def setUpTestData(cls):
        cls.task1 = mixer.blend(Task)
        cls.task2 = mixer.blend(Task)

    def test_get_all_tasks(self):
        response = self.query(
        '''
        query {
            tasks {
                title
                description
                order
                tile {
                    title
                    status
                    launchDate
                    }
            }
        }
        ''',
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert len(content['data']['tasks']) == 2



