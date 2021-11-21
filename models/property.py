from flask import Blueprint
from app.db import Connection

class PropertyModel:
    
    def get_properties(year=None, city=None, status=None):
        try:
            conn = Connection()
            conn.open()
            
            sql = """
                        SELECT 
                            cte.id, 
                            cte.address, 
                            cte.city, 
                            cte.price,
                            cte.description, 
                            cte.`year`,
                            s.name AS status_name,
                            s.label AS status_label
                        FROM (
                                SELECT 
                                        p.id, 
                                        p.address, 
                                        p.city, 
                                        p.price,
                                        p.description, 
                                        p.`year`,
                                        (select max(sh.id) as id
                                        FROM habi_db.status_history as sh where sh.property_id = p.id group by sh.property_id) as history_id
                                        FROM habi_db.property as p
                                ) as cte
                                INNER JOIN habi_db.status_history as sh on sh.id = cte.history_id
                                INNER JOIN habi_db.status as s on s.id = sh.status_id
                               WHERE sh.status_id IN (3, 4, 5)
                        """
            params = []
            if year:
                sql = '{0} AND cte.year IN %s'.format(sql)
                params.append(year.split(','))
            if city:
                sql = "{0} AND cte.city = %s".format(sql)
                params.append(city.split(','))
            if status:
                sql = '{0} AND sh.status_id IN %s'.format(sql)
                params.append(status.split(','))
            result = conn.query(sql, params)                    
           
            return result
        except Exception as e:
            print(e)
            raise(e)
        
        