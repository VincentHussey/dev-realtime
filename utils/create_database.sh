echo "Enter a database username to create:"
read USER
createuser -U postgres -d -l -R -S -P $USER
echo "Enter a database name to create:"
read DB_NAME
createdb -U postgres -E UTF8 -O $USER $DB_NAME
createlang -U postgres plpgsql $DB_NAME
psql -U postgres -d $DB_NAME -f /usr/share/pgsql/contrib/postgis.sql
psql -U postgres -d $DB_NAME -f /usr/share/pgsql/contrib/spatial_ref_sys.sql
psql -U postgres -d $DB_NAME -c "alter table spatial_ref_sys owner to flood"
psql -U postgres -d $DB_NAME -c "alter table geometry_columns owner to flood"
psql -U postgres -d $DB_NAME -c "alter table geography_columns owner to flood"
