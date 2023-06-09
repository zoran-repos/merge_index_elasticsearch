# Demo how to force merge indexes in Elasticsearch

For testing purpose those setup will spinup Elasticsearch and Kibana in Docker environment

## Technologies Used
-Python\
-Docker

## Getting Started

### Prerequisites
- Python (version X.X.X)
- Docker (version X.X.X)

## Installation
- clone the repository

```bash
git clone https://github.com/zoran-repos/recipes.git](https://github.com/zoran-repos/merge_index_elasticsearch.git
```
```bash
docker-compose up -d
```
- Create random index-es for current year

```bash
python3 random_indexes.py
```
- Start force merge indexes for all indexes from 2000y. till now. Non existing indexes will be skiped

```bash
python3 merge_index_final.py
```


## License

[MIT](https://choosealicense.com/licenses/mit/)
 
