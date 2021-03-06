/* 
 * MDES for Merchants
 *
 * The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br> __Authentication__ Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br> 1 . A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br>  __Encryption__<br>  All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br> __Additional Encryption of Sensitive Data__ In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java) 
 *
 * The version of the OpenAPI document: 1.2.9
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using OpenAPIDateConverter = Mastercard.Developer.DigitalEnablement.Client.Client.OpenAPIDateConverter;

namespace Mastercard.Developer.DigitalEnablement.Client.Model
{
    /// <summary>
    /// TransactRequestSchema
    /// </summary>
    [DataContract]
    public partial class TransactRequestSchema :  IEquatable<TransactRequestSchema>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="TransactRequestSchema" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected TransactRequestSchema() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="TransactRequestSchema" /> class.
        /// </summary>
        /// <param name="responseHost">The host that originated the request. Future calls in the same conversation may be routed to this host. .</param>
        /// <param name="requestId">Unique identifier for the request.  (required).</param>
        /// <param name="tokenUniqueReference">Globally unique identifier for the Token, as assigned by MDES.    __Max Length:64__  (required).</param>
        /// <param name="dsrpType">What type of DSRP cryptogram to create. Must be either UCAF or M_CHIP.     __Max Length:64__  (required).</param>
        /// <param name="unpredictableNumber">HEX Encoded data (case sensitive) provided by the merchant to provide variability and uniqueness to the generation of a cryptogram.  __Length:8__  (required).</param>
        /// <param name="amount">Transaction amount to be authorized. Note that refund transactions are not supported – this value must be a positive amount and can contain up to 12 digits, inclusive of any digits in the currency exponent.     __Max Length:13__ .</param>
        /// <param name="currencyCode">The transaction currency. Expressed as a 3-character ISO 4217 currency code. .</param>
        public TransactRequestSchema(string responseHost = default(string), string requestId = default(string), string tokenUniqueReference = default(string), string dsrpType = default(string), string unpredictableNumber = default(string), string amount = default(string), string currencyCode = default(string))
        {
            // to ensure "requestId" is required (not null)
            if (requestId == null)
            {
                throw new InvalidDataException("requestId is a required property for TransactRequestSchema and cannot be null");
            }
            else
            {
                this.RequestId = requestId;
            }
            
            // to ensure "tokenUniqueReference" is required (not null)
            if (tokenUniqueReference == null)
            {
                throw new InvalidDataException("tokenUniqueReference is a required property for TransactRequestSchema and cannot be null");
            }
            else
            {
                this.TokenUniqueReference = tokenUniqueReference;
            }
            
            // to ensure "dsrpType" is required (not null)
            if (dsrpType == null)
            {
                throw new InvalidDataException("dsrpType is a required property for TransactRequestSchema and cannot be null");
            }
            else
            {
                this.DsrpType = dsrpType;
            }
            
            // to ensure "unpredictableNumber" is required (not null)
            if (unpredictableNumber == null)
            {
                throw new InvalidDataException("unpredictableNumber is a required property for TransactRequestSchema and cannot be null");
            }
            else
            {
                this.UnpredictableNumber = unpredictableNumber;
            }
            
            this.ResponseHost = responseHost;
            this.Amount = amount;
            this.CurrencyCode = currencyCode;
        }
        
        /// <summary>
        /// The host that originated the request. Future calls in the same conversation may be routed to this host. 
        /// </summary>
        /// <value>The host that originated the request. Future calls in the same conversation may be routed to this host. </value>
        [DataMember(Name="responseHost", EmitDefaultValue=false)]
        public string ResponseHost { get; set; }

        /// <summary>
        /// Unique identifier for the request. 
        /// </summary>
        /// <value>Unique identifier for the request. </value>
        [DataMember(Name="requestId", EmitDefaultValue=false)]
        public string RequestId { get; set; }

        /// <summary>
        /// Globally unique identifier for the Token, as assigned by MDES.    __Max Length:64__ 
        /// </summary>
        /// <value>Globally unique identifier for the Token, as assigned by MDES.    __Max Length:64__ </value>
        [DataMember(Name="tokenUniqueReference", EmitDefaultValue=false)]
        public string TokenUniqueReference { get; set; }

        /// <summary>
        /// What type of DSRP cryptogram to create. Must be either UCAF or M_CHIP.     __Max Length:64__ 
        /// </summary>
        /// <value>What type of DSRP cryptogram to create. Must be either UCAF or M_CHIP.     __Max Length:64__ </value>
        [DataMember(Name="dsrpType", EmitDefaultValue=false)]
        public string DsrpType { get; set; }

        /// <summary>
        /// HEX Encoded data (case sensitive) provided by the merchant to provide variability and uniqueness to the generation of a cryptogram.  __Length:8__ 
        /// </summary>
        /// <value>HEX Encoded data (case sensitive) provided by the merchant to provide variability and uniqueness to the generation of a cryptogram.  __Length:8__ </value>
        [DataMember(Name="unpredictableNumber", EmitDefaultValue=false)]
        public string UnpredictableNumber { get; set; }

        /// <summary>
        /// Transaction amount to be authorized. Note that refund transactions are not supported – this value must be a positive amount and can contain up to 12 digits, inclusive of any digits in the currency exponent.     __Max Length:13__ 
        /// </summary>
        /// <value>Transaction amount to be authorized. Note that refund transactions are not supported – this value must be a positive amount and can contain up to 12 digits, inclusive of any digits in the currency exponent.     __Max Length:13__ </value>
        [DataMember(Name="amount", EmitDefaultValue=false)]
        public string Amount { get; set; }

        /// <summary>
        /// The transaction currency. Expressed as a 3-character ISO 4217 currency code. 
        /// </summary>
        /// <value>The transaction currency. Expressed as a 3-character ISO 4217 currency code. </value>
        [DataMember(Name="currencyCode", EmitDefaultValue=false)]
        public string CurrencyCode { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class TransactRequestSchema {\n");
            sb.Append("  ResponseHost: ").Append(ResponseHost).Append("\n");
            sb.Append("  RequestId: ").Append(RequestId).Append("\n");
            sb.Append("  TokenUniqueReference: ").Append(TokenUniqueReference).Append("\n");
            sb.Append("  DsrpType: ").Append(DsrpType).Append("\n");
            sb.Append("  UnpredictableNumber: ").Append(UnpredictableNumber).Append("\n");
            sb.Append("  Amount: ").Append(Amount).Append("\n");
            sb.Append("  CurrencyCode: ").Append(CurrencyCode).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as TransactRequestSchema);
        }

        /// <summary>
        /// Returns true if TransactRequestSchema instances are equal
        /// </summary>
        /// <param name="input">Instance of TransactRequestSchema to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(TransactRequestSchema input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.ResponseHost == input.ResponseHost ||
                    (this.ResponseHost != null &&
                    this.ResponseHost.Equals(input.ResponseHost))
                ) && 
                (
                    this.RequestId == input.RequestId ||
                    (this.RequestId != null &&
                    this.RequestId.Equals(input.RequestId))
                ) && 
                (
                    this.TokenUniqueReference == input.TokenUniqueReference ||
                    (this.TokenUniqueReference != null &&
                    this.TokenUniqueReference.Equals(input.TokenUniqueReference))
                ) && 
                (
                    this.DsrpType == input.DsrpType ||
                    (this.DsrpType != null &&
                    this.DsrpType.Equals(input.DsrpType))
                ) && 
                (
                    this.UnpredictableNumber == input.UnpredictableNumber ||
                    (this.UnpredictableNumber != null &&
                    this.UnpredictableNumber.Equals(input.UnpredictableNumber))
                ) && 
                (
                    this.Amount == input.Amount ||
                    (this.Amount != null &&
                    this.Amount.Equals(input.Amount))
                ) && 
                (
                    this.CurrencyCode == input.CurrencyCode ||
                    (this.CurrencyCode != null &&
                    this.CurrencyCode.Equals(input.CurrencyCode))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.ResponseHost != null)
                    hashCode = hashCode * 59 + this.ResponseHost.GetHashCode();
                if (this.RequestId != null)
                    hashCode = hashCode * 59 + this.RequestId.GetHashCode();
                if (this.TokenUniqueReference != null)
                    hashCode = hashCode * 59 + this.TokenUniqueReference.GetHashCode();
                if (this.DsrpType != null)
                    hashCode = hashCode * 59 + this.DsrpType.GetHashCode();
                if (this.UnpredictableNumber != null)
                    hashCode = hashCode * 59 + this.UnpredictableNumber.GetHashCode();
                if (this.Amount != null)
                    hashCode = hashCode * 59 + this.Amount.GetHashCode();
                if (this.CurrencyCode != null)
                    hashCode = hashCode * 59 + this.CurrencyCode.GetHashCode();
                return hashCode;
            }
        }
    }

}
