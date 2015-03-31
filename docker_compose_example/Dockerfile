FROM python:2.7.9-onbuild
MAINTAINER Alberto Perez <info@apa42.com>

# Install simpledatamigrate
RUN pip install git+https://github.com/aleasoluciones/simpledatamigrate.git

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["apa_run_main"]

