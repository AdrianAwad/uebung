import BusinessObject from './BusinessObject';


export default class GradingBO extends BusinessObject {

/// Represents a grade which can be given a student.

    constructor(aGrade){
        super();
        this.grade=aGrade;
    }

    //Sets the grade
    setGrade(aGrade){
      this.grade = aGrade;
    }

    //Reads out the grade
    getGrade(){
        return this.grade;
    }

    //Returns an Array of GradingBOs from a given JSON structure.

    static fromJSON(gradings) {
        let result = [];

        if (Array.isArray(gradings)) {
            gradings.forEach((g) => {
                Object.setPrototypeOf(g, GradingBO.prototype);
                result.push(g);
            })
        }
        // it's a single object and not an array
        else {
            let g = gradings;
            Object.setPrototypeOf(g, GradingBO.prototype);
            result.push(g);
        }

        return result;
    }
}
