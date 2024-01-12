SELECT
  patient_id,
  first_name,
  last_name
FROM
  patients
GROUP BY
  patient_id,
  diagnosis
HAVING
  COUNT(diagnosis) > 1
ORDER BY
  patient_id
  
  /*
   Start by selecting a question by pressing 'Start' or 'View All Questions'.
   Use the resources and information about the database from the left panel to help.
   Press the run button to execute the query.
   Question is automatically validated every time you execute the query.
   Make your output match the expected output.


   Keybinds:
   [ctrl + enter]: Execute the SQL
   [ctrl + q]: Auto-format the SQL
   */
