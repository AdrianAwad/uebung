import GradingBO from './GradingBO';

export default class testAPI {
    static #api = null;

    // Local Python backend
    #testBaseURL ='http://localhost:5000/test';

    //Grading related
    #getAllGradesURL = () => `${this.#testBaseURL}/grading`
    #getGradeURL = (id) => `${this.#testBaseURL}/grading/${id}`
    #addGradeURL = () => `${this.#testBaseURL}/grading`;
    #updateGradeURL = (id) => `${this.#testBaseURL}/grade/${id}`;
    #deleteGradeURL = (id) => `${this.#testBaseURL}/grading/${id}`;

 /**
   * Get the Singelton instance
   *
   * @public
   */
  static getAPI() {
    if (this.#api == null) {
      this.#api = new testAPI();
    }
    return this.#api;
  }

/**
*  Returns a Promise which resolves to a json object.
*  The Promise returned from fetch() won’t reject on HTTP error status even if the response is an HTTP 404 or 500.
*  fetchAdvanced throws an Error also an server status errors
*/
#fetchAdvanced = (url, init) => fetch(url, init)
.then(res => {
  // The Promise returned from fetch() won’t reject on HTTP error status even if the response is an HTTP 404 or 500.
  if (!res.ok) {
    throw Error(`${res.status} ${res.statusText}`);
  }
  return res.json();
}
)


  //----------Grading relevant operation-------------------------

   /**
   * Returns a Promise, which resolves to an Array of GrandingBOs
   * @public
   */
  getAllGrades(){
    return this.#fetchAdvanced(this.#getAllGradesURL()).then((responseJSON)=> {
      let responseGradingBOs = GradingBO.fromJSON(responseJSON);
      console.log('response' + responseGradingBOs);
      return new Promise(function(resolve){
          resolve(responseGradingBOs);
      })
    })

  }

/**
 * Returns a Promise, which resolves to a GradingBO
 * @param {gradeID} gradingID to be retrieved
 * @public
 */
  getGrade(gradeID){
    return this.#fetchAdvanced(this.#getGradeURL(gradeID)).then((responseJSON)=> {
      let responseGradingBOs = GradingBO.fromJSON(responseJSON)[0];
      return new Promise(function(resolve){
        resolve(responseGradingBOs);
      })
    })

  }

 /**
 * Adds a grade and returns a Promise, which resolves to a new GradingBO object
 * @param {grading} gradingBO to be added. The ID of the new grade is set by the backend
 * @public
 */
  addGrade(grading){
      return this.#fetchAdvanced(this.#addGradeURL(), {
          method: 'POST',
          headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
          },
          body: JSON.stringify(grading)
        }).then((responseJSON) => {
            let responseGradeBO = GradingBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseGradeBO);
            })
          })
  }

  /**
 * Updates a gradeand returns a Promise, which resolves to a GradingBO.
 *
 * @param {gradingBO} the gradingBO to be updated
 * @public
 */
  updateGrade(gradingBO){
      return this.#fetchAdvanced(this.#updateGradeURL(gradingBO.getID()), {
          method: 'PUT',
          headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
          },
          body: JSON.stringify(gradingBO)
          }).then((responseJSON) => {
          let responseGradingBO = GradingBO.fromJSON(responseJSON)[0];
          return new Promise(function (resolve) {
            resolve(responseGradingBO);
          })
        })
  }


/**
 * Returns a Promise, which resolves to an Array of GradingBOs
 * @param {gradeID} the gradingID to be deleted
 * @public
 */
  deleteGrade(gradeID){
      return this.#fetchAdvanced(this.#deleteGradeURL(gradeID), {
          method: 'DELETE'
        }).then((responseJSON) => {
          let responseGradingBO = GradingBO.fromJSON(responseJSON)[0];
          return new Promise(function (resolve) {
            resolve(responseGradingBO);
          })
        })
  }
}