from database.DB_connect import DBConnect


class DAO():

    @staticmethod
    def getNodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct c.Localization as loc
                    from classification c 
                    order by c.Localization asc"""
        cursor.execute(query)
        for row in cursor:
            result.append(row['loc'])
        cursor.close()
        conn.close()
        return (result)

    @staticmethod
    def peso(g1,g2):
        conn = DBConnect.get_connection()

        result = 0

        cursor = conn.cursor(dictionary=True)
        query = """select count( distinct i.`Type`  ) as peso
                    from interactions i ,(select distinct c.GeneID as gene
                                            from classification c 
                                            where c.Localization =%s) as c1, (select distinct c.GeneID as gene
                                                                                    from classification c 
                                                                                    where c.Localization =%s) as c2	
                    where (i.GeneID1=c1.gene and i.GeneID2=c2.gene) or (i.GeneID2=c1.gene and i.GeneID1=c2.gene) 
                    """
        cursor.execute(query,(g1,g2,))
        for row in cursor:
            result = row['peso']
        cursor.close()
        conn.close()
        return (result)



