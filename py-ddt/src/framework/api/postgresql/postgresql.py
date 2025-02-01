import datetime
import random as rnd
import string
import json
import os
from pathlib import Path
from datetime import datetime as stamp
from os import getenv
from uuid import uuid4 as hasher, UUID
from typing import List, Union

import psycopg2

from src.framework.infra.tools.definitions import Definitions as DF


class PostgreSqlApi(object):  # object inheritance support for py2 agnostic
    """
    PostgreSqlApi is an entity that handles interactions with a PostgreSQL database.
    TODO: documentation for PostgreSqlApi.py

    SPECIAL: be mindful of the numeric types from postgresql and python
     this references UUID in python as of os.time.now is a 128 bit | 16 byte entity
     which means that storing in postgresql will require a UUID type, default numeric types will not work
     this references TIMESTAMP in python as of os.time.now is a 64 bit | 8 byte entity
     which means that storing in postgresql will require a TIMESTAMP type, default numeric type will work
     reference : Definitions.POSTGRESQL_NUMERIC_TYPES
    """

    def __init__(self):
        """
        Initializes PostgreSqlApi with a default host set to None.
        Usages for a qualified session are,
            local/remote machine: 'localhost', 'ip', or 'nameserver'.
        """
        self._host = None
        print(r'DEBUG:postgresql.py,PostgreSqlApi __init__')

    @property
    def host(self):
        """Getter for the 'host' attribute."""
        return self._host

    @host.setter
    def host(self, value):
        """Setter for the 'host' attribute."""
        if isinstance(value, str) and value:
            self._host = value
        else:
            raise ValueError("Host must be a non-empty string.")

    modes = {
        0: 'connect(...)',  # @param host       , op connects db
        1: 'sql_create(...)',  # @param session    , op create δ
        2: 'sql_insert(...)',  # @param session    , op insert δ
        3: 'sql_select(...)',  # @param session    , op select δ
        4: 'sql_update(...)',  # @param session    , op update δ
        5: 'sql_delete(...)',  # @param session    , op delete δ
        6: 'sql_orderby(...)',  # @param session    , op orderby δ
        7: 'sql_groupby(...)',  # @param session    , op groupby δ
        8: 'sql_inner_join(...)',  # @param session    , op join δ
        9: 'sql_dump(...)',  # @param session    , op dump δ
        10: 'sql_experimental_cleanup(...)',  # @param session    , op clean db
        11: 'sql_experimental_json_mb_insert(...)',  # @param session    , op insert δ
        12: 'sql_experimental_json_mb_dump(...)',  # @param session    , op dump δ
        13: 'sql_experimental_json_mb_delete(...)',  # @param session    , op delete δ
        14: 'sql_experimental_audit_db_ops(...)',  # @param session    , op audit δ
        15: 'sql_experimental_audit_join_ops(...)',  # @param session    , op audit δ
        16: 'sql_experimental_delete_without_where(...)',  # @param session    , op delete δ
        17: 'sql_experimental_destroy(...)',  # @param session    , op destroy δ
        -1: 'EXIT'  # @param session    , op exit db
    }

    def fire_mode(self):
        """ Function provides the operations available to interface with the PostgresSQL database. """
        print(r'DEBUG:postgresql.py,PostgreSqlApi fire_mode(....)')
        db_cursor = None
        api_caller = self.ApiCall()
        for key, value in self.modes.items():
            print(f'{key}: {value}')
        while True:
            try:
                mode = int(input("Enter the mode: "))
                if mode in self.modes:
                    selected = self.modes[mode]
                    if mode == DF.PSQL_EXIT:
                        print("Exiting the program.")
                        break
                    elif mode == DF.PSQL_CONNECT:
                        print(f'Using "{selected}"')
                        self.host = 'localhost'
                        try:
                            api_caller.session = api_caller.connect(self.host)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                    elif mode == DF.PSQL_CREATE:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_create(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_INSERT:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_insert(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_SELECT:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_select(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_UPDATE:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_update(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_DELETE:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_delete_at_random(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_ORDERBY:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_orderby(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_GROUPBY:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_groupby(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_INNER_JOIN:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_inner_join(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_DUMP:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            db_cursor.execute(
                                f"""
                                SELECT *
                                FROM features
                                """
                            )
                            rows = db_cursor.fetchall()
                            api_caller.sql_dump(db_cursor, rows)
                            api_caller.session.commit()
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_EXPERIMENTAL_CLEANUP:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_experimental_cleanup(api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                    elif mode == DF.PSQL_EXPERIMENTAL_JSON_MB_INSERT:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_experimental_json_mb_insert(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_EXPERIMENTAL_JSON_MB_DUMP:
                        # TODO: audit using this method , watch memory for MB operation
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            db_cursor.execute(
                                f"""
                                SELECT *
                                FROM features
                                """
                            )
                            rows = db_cursor.fetchall()
                            api_caller.sql_experimental_json_mb_dump(db_cursor, rows)
                            api_caller.session.commit()
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_EXPERIMENTAL_JSON_MB_DELETE:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_experimental_json_mb_delete(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                    elif mode == DF.PSQL_EXPERIMENTAL_AUDIT_DBOPS:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_experimental_audit_db_ops(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_EXPERIMENTAL_AUDIT_JOINS:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_experimental_audit_join_ops(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_EXPERIMENTAL_DELETE_WITHOUT_WHERE:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_delete_without_where(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    elif mode == DF.PSQL_EXPERIMENTAL_DESTROY:
                        print(f'Using "{selected}"')
                        try:
                            db_cursor = api_caller.session.cursor()
                            api_caller.sql_experimental_destroy(db_cursor, api_caller.session)
                            print(f'{selected} is successful')
                        except Exception as e:
                            print(f'Error: {e}')
                        finally:
                            db_cursor.close()
                    else:
                        print(f'Unsupported: "{selected}"')
                else:
                    print(api_caller.session)
                    print("Invalid mode. Enter a valid mode.")
            except ValueError:
                print("Invalid input. Enter a valid input.")

    class ApiCall:
        """Handles SQL operations with the database."""

        """ tokens is a list that contains the unique sql table names for our database """
        table_tokens = [
            "features",
            "other"
        ]

        """ table_rider is a dictionary that contains a unique entry in the form of a sql table for our database """
        table_rider = {
            'rider_id': UUID,
            'rider_timestamp': datetime
        }

        """ feature_table is a variable that will facilitate accessing the table_tokens item for features"""
        T_feature = table_tokens[0]

        @property
        def session(self) -> psycopg2.extensions.connection:
            """Getter for the 'session' attribute."""
            return self._session

        @session.setter
        def session(self, value):
            """Setter for the 'session' attribute."""
            if isinstance(value, psycopg2.extensions.connection) and value:
                self._session = value
            else:
                raise ValueError("Session must be a non-empty string.")

        def __init__(self):
            self._session: psycopg2.extensions.connection = None
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall __init__')

        def __enter__(self):
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall __enter__')
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall __exit__')
            if self._session:
                self.sql_experimental_cleanup(self._session)
            return False

        def connect(self, ip: string) -> psycopg2.extensions.connection:
            """
            :functionality: Connect to the PostgreSQL database.
            :args: ip (string): the IP address or hostname of the PostgreSQL server.
            :return: connection (psycopg2.extensions.connection): a connection object.
            """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall connect(...)')
            return psycopg2.connect(database="feature_engineering_db",
                                    port=DF.POSTGRESQL_PORT,
                                    host=ip,
                                    user=getenv('CREDENTIAL_POSTGRESQL_SERVER_USERNAME'),
                                    password=getenv('CREDENTIAL_POSTGRESQL_SERVER_PASSWORD'))

        def sql_create(self, db_cursor, db_session):
            """ Function for create operation
            , to create a table with rider_id (UUID) and rider_timestamp (BIGINT). """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_create(...)')
            if db_cursor is None:
                print(f'DEBUG: sql_create . db_cursor : {db_cursor}')
            db_cursor.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {self.T_feature}
                (
                    rider_id UUID PRIMARY KEY, 
                    rider_timestamp TIMESTAMP NOT NULL
                )
                """
            )
            db_session.commit()

        def sql_insert(self, db_cursor, db_session):
            """ Function for insert operation
            , to insert into a table with rider_id (UUID) and rider_timestamp (BIGINT). """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_insert(...)')
            self.table_rider.update({'rider_id': hasher().hex})
            self.table_rider.update({'rider_timestamp': stamp.now().strftime('%Y-%m-%d %H:%M:%S')})
            p = list(self.table_rider.values())[0]
            temp = list(self.table_rider.values())[1]
            q = stamp.strptime(temp, "%Y-%m-%d %H:%M:%S")
            db_cursor.execute(
                f"""
                INSERT INTO {self.T_feature}
                (
                    rider_id,
                    rider_timestamp
                )
                VALUES
                (
                    '{p}',
                    '{q}'
                )
                """
            )
            db_session.commit()

        def sql_select(self, db_cursor, db_session):
            """ Function for select operation
            , to select from table with rider_id (UUID) and rider_timestamp (BIGINT). """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_select(...)')
            db_cursor.execute(
                f"""
                SELECT *
                FROM {self.T_feature}
                """
            )
            rows = db_cursor.fetchall()
            for i, row in enumerate(rows):  # rows is tuple. lacks index. enumerate to iterate
                print(f'row_id:{i},row_data:{row}')
            db_session.commit()

        def sql_update(self, db_cursor, db_session):
            # TODO: postgresql.py, sql_update
            """ Function for update operation
            , to update from table with rider_id (UUID) and rider_timestamp (TIMESTAMP). """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_update(...)')
            # a = self.T_feature
            # b = 'rider_timestamp,TODO:sql_update.py'
            # c = 'rider_id,TODO:sql_update.py'
            # db_cursor.execute(
            #     f"""
            #     UPDATE {a}
            #     SET rider_timestamp = {b}
            #     WHERE rider_id = {c}
            #     """
            # )
            # db_session.commit()

        def sql_delete_at_random(self, db_cursor, db_session):
            # TODO: postgresql.py, sql_delete_with_where
            """ Function for delete operation
            , to delete from table with rider_id (UUID) and rider_timestamp (TIMESTAMP).
            delete the row that satisfies the where clause from the specified table.
            this approach allows us to select an item in the table at random then delete it."""
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_delete_at_random(...)')
            # feature_table = {self.T_feature}
            # db_cursor.execute(
            #     f"""
            #     SELECT rider_id
            #     FROM {feature_table}
            #     ORDER BY RANDOM()
            #     LIMIT 1;
            #     DELETE FROM {feature_table}
            #     WHERE rider_id = (
            #         SELECT rider_id
            #         FROM {feature_table}
            #         ORDER BY RANDOM()
            #         LIMIT 1
            #     );
            #     """
            # )
            # db_session.commit()

        def sql_orderby(self, db_cursor, db_session):
            # TODO: postgresql.py, sql_orderby
            """ Function for orderby operation
            , to orderby from table with rider_id (UUID) option. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_orderby(...)')
            # db_cursor.execute(
            #     f"""
            #     SELECT *
            #     FROM {self.T_feature}
            #     ORDER BY rider_id
            #     """
            # )
            # db_session.commit()

        def sql_groupby(self, db_cursor, db_session):
            # TODO: postgresql.py, sql_groupby
            """ Function for sql_groupby operation
            , to sql_groupby from table with rider_id (UUID) option. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_orderby(...)')
            # db_cursor.execute(
            #     f"""
            #     SELECT *,
            #     COUNT(*)
            #     FROM {self.T_feature}
            #     GROUP BY rider_id
            #     """
            # )
            # db_session.commit()

        def sql_inner_join(self, db_cursor, db_session):
            # TODO: postgresql.py, sql_inner_join
            """ Function for inner join operation
            , to inner join from table with another table on two distinct keys. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_inner_join(...)')
            # db_cursor.execute(
            #     f"""
            #     SELECT *
            #     FROM {self.T_feature}
            #     INNER JOIN table_other
            #     ON table_rider.key == table_other.key
            #     """
            # )
            # db_session.commit()

        def sql_left_outer_join(self, db_cursor, db_session):
            # TODO: postgresql.py, sql_left_outer_join
            """ Function for left outer join operation
            , to left outer join from table with another table on two distinct keys. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_left_outer_join(...)')
            # db_cursor.execute(
            #     f"""
            #     SELECT *
            #     FROM {self.T_feature}
            #     LEFT OUTER JOIN table_other
            #     ON table_rider.key == table_other.key
            #     """
            # )
            # db_session.commit()

        def sql_right_outer_join(self, db_cursor, db_session):
            # TODO: postgresql.py, sql_right_outer_join
            """ Function for right outer join operation
            , to right outer join from table with another table on two distinct keys. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_right_outer_join(...)')
            # db_cursor.execute(
            #     f"""
            #     SELECT *
            #     FROM {self.T_feature}
            #     RIGHT OUTER JOIN table_other
            #     ON table_rider.key == table_other.key
            #     """
            # )
            # db_session.commit()

        def sql_full_outer_join(self, db_cursor, db_session):
            # TODO: postgresql.py, sql_full_outer_join
            """ Function for full outer join operation
            , to full outer join from table with another table on two distinct keys. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_full_outer_join(...)')
            # db_cursor.execute(
            #     f"""
            #     SELECT *
            #     FROM {self.T_feature}
            #     FULL OTER JOIN table_other
            #     ON table_rider.key == table_other.key
            #     """
            # )
            # db_session.commit()

        def sql_cross_join(self, db_cursor, db_session):
            # TODO: postgresql.py, sql_cross_join
            """ Function for cross join operation
            , to cross join from table with another table on two distinct keys. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_cross_join(...)')
            # db_cursor.execute(
            #     f"""
            #     SELECT *
            #     FROM {self.T_feature}
            #     CROSS JOIN table_other
            #     ON table_rider.key == table_other.key
            #     """
            # )
            # db_session.commit()

        def sql_self_inner_join(self, db_cursor, db_session):
            # TODO: postgresql.py, sql_self_inner_join
            """ Function for self inner join operation
            , to self inner join from table with another table on two distinct keys. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_self_inner_join(...)')
            # db_cursor.execute(
            #     f"""
            #     SELECT *
            #     FROM {self.T_feature}
            #     SELF JOIN table_other
            #     ON table_rider.key == table_other.key
            #     """
            # )
            # db_session.commit()

        def sql_anti_join(self, db_cursor, db_session):
            # TODO: postgresql.py, sql_anti_join
            """ Function for anti join operation
            , to anti join from table with another table on two distinct keys. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_anti_join(...)')
            # db_cursor.execute(
            #     f"""
            #     SELECT *
            #     FROM {self.T_feature}
            #     ANTI JOIN table_other
            #     ON table_rider.key == table_other.key
            #     """
            # )
            # db_session.commit()

        def sql_semi_join(self, db_cursor, db_session):
            # TODO: postgresql.py, sql_semi_join
            """ Function for semi join operation
            , to semi join from table with another table on two distinct keys. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_semi_join(...)')
            # db_cursor.execute(
            #     f"""
            #     SELECT *
            #     FROM {self.T_feature}
            #     SEMI JOIN table_other
            #     ON table_rider.key == table_other.key
            #     """
            # )
            # db_session.commit()

        def sql_dump(self, db_cursor, data):
            """ Function for dump operation, to take the database and output to a file. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_dump(...)')
            column_names = [desc[0] for desc in db_cursor.description]
            # json throws object serialization for datetime
            # , so to mitigate this convert datetime to string
            temp = []
            for row in data:
                zipper = dict(zip(column_names, row))
                for key, value in zipper.items():
                    if isinstance(value, stamp):
                        zipper[key] = value.isoformat()
                temp.append(zipper)
            root = os.path.abspath(os.curdir)
            ts = stamp.now().strftime('%Y-%m-%d_%H-%M-%S')
            path = Path(root) / 'data' / 'dumps - rideshare-mocked'
            path.mkdir(parents=True, exist_ok=True)
            file_path = path / f'{ts} - dump.json'
            try:
                with open(file_path, 'w') as jsonfile:
                    json.dump(temp, jsonfile, indent=4)
            except (IOError, ValueError) as exception:
                print(f'Exception: {exception}')

        def sql_experimental_json_mb_insert(self, db_cursor, db_session):
            """ Function for insert operation, constraint in MB size. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_experimental_json_mb_insert(...)')
            target_size_bytes = 1 * 1024 * 1024
            row_size_estimate = 256
            counter_inserted_size = 0
            while counter_inserted_size < target_size_bytes:
                print(f'DEBUG:postgresql.py,sql_experimental_json_mb_insert(...)'
                      f',data size:{counter_inserted_size}')
                data_template = self.data_template()
                p = data_template[0]
                q = data_template[1]
                db_cursor.execute(
                    f"""
                    INSERT INTO {self.T_feature}
                    (
                        rider_id,
                        rider_timestamp
                    )
                    VALUES
                    (
                        '{p}',
                        '{q}'
                    )
                    """
                )
                counter_inserted_size += row_size_estimate  # Estimate the size of the inserted row in bytes.
                # If the target size is reached or exceeded, break the loop.
                if counter_inserted_size >= target_size_bytes:
                    break
            db_session.commit()

        def sql_experimental_json_mb_dump(self, db_cursor, data):
            """ Function for dump operation, constraint in MB size. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_experimental_json_mb_dump(...)')

        def sql_experimental_json_mb_delete(self, db_cursor, db_session):
            """ Function for delete operation, constraint in MB size. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_experimental_json_mb_delete(...)')

        def sql_experimental_audit_db_ops(self, db_cursor, db_session):
            """ Function for audit operation, aim to perform a set of predefined DB operations. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_experimental_audit_db_ops(...)')
            self.sql_create(db_cursor, db_session)
            self.sql_insert(db_cursor, db_session)
            self.sql_select(db_cursor, db_session)
            self.sql_update(db_cursor, db_session)
            self.sql_delete_at_random(db_cursor, db_session)
            self.sql_orderby(db_cursor, db_session)
            self.sql_groupby(db_cursor, db_session)

        def sql_experimental_audit_join_ops(self, db_cursor, db_session):
            """ Function for audit operation, aim to perform a set of predefined JOIN operations. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_experimental_audit_join_ops(...)')
            self.sql_inner_join(db_cursor, db_session)
            self.sql_left_outer_join(db_cursor, db_session)
            self.sql_right_outer_join(db_cursor, db_session)
            self.sql_full_outer_join(db_cursor, db_session)
            self.sql_cross_join(db_cursor, db_session)
            self.sql_self_inner_join(db_cursor, db_session)
            self.sql_anti_join(db_cursor, db_session)
            self.sql_semi_join(db_cursor, db_session)

        def sql_experimental_cleanup(self, db_session):
            """ Function for cleanup operation, aim to gracefully release resources. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_experimental_cleanup(...)')
            db_session.cursor().close()
            db_session.close()

        def sql_delete_without_where(self, db_cursor, db_session):
            """ Function for delete operation, deletes all the rows but preserves the table. """
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_delete_without_where(...)')
            db_cursor.execute(
                f"""
                DELETE FROM {self.T_feature}
                """
            )
            db_session.commit()

        def sql_experimental_destroy(self, db_cursor, db_session):
            """ Function for destroy operation, deletes all the rows and the entire table.
            destroy will remove table from database. it will always remove any indexes, rules, triggers
            , and constraints that exist, but, if there's a dependency from a view or a foreign key
            then a CASCADE option must be specified."""
            print(r'DEBUG:postgresql.py,PostgreSqlApi ApiCall sql_experimental_destroy(...)')
            db_cursor.execute(
                f"""
                DROP TABLE {self.T_feature}
                """
            )
            db_session.commit()

        def data_template(self) -> List[Union[str, int]]:
            # TODO:postgresql.py,data_template,audit return type is List[Union[str],int]]
            """
            :functionality: Resembles a table data structure for the PostgreSQL database.
            :return: List[Union[str,int]]
            :visually: [ ...[...,...],[...,...],[rider_id,rider_timestamp],[...,...],[...,...]... ]
            """
            self.table_rider.update({'rider_id': str(hasher())})
            local_time = stamp.now()
            time_range_algorithm = DF.DF_SECONDS*DF.DF_HOURS*DF.DF_HOURS*DF.DF_MONTH*DF.DF_YEAR
            rnd_seconds = rnd.randint(-time_range_algorithm,+time_range_algorithm)
            rnd_time = local_time + datetime.timedelta(seconds=rnd_seconds)
            self.table_rider.update({'rider_timestamp': rnd_time.strftime('%Y-%m-%d %H:%M:%S')})
            p = self.table_rider['rider_id']
            q = stamp.strptime(self.table_rider['rider_timestamp'], "%Y-%m-%d %H:%M:%S")
            return [p, q]
