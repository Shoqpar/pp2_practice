CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact_by_value(
    p_value VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value OR phone = p_value;
END;
$$;


-- 3. Bulk insert/update with validation
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER;
    current_name TEXT;
    current_phone TEXT;
BEGIN
    IF array_length(p_names, 1) IS DISTINCT FROM array_length(p_phones, 1) THEN
        RAISE EXCEPTION 'Names and phones arrays must have the same length';
    END IF;

    FOR i IN 1 .. array_length(p_names, 1) LOOP
        current_name := p_names[i];
        current_phone := p_phones[i];

        IF current_phone ~ '^\+7[0-9]{10}$' THEN
            IF EXISTS (SELECT 1 FROM contacts WHERE name = current_name) THEN
                UPDATE contacts
                SET phone = current_phone
                WHERE name = current_name;
            ELSE
                INSERT INTO contacts(name, phone)
                VALUES (current_name, current_phone);
            END IF;
        ELSE
            RAISE NOTICE 'Incorrect data: %, %', current_name, current_phone;
        END IF;
    END LOOP;
END;
$$;