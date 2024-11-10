import re
from typing import Dict, Pattern

class Traductor:
    def __init__(self) -> None:
        self.translation_dict: Dict[str, str] = {
            "SELECT": "TRAEME",
            "*": "TODO",
            "FROM": "DE LA TABLA",
            "WHERE": "DONDE",
            "GROUP BY": "AGRUPANDO POR",
            "HAVING": "WHERE DEL GROUP BY",
            "JOIN": "MEZCLANDO",
            "ON": "EN",
            "INSERT INTO": "METE EN",
            "VALUES": "LOS VALORES",
            "UPDATE": "ACTUALIZA",
            "SET": "SETEA",
            "DELETE FROM": "BORRA DE LA",
            "ALTER TABLE": "CAMBIA LA TABLA",
            "ADD COLUMN": "AGREGA LA COLUMNA",
            "DROP COLUMN": "ELIMINA LA COLUMNA",
            "COUNT": "CONTANDO",
            "AND": "Y",
            "BETWEEN": "ENTRE",
            "NOT NULL": "NO NULO",
            "NOT": "NO",
            "NULL": "NULO",
        }
        self.usql_to_sql_mapping: Dict[str, str] = {
            v.upper(): k for k, v in self.translation_dict.items()
        }

    def translate(self, query: str, direction: str = 'sql_to_usql') -> str:
        mapping: Dict[str, str] = (
            self.translation_dict if direction == 'sql_to_usql' else self.usql_to_sql_mapping
        )
        tokens: list[str] = re.findall(r'\w+|[^\w\s]', query)
        translated_tokens: list[str] = []
        i: int = 0
        while i < len(tokens):
            matched: bool = False
            for size in (3, 2, 1):
                if i + size <= len(tokens):
                    phrase_tokens = tokens[i:i+size]
                    phrase = ' '.join(phrase_tokens).upper()
                    phrase = re.sub(r'\s+', ' ', phrase.strip())
                    if phrase in mapping:
                        translated_phrase = mapping[phrase]
                        translated_tokens.append(translated_phrase)
                        i += size
                        matched = True
                        break
            if not matched:
                translated_tokens.append(tokens[i])
                i += 1
        output: str = ''
        for idx, token in enumerate(translated_tokens):
            if idx == 0:
                output += token
            else:
                if token in ',;)' or translated_tokens[idx - 1] in '([':
                    output += token
                else:
                    output += ' ' + token
        return output

    def sql_to_usql(self, query: str) -> str:
        return self.translate(query, direction='sql_to_usql')

    def usql_to_sql(self, query: str) -> str:
        return self.translate(query, direction='usql_to_sql')
